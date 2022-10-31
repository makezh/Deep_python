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
SIZE = 1024
END_QUE = '>END'
SPLIT_CHAR = '†'


def check_argv():
    if not (0 < len(sys.argv[1:]) < 3):
        raise AttributeError(
            "there are 2 arguments: number of arguments and name of file with urls"
        )

    try:
        int(sys.argv[1])
    except ValueError as v_err:
        raise ValueError(
            "1st argument should be INTEGER"
        ) from v_err

    if not (os.path.exists(sys.argv[2])):
        raise FileNotFoundError(
            f"file {sys.argv[2]} not found"
        )


def process_file(file: str):
    urls = queue.Queue()
    with open(file, 'r', encoding=FORMAT) as file_urls:
        for line in file_urls:
            urls.put(line.strip() + SPLIT_CHAR)
        urls.put(END_QUE)
    return urls


def client_connect(addr: tuple[str, int]):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(addr)
    return sock


def client_request(sock: socket.socket,
                   que: queue.Queue):
    while que.qsize() > 0:
        # отправляем url из очереди
        data = que.get().encode(FORMAT)
        sock.sendall(data)

        # принимаем ответ с сервера
        print(sock.recv(SIZE).decode(FORMAT))


def main():
    if __name__ == '__main__':
        check_argv()
        n_threads = int(sys.argv[1])
        file = sys.argv[2]

        sock = client_connect(ADDR)
        urls_que = process_file(file)

        threads = [
            threading.Thread(
                target=client_request,
                args=(sock, urls_que),
            )
            for _ in range(n_threads)
        ]

        for thread in threads:
            thread.start()

        for thread in threads:
            thread.join()

        print(">>>THE END<<<")

        sock.close()
        return "end of main in client"
    return "just end of client"


main()
