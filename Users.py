import json


class Users:
    def __init__(self, filename: str):
        self.filename = filename

    def load(self) -> dict:
        return json.load(open(self.filename, "r"))

    def dump(self, ip):
        json.dump(ip, open(self.filename, "w"))

    def is_exist(self, ip: str) -> bool:
        return ip in self.load()

    def set_field_value(self, ip: str, field: str, value: str | bool):
        ips = self.load()
        ips[ip][field] = value
        self.dump(ips)

    def get_field_value(self, ip: str, field: str) -> str | bool | None:
        if self.is_exist(ip):
            return self.load()[ip][field]
        else:
            return None

    def add_ip(self, ip: str, login: str, password: str):
        users = self.load()
        users[ip] = {
            'username': login,
            'password': password,
            'is_logged_in': True
        }
        self.dump(users)
