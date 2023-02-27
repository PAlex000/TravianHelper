import re

from src.exceptions.EmailError import EmailError
from src.exceptions.PasswordError import PasswordError


class LoginInputCheck:
    regexForEmail = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b"

    def __init__(self, email, password, saveEmailBtn):
        self.__email = email
        self.__password = password
        self.__saveEmailBtn = saveEmailBtn

    @property
    def email(self):
        return self.__email

    @property
    def password(self):
        return self.__password

    @property
    def saveEmailBtn(self):
        return self.__saveEmailBtn

    def getLoginCredentials(self):
        self.__emailCheck()
        self.__passwordCheck()
        return {
            "email": self.__email,
            "password": self.__password,
            "saveEmail": self.__saveEmailBtn,
        }

    def __emailCheck(self):
        if not self.__isEmailMatched():
            raise EmailError

    def __isEmailMatched(self):
        return re.fullmatch(LoginInputCheck.regexForEmail, self.__email)

    def __passwordCheck(self):
        if self.__isPasswordEmpty():
            raise PasswordError

    def __isPasswordEmpty(self):
        return len(self.__password) == 0
