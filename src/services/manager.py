import json
import os.path
from dataclasses import asdict
from src.models import PasswordDto
from contextlib import suppress


class PasswordManager:

    __file_name = os.path.join(os.path.dirname(os.path.abspath(__name__)), "static/passwords.json")

    def __init__(self, source: str):
        """
        PasswordManager helps to manage secret passwords.
        :param source: Name of Source the password made for
        """
        self.source = source
        # self.check_file()

    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value: str):
        if value and isinstance(value, str):
            self._source = value
        else:
            ValueError("Source must be a string")

    def save_password(self, password: str):
        with open(self.__file_name, "r+") as file:
            try:
                data: dict = json.load(file)
            except json.JSONDecodeError:
                data = {}
            data[self.source] = asdict(PasswordDto(password))
            file.seek(0)
            file.truncate(0)
            json.dump(data, file, indent=2)

    def read_password(self):
        with open(self.__file_name, "r") as file:
            with suppress(Exception):
                data: dict = json.load(file)
                if password := data.get(self._source, None):
                    return PasswordDto(**password).password

    @staticmethod
    def get_saved_sources() -> list | None:
        with open(PasswordManager.__file_name, "r") as file:
            with suppress(Exception):
                data: dict = json.load(file)
                return data.keys() if data else None
