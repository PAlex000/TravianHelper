import pytest
from src.webscrape.login import Login
from tests import BaseTest

class Test_Login(BaseTest):
    
    def testLoginWithCorrectCredentials(self):
        self._driverSetUp()
        self._getCredentialsFromJSON()
        saveEmail = 0
        self.login = Login(self._email, self._password, saveEmail, self._driver)
        self.login.login()
        assert self._driver.current_url == "https://lobby.kingdoms.com/#/" and self.login.email == self._email and self.login.password == self._password
        self._driverQuit()

    def testLoginWithIncorrectCredentials(self):
        self._driverSetUp()
        email = "definitelyAgoodEmail@gmail.com"
        password = "1234"
        saveEmail = 0
        self.login = Login(email, password, saveEmail, self._driver)
        with pytest.raises(SystemExit):
            self.login.login()
        self._driverQuit()
