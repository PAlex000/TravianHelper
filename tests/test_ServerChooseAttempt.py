import pytest
from tests import BaseTest
from src.gui.attempts.serverChooseAttempt import ServerChooseAttempt
from src.exceptions.serverNameError import ServerNameError
from src.exceptions.serverElementError import ServerElementError

class Test_ServerChooseAttempt(BaseTest):

    def testServerChooseAttemptWithOneServer(self):
        attempt = ServerChooseAttempt("COM3X3", "element")
        attempt.getStatus()
        assert attempt.serverName == "COM3X3" and attempt.serverElement == "element"

    def testServerChooseAttemptWithoutServerName(self):
        with pytest.raises(ServerNameError):
            attempt = ServerChooseAttempt("", "")
            attempt.getStatus()

    def testServerChooseAttemptWithoutServerElement(self):
        with pytest.raises(ServerElementError):
            attempt = ServerChooseAttempt("COM3x3", "")
            attempt.getStatus()
