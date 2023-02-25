import pytest

from src.exceptions.serverNameError import ServerNameError
from src.gui.attempts.serverChooseAttempt import ServerChooseAttempt
from tests import BaseTest


class Test_ServerChooseAttempt(BaseTest):

    def testServerChooseAttemptWithOneServer(self):
        attempt = ServerChooseAttempt("COM3X3", "element")
        attempt.getStatus()
        assert attempt.serverName == "COM3X3"

    def testServerChooseAttemptWithoutServerName(self):
        with pytest.raises(ServerNameError):
            attempt = ServerChooseAttempt("", "")
            attempt.getStatus()
