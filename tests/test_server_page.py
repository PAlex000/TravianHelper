from tests import BaseTest

from src.gui.pages.server_page import ServerPage


class TestServerPage(BaseTest):
    def test_with_default_values(self):
        server_page = ServerPage("element")

        assert (
            server_page.server_details == {"servername": "", "serverelement": ""}
            and server_page.server_count.get() == 0
            and not server_page.server_names
        )

        server_page.destroy()

    def test_server_names(self):
        server = {
            "COM3X3": "ElementOfCOM3X3",
            "COM1X3": "ElementOfCOM1X3",
            "COM2X3": "ElementOfCOM2X3",
        }
        server_page = ServerPage(server)
        server_page.server_names = "COM15X3"
        server_page.after(500, lambda: server_page.choose_button.invoke())
        server_page.create_server_page()

        assert server_page.server_names == ["COM15X3", "COM3X3", "COM1X3", "COM2X3"]

    def test_server_details(self):
        server = {
            "COM3X3": "ElementOfCOM3X3",
            "COM1X3": "ElementOfCOM1X3",
            "COM2X3": "ElementOfCOM2X3",
        }
        server_page = ServerPage(server)

        server_page.after(500, lambda: server_page.server_count.set(2))
        server_page.after(1000, lambda: server_page.choose_button.invoke())
        server_page.create_server_page()

        assert server_page.server_details == {
            "servername": "COM2X3",
            "serverelement": "ElementOfCOM2X3",
        }
