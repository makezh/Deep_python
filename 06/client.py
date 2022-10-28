import queue
import socket
import sys
import os
import threading

# CONSTANTS
IP = socket.gethostbyname(socket.gethostname())
PORT = 5555
ADDR = (IP, PORT)
FORMAT = 'utf-8'


def check_argv():
    if not (0 < len(sys.argv[1:]) < 3):
        raise AttributeError(
            "there are 2 arguments: number of arguments and name of file with urls"
        )

    try:
        int(sys.argv[1])
    except ValueError:
        raise ValueError(
            "1st argument should be INTEGER"
        )

    if not (os.path.exists(sys.argv[2])):
        raise FileNotFoundError(
            f"file {sys.argv[2]} not found"
        )


def batch_file(file: str, workers: int):
    with open(file, 'r') as f:
        length = len(f.readlines())
    return length // workers


def process_file(file: str, thread: int, for_one: int):
    urls = queue.Queue(for_one)
    with open(file, 'r') as f:
        for i, line in enumerate(f):
            for url in range(for_one):
                if i == (thread * for_one + url):
                    urls.put(line.strip())
    return urls


def main():
    check_argv()
    N_THREADS = int(sys.argv[1])
    FILE = sys.argv[2]
    for_one = batch_file(FILE, N_THREADS)
    threads = [
        threading.Thread(
            target=process_file,
            args=(FILE, thread, for_one),
        )
        for thread in range(N_THREADS)
    ]

    for th in threads:
        th.start()

    for th in threads:
        th.join()

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)


if __name__ == '__main__':
    main()
