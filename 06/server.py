import json
from collections import Counter
import sys
import argparse
from queue import Queue

import requests
from bs4 import BeautifulSoup
import socket
import threading

# CONSTANTS
IP = socket.gethostbyname(socket.gethostname())
PORT_R = 5555
PORT_S = 6666
ADDR_R = (IP, PORT_R)
ADDR_S = (IP, PORT_S)
FORMAT = 'utf-8'
SIZE = 1024
END_QUE = '>END'


def create_parser():
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('-w', '--workers', type=int, default=1)
    arg_parser.add_argument('-k', '--top_k', type=int, default=5)

    return arg_parser


def server_connect(ADDR1, ADDR2):
    socket_1 = socket.socket()
    socket_2 = socket.socket()

    socket_1.bind(ADDR1)
    socket_1.listen(0)
    socket_2.bind(ADDR2)
    socket_2.listen(0)
    return socket_1, socket_2


def common_words(url: str, count_words: int):
    word_count = Counter()
    request = requests.get(url, timeout=3)
    soup = BeautifulSoup(request.text, 'html.parser')
    all_words = soup.get_text(" ", strip=True).lower().split()

    for word in all_words:
        cln_word = word.strip('.,?')
        # не будем считать предлоги/союзы
        if len(cln_word) > 3:
            word_count[cln_word] += 1

    res_dict = {url: {words[0]: words[1] for words in word_count.most_common(count_words)}}
    res_json = json.dumps(res_dict, ensure_ascii=False)

    return res_json


def get_urls(conn, que):
    while True:
        urls = conn.recv(SIZE).decode(FORMAT)
        for url in urls:
            if url == END_QUE:
                return
            if url:
                que.put(url)


def process_urls(conn, lock, que, top_k, count):
    while True:
        url = que.get()
        if url == END_QUE:
            que.put(END_QUE)
            break
        url_json = common_words(url, top_k)
        conn.send(url_json.encode(FORMAT))
        with lock:
            count += 1
            print(count, "ссылок обработано")


def main():
    parser = create_parser()
    namespace = parser.parse_args(sys.argv[1:])
    workers, top_k = namespace.workers, namespace.top_k
    server_rec, server_send = server_connect(ADDR_R, ADDR_S)

    conn_r, _ = server_rec.accept()
    conn_s, _ = server_send.accept()
    lock = threading.Lock()
    que = Queue()
    count = 0
    threads = [
        threading.Thread(target=process_urls, args=(conn_s, lock, que, top_k, count))
        for _ in range(workers)
    ]

    threads.append(
        threading.Thread(target=get_urls, args=(conn_r, que))
    )

    for th in threads:
        th.start()

    for th in threads:
        th.join()

    server_rec.close()
    server_send.close()


if __name__ == '__main__':
    main()
