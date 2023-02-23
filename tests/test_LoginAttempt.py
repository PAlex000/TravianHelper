import pytest
from tests import BaseTest
from src.gui.attempts.loginAttempt import LoginAttempt
from src.exceptions.EmailError import EmailError
from src.exceptions.PasswordError import PasswordError


class Test_LoginAttempt(BaseTest):
    
    def testLoginAttemptWithCorrectCredentials(self):
        self._getCredentialsFromJSON()
        attempt = LoginAttempt(self._email, self._password, 0)
        attempt.getStatus()
        assert attempt.email == self._email and attempt.password == self._password and attempt.saveEmailBtn == 0

    def testLoginAttemptWithIncorrectEmail(self):
        with pytest.raises(EmailError):
            attempt = LoginAttempt("ThisIsNotAnEmail", "", 0)
            attempt.getStatus()
            
    def testLoginAttemptWithIncorrectPassword(self):
        with pytest.raises(PasswordError):
            attempt = LoginAttempt("correctEmail@gmail.com", "", 0)
            attempt.getStatus()
