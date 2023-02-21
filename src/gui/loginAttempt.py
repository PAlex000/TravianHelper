import re
from src.exceptions.EmailError import EmailError
from src.exceptions.PasswordError import PasswordError

class LoginAttempt():

    regexForEmail = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

    def __init__(self, email, password):
        self.__email = email
        self.__password = password

    @property
    def email(self):
        return self.__email
    
    @property
    def password(self):
        return self.__password

    def getStatus(self):
        self.__emailCheck()
        self.__passwordCheck()
        return [self.__email, self.__password]

    def __emailCheck(self):
        if not self.__isEmailMatched():
            raise EmailError
    
    def __isEmailMatched(self):
        return True if re.fullmatch(LoginAttempt.regexForEmail, self.__email) else False

    def __passwordCheck(self):
        if self.__isPasswordEmpty():
            raise PasswordError
    
    def __isPasswordEmpty(self):
        return True if len(self.__password) == 0 else False
    