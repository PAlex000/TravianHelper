from tkinter import BOTH, Frame

from src.gui.pages.default_page import DefaultPage
from tests import BaseTest


class TestDefaultPage(BaseTest):
    def test_default_page_with_title(self):
        default_page = DefaultPage("Title")

        assert (
            default_page.properties == {"ipadx": 20, "ipady": 10, "fill": BOTH}
            and default_page.title() == "Title"
        )

        default_page.destroy()

    def test_default_page_without_title(self):
        default_page = DefaultPage()

        assert default_page.title() == "unnamed"

        default_page.destroy()

    def test_default_page_frame(self):
        default_page = DefaultPage("Title")

        assert isinstance(default_page.frame, Frame)

        default_page.destroy()
