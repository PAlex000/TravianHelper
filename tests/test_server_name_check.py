import pytest

from src.exceptions.server_name_error import ServerNameError
from src.gui.attempts.server_name_check import ServerNameCheck
from tests import BaseTest


class TestServerNameCheck(BaseTest):
    def test_server_name_check_attempt_with_one_server(self):
        attempt = ServerNameCheck("COM3X3", "element")
        attempt.get_server_details()
        assert attempt.server_name == "COM3X3"

    def test_server_name_check_attempt_without_server_name(self):
        with pytest.raises(ServerNameError):
            attempt = ServerNameCheck("", "")
            attempt.get_server_details()
