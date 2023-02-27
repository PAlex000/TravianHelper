from tests import BaseTest

from src.gui.pages.serverPage import ServerPage


class Test_ServerPage(BaseTest):
    def testWithDefaultValues(self):
        serverpage = ServerPage("element")

        assert (
            serverpage.serverDetails == {"servername": "", "serverelement": ""}
            and serverpage.serverCount.get() == 0
            and not serverpage.serverNames
        )

        serverpage.destroy()

    def testServerNames(self):
        server = {
            "COM3X3": "ElementOfCOM3X3",
            "COM1X3": "ElementOfCOM1X3",
            "COM2X3": "ElementOfCOM2X3",
        }
        serverpage = ServerPage(server)
        serverpage.serverNames = "COM15X3"
        serverpage.after(500, serverpage.chooseButton.invoke())
        serverpage.createServerPage()

        assert serverpage.serverNames == ["COM15X3", "COM3X3", "COM1X3", "COM2X3"]

    def testServerDetails(self):
        server = {
            "COM3X3": "ElementOfCOM3X3",
            "COM1X3": "ElementOfCOM1X3",
            "COM2X3": "ElementOfCOM2X3",
        }
        serverpage = ServerPage(server)

        serverpage.after(500, lambda: serverpage.serverCount.set(2))
        serverpage.after(1000, serverpage.chooseButton.invoke())
        serverpage.createServerPage()

        assert serverpage.serverDetails == {
            "servername": "COM2X3",
            "serverelement": "ElementOfCOM2X3",
        }
