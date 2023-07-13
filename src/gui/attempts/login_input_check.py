import re

from src.exceptions.email_error import EmailError
from src.exceptions.password_error import PasswordError


class LoginInputCheck:
    regex_for_email = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b"

    def __init__(self, email, password, save_email):
        self.__email = email
        self.__password = password
        self.__save_email_btn = save_email

    @property
    def email(self):
        return self.__email

    @property
    def password(self):
        return self.__password

    @property
    def save_email_btn(self):
        return self.__save_email_btn

    def get_login_credentials(self):
        self.__email_check()
        self.__password_check()
        return {
            "email": self.__email,
            "password": self.__password,
            "saveEmail": self.__save_email_btn,
        }

    def __email_check(self):
        if not self.__is_email_matched():
            raise EmailError

    def __is_email_matched(self):
        return re.fullmatch(LoginInputCheck.regex_for_email, self.__email)

    def __password_check(self):
        if self.__is_password_empty():
            raise PasswordError

    def __is_password_empty(self):
        return len(self.__password) == 0
