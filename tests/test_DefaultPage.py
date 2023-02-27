from tkinter import BOTH, Frame

import pytest

from src.gui.pages.defaultPage import DefaultPage
from tests import BaseTest


class Test_DefaultPage(BaseTest):
    def testDefaultPageWithTitle(self):
        self._driverSetUp()
        defaultPage = DefaultPage("Title")

        assert (
            defaultPage.properties == {"ipadx": 20, "ipady": 10, "fill": BOTH}
            and defaultPage.title() == "Title"
        )

        self._driverQuit()

    def testDefaultPageWithoutTitle(self):
        self._driverSetUp()
        defaultPage = DefaultPage()

        assert defaultPage.title() == "unnamed"

        self._driverQuit()

    def testDefaultPageFrame(self):
        self._driverSetUp()
        defaultPage = DefaultPage("Title")

        assert isinstance(defaultPage.frame, Frame)

        self._driverQuit()
