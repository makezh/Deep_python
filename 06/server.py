import json
import queue
from collections import Counter
import sys
import argparse
from queue import Queue

import socket
import threading
import requests
from bs4 import BeautifulSoup

# CONSTANTS
IP = socket.gethostbyname(socket.gethostname())
PORT = 5555
ADDR = (IP, PORT)
FORMAT = 'utf-8'
SIZE = 1024
END_QUE = '>END'
SPLIT_CHAR = '†'


def create_parser():
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('-w', '--workers', type=int, default=1)
    arg_parser.add_argument('-k', '--top_k', type=int, default=5)

    return arg_parser


def server_connect(addr: tuple[str, int]):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(addr)
    sock.listen()
    return sock


def common_words(url: str, count_words: int):
    word_count = Counter()
    try:
        request = requests.get(url, timeout=3)
    except (requests.ConnectionError,
            requests.exceptions.MissingSchema,
            requests.exceptions.ReadTimeout):
        res_json = json.dumps({url: 'error'}, ensure_ascii=False)
    else:
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


def get_urls(conn: socket.socket, que: queue.Queue):
    while True:
        urls = conn.recv(SIZE).decode(FORMAT).split(SPLIT_CHAR)
        for url in urls:
            if url:
                que.put(url)
            if url == END_QUE:
                return


def process_urls(conn: socket.socket,
                 lock: threading.Lock,
                 que: queue.Queue,
                 top_k: int,
                 count: [int]):
    while True:
        url = que.get()
        if url == END_QUE:
            que.put(END_QUE)
            break
        url_json = common_words(url, top_k)
        conn.send(url_json.encode(FORMAT))
        with lock:
            count[0] += 1
            print(count[0], "ссылок обработано")


def main():
    parser = create_parser()
    namespace = parser.parse_args(sys.argv[1:])
    workers, top_k = namespace.workers, namespace.top_k
    server = server_connect(ADDR)

    conn, _ = server.accept()
    lock = threading.Lock()
    que = Queue()
    count = [0]
    threads = [
        threading.Thread(target=process_urls, args=(conn, lock, que, top_k, count))
        for _ in range(workers)
    ]

    threads.append(
        threading.Thread(target=get_urls, args=(conn, que))
    )

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    print(">>>THE END<<<")

    server.close()


if __name__ == '__main__':
    main()
