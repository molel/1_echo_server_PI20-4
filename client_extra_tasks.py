import socket
import sys
import re
from datetime import datetime

LOG = "client_log.txt"
PASSWORD = "Введите пароль"
NEW_PASSWORD = "Задайте пароль"
SUCCESS = "Вход выполнен"
EXIT = "exit\n"


# функция добавления новой записи в файл логов
def write_log(filename: str, log: str):
    with open(filename, "a") as file:
        file.write(f"{datetime.now()}:\n{log}\n\n")


# отправка логина
def send_login(sock: socket.socket):
    message: str = sock.recv(2048).decode()
    print(message)

    write_log(LOG, f"Получено от сервера '{message}'")  # запись лога

    login: str = input()
    sock.send(login.encode())

    write_log(LOG, f"Отправлено серверу '{login}'")  # запись лога

    message: str = sock.recv(2048).decode()
    print(message)

    write_log(LOG, f"Получено от сервера '{message}'")  # запись лога

    if message == PASSWORD:
        send_password(sock)
    elif message == NEW_PASSWORD:
        send_new_password(sock)
    elif message == SUCCESS:
        send_and_get(sock)


# отправка пароля
def send_password(sock: socket.socket):
    password: str = input()
    sock.send(password.encode())

    write_log(LOG, f"Отправлено серверу '{password}'")  # запись лога

    message: str = sock.recv(2048).decode()
    print(message)

    write_log(LOG, f"Получено от сервера '{message}'")  # запись лога

    if message == SUCCESS:
        send_and_get(sock)
    elif message == PASSWORD:
        send_password(sock)


# отправка нового пароля
def send_new_password(sock: socket.socket):
    new_password: str = input()
    sock.send(new_password.encode())

    write_log(LOG, f"Отправлено серверу '{new_password}'")  # запись лога

    message: str = sock.recv(2048).decode()
    print(message)

    write_log(LOG, f"Получено от сервера '{message}'")  # запись лога

    send_and_get(sock)


# рекурсивная отправка и принятие сообщения
def send_and_get(sock: socket.socket):
    message: str = input("Введите сообщение:\n") + "\n"
    sock.send(message.encode())

    write_log(LOG, f"Отправлено серверу '{message[:-1]}'")  # запись лога

    if message == EXIT:
        return
    message: str = sock.recv(2048).decode()
    print(message)

    write_log(LOG, f"Получено от сервера '{message[:-1]}'")  # запись лога

    send_and_get(sock)


# установка хоста и порта
def get_host_and_name():
    host = input("Введите хост или нажмите Enter для настройки по умолчанию: ")
    port = input("Введите порт или нажмите Enter для настройки по умолчанию: ")
    try:
        port = int(port)
        if 0 <= port <= 2 ** 16 - 1:
            port = 9090
    except:
        port = 9090

    try:
        for octet in host.split("."):
            if 0 <= int(octet) <= 255:
                pass
        if len(host.split(".")) != 4:
            host = "127.0.0.1"
    except:
        host = "127.0.0.1"

    return host, port


def main():
    write_log(LOG, f"Новая сессия")  # запись лога

    host, port = get_host_and_name()
    sock = socket.socket()
    try:
        sock.connect((host, port))
    except:
        write_log(LOG, f"Не удалось подключиться к {host}, {port}")  # запись лога
        print(f"Не удалось подключиться к {host}, {port}")
        sys.exit()

    write_log(LOG, f"Соединено с {host}, {port}")  # запись лога

    send_login(sock)


if __name__ == '__main__':
    main()
