import socket
from datetime import datetime
from Users import Users

LOG = "server_log.txt"
AUTH = "auth.json"
LOGIN = "Введите логин"
PASSWORD = "Введите пароль"
NEW_PASSWORD = "Задайте пароль"
SUCCESS = "Вход выполнен"
EXIT = "exit\n"


# функция добавления новой записи в файл логов
def write_log(filename: str, log: str):
    with open(filename, "a") as file:
        file.write(f"{datetime.now()}:\n{log}\n\n")


users = Users(AUTH)


def bind(sock: socket.socket, port: int = 9090):
    try:
        sock.bind(("127.0.0.1", port))
        write_log(LOG, f"Сервер привязан к 127.0.0.1, {port}")
    except:
        bind(sock, port + 1)


def auth(sock: socket.socket, conn: socket.socket, addr: str):
    global users
    login = get_login(conn)
    write_log(LOG, f"Получено '{login}'")
    if users.is_exist(addr):
        if users.get_field_value(addr, "is_logged_in"):
            echo(sock, conn, addr)
        else:
            get_password(sock, conn, addr, users.get_field_value(addr, "password"))
    else:
        get_new_password(sock, conn, addr, login)


def get_login(conn: socket.socket) -> str:
    conn.send(LOGIN.encode())
    write_log(LOG, f"Отправлено '{LOGIN}'")
    return conn.recv(2048).decode()


def get_password(sock: socket.socket, conn: socket.socket, addr: str, correct_password: str):
    conn.send(PASSWORD.encode())
    write_log(LOG, f"Отправлено '{PASSWORD}'")
    password = conn.recv(2048).decode()
    write_log(LOG, f"Получено '{password}'")
    if correct_password == password:
        echo(sock, conn, addr)
    else:
        get_password(sock, conn, addr, correct_password)


def get_new_password(sock: socket.socket, conn: socket.socket, addr: str, login: str):
    global users
    conn.send(NEW_PASSWORD.encode())
    write_log(LOG, f"Отправлено '{NEW_PASSWORD}'")
    new_password = conn.recv(2048).decode()
    write_log(LOG, f"Получено '{new_password}'")
    users.add_ip(addr, login, new_password)
    echo(sock, conn, addr)


def echo(sock: socket.socket, conn: socket.socket, addr: str):
    users.set_field_value(addr, "is_logged_in", True)
    conn.send(SUCCESS.encode())
    write_log(LOG, f"Отправлено '{SUCCESS}'")
    while True:
        try:
            message = conn.recv(2048)
            write_log(LOG, f"Получено '{message.decode()}'")
            if message.decode() == EXIT:
                users.set_field_value(addr, "is_logged_in", False)
                accept(sock)
            else:
                conn.send(message)
                write_log(LOG, f"Отправлено '{message.decode()}'")
        except:
            accept(sock)
            break


def accept(sock: socket.socket):
    while True:
        try:
            conn, addr = sock.accept()
            write_log(LOG, f"Соединено с {addr[0]}, {addr[1]}")
            auth(sock, conn, addr[0])
            break
        except:
            continue


def main():
    sock: socket.socket = socket.socket()
    bind(sock)
    sock.listen(1)
    accept(sock)


if __name__ == '__main__':
    main()
