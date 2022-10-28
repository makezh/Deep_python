import queue
import socket
import sys
import os
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


def process_file(file: str):
    urls = queue.Queue()
    with open(file, 'r') as f:
        for line in f:
            urls.put(line.strip())
        urls.put(END_QUE)
    return urls


def client_connect(ADDR1, ADDR2):
    socket_1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    socket_1.connect(ADDR1)
    socket_2.connect(ADDR2)
    return socket_1, socket_2


def client_request(sock_rec, sock_send, que):
    # отправляем url из очереди
    sock_send.sendall(que.get().encode(FORMAT))

    # принимаем ответ с сервера
    print(sock_rec.recv(SIZE).decode(FORMAT))


def main():
    check_argv()
    N_THREADS = int(sys.argv[1])
    FILE = sys.argv[2]

    sock_rec, sock_send = client_connect(ADDR_R, ADDR_S)
    urls_que = process_file(FILE)

    threads = [
        threading.Thread(
            target=client_request,
            args=(sock_rec, sock_send, urls_que),
        )
        for _ in range(N_THREADS)
    ]

    for th in threads:
        th.start()

    for th in threads:
        th.join()

    sock_rec.close()
    sock_send.close()


if __name__ == '__main__':
    main()
