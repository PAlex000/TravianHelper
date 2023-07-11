import pytest

from exceptions.email_error import EmailError
from exceptions.password_error import PasswordError
from gui.attempts.login_input_check import LoginInputCheck
from tests import BaseTest


class Test_LoginInputCheck(BaseTest):
    def testLoginInputCheckWithCorrectCredentials(self):
        self._getCredentialsFromJSON()
        attempt = LoginInputCheck(self._email, self._password, 0)
        attempt.getLoginCredentials()
        assert (
            attempt.email == self._email
            and attempt.password == self._password
            and attempt.saveEmailBtn == 0
        )

    def testLoginInputCheckWithIncorrectEmail(self):
        with pytest.raises(EmailError):
            attempt = LoginInputCheck("ThisIsNotAnEmail", "", 0)
            attempt.getLoginCredentials()

    def testLoginInputCheckWithIncorrectPassword(self):
        with pytest.raises(PasswordError):
            attempt = LoginInputCheck("correctEmail@gmail.com", "", 0)
            attempt.getLoginCredentials()
