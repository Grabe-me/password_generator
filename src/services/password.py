import random


class Password:

    __shift = 2
    __valid_items = [33, 36, 38, 45, *list(range(48, 58)), *list(range(63, 91)), 95, *list(range(97, 123))]

    #     97 - 122 = a - z
    #     95 = _
    #     65 - 90 = A - Z
    #     48 - 57 = 0 - 9
    #     63 = ?
    #     64 = @
    #     45 = -
    #     33 = !
    #     36 = $
    #     38 = &

    def __init__(self, password: str, *, reverse: bool = False):
        if reverse:
            self._password = password
            self.show_password()
        else:
            self.password = password
            self.hide_password()

    def check_password(self, password: str):
        if password and len(password) > 7:
            for char in password:
                if not char.isascii() or ord(char) not in self.__valid_items:
                    return False
        return True

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password: str):
        if self.check_password(password):
            self._password = password
        else:
            raise ValueError("Password must contain only ASCII signs and have at least 8 characters")

    def hide_password(self):
        result = ""

        for i in range(len(self.password)):
            char = self._password[i]
            result += chr((ord(char) + self.__shift - 32) % 90 + 33)
        self._password = result
        return self

    def show_password(self):
        result = ""

        for i in range(len(self._password)):
            char = self._password[i]
            result += chr((ord(char) - self.__shift - 33) % 90 + 32)
        self._password = result
        return self

    @staticmethod
    def generate_new_password() -> str:

        return "".join([chr(random.choice(Password.__valid_items)) for _ in range(random.randrange(13, 17))])

    def __str__(self):
        return self.password
