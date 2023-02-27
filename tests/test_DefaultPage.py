from tkinter import BOTH, Frame

from src.gui.pages.defaultPage import DefaultPage
from tests import BaseTest


class Test_DefaultPage(BaseTest):
    def testDefaultPageWithTitle(self):
        defaultPage = DefaultPage("Title")

        assert (
            defaultPage.properties == {"ipadx": 20, "ipady": 10, "fill": BOTH}
            and defaultPage.title() == "Title"
        )

    def testDefaultPageWithoutTitle(self):
        defaultPage = DefaultPage()

        assert defaultPage.title() == "unnamed"

    def testDefaultPageFrame(self):
        defaultPage = DefaultPage("Title")

        assert isinstance(defaultPage.frame, Frame)
