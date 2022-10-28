from collections import Counter
import sys
import argparse
import requests
from bs4 import BeautifulSoup
import socket
import threading

# CONSTANTS
IP = socket.gethostbyname(socket.gethostname())
PORT = 5555
ADDR = (IP, PORT)
FORMAT = 'utf-8'
DISCONNECT_MSG = '/exit'


def create_parser():
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('-w', '--workers', type=int, default=1)
    arg_parser.add_argument('-k', '--top_k', type=int, default=5)

    return arg_parser


def common_words(url: str, count_words: int):
    word_count = Counter()
    request = requests.get(url, timeout=1)
    soup = BeautifulSoup(request.text, 'html.parser')
    all_words = soup.get_text(" ", strip=True).lower().split()

    for word in all_words:
        cln_word = word.strip('.,?')
        # не будем считать предлоги/союзы
        if len(cln_word) > 3:
            word_count[cln_word] += 1

    return word_count.most_common(count_words)


def handle_client(conn, addr):
    connected = True
    while connected:
        msg = conn.recv().decode(FORMAT)
        if msg == DISCONNECT_MSG:
            connected = False

        print(f"[{addr}] {msg}")
        # msg = f"Msg received: {msg}"
        msg = f""
        conn.send(msg.encode(FORMAT))

    conn.close()


def main():
    parser = create_parser()
    namespace = parser.parse_args(sys.argv[1:])
    workers, top_k = namespace.workers, namespace.top_k
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(ADDR)
    server.listen()
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()


if __name__ == '__main__':
    main()
