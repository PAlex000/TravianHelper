import pytest

from src.exceptions.email_error import EmailError
from src.exceptions.password_error import PasswordError
from src.gui.attempts.login_input_check import LoginInputCheck
from tests import BaseTest


class TestLoginInputCheck(BaseTest):
    def test_login_input_check_with_correct_credentials(self):
        self._set_credentials_from_json()
        attempt = LoginInputCheck(self._email, self._password, 0)
        attempt.get_login_credentials()
        assert (
            attempt.email == self._email
            and attempt.password == self._password
            and attempt.save_email_btn == 0
        )

    def test_login_input_check_with_incorrect_email(self):
        with pytest.raises(EmailError):
            attempt = LoginInputCheck("ThisIsNotAnEmail", "", 0)
            attempt.get_login_credentials()

    def test_login_input_check_with_incorrect_password(self):
        with pytest.raises(PasswordError):
            attempt = LoginInputCheck("correctEmail@gmail.com", "", 0)
            attempt.get_login_credentials()
