import pytest

from src.webscrape.login import Login
from tests import BaseTest


class TestLogin(BaseTest):
    def test_login_with_correct_credentials(self):
        self._driver_setup()
        self._set_credentials_from_json()
        save_email = 0
        self.login = Login(self._email, self._password, save_email, self._driver)
        self.login.login()
        assert (
            self._driver.current_url == "https://lobby.kingdoms.com/#/"
            and self.login.email == self._email
            and self.login.password == self._password
        )
        self._driver_quit()

    def test_login_with_incorrect_credentials(self):
        self._driver_setup()
        email = "definitelyAgoodEmail@gmail.com"
        password = "1234"
        save_email = 0
        self.login = Login(email, password, save_email, self._driver)
        with pytest.raises(SystemExit):
            self.login.login()
        self._driver_quit()
