from src.gui.pages.login_page import LoginPage
from src.gui.pages.general_page import GeneralPage
from src.webscrape.driver import Driver
from src.webscrape.server_selection import ServerSelection


class App:
    def __init__(self):
        self.__configured_driver = ""
        self.__general_page = ""

    @property
    def general_page(self):
        return self.__general_page

    def run(self):
        self.__configure_driver()
        self.__login()
        self.__server_selection()
        self.__start_general_page()

    def __configure_driver(self):
        self.__configured_driver = Driver()
        self.__configured_driver.configure_driver()

    def __login(self):
        attempt = LoginPage(self.__configured_driver.driver)
        attempt.create_login_page()
        attempt.start_main_loop()

    def __server_selection(self):
        selected_server = ServerSelection(self.__configured_driver.driver)
        selected_server.server_select()

    def __start_general_page(self):
        GeneralPage(self.__configured_driver.driver).mainloop()
