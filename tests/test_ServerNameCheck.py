import pytest

from exceptions.server_name_error import ServerNameError
from gui.attempts.server_name_check import ServerNameCheck
from tests import BaseTest


class Test_ServerNameCheck(BaseTest):
    def testServerNameCheckAttemptWithOneServer(self):
        attempt = ServerNameCheck("COM3X3", "element")
        attempt.getServerDetails()
        assert attempt.serverName == "COM3X3"

    def testServerNameCheckAttemptWithoutServerName(self):
        with pytest.raises(ServerNameError):
            attempt = ServerNameCheck("", "")
            attempt.getServerDetails()
