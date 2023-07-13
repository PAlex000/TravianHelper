from src.gui.pages.login_page import LoginPage
from src.gui.pages.general_page import GeneralPage
from src.webscrape.driver import Driver
from src.webscrape.login import Login
from src.webscrape.server_selection import ServerSelection


class App:
    def __init__(self):
        self.__configured_driver = ""

    def run(self):
        self.__configure_driver()
        self.__login()
        self.__server_selection()
        self.__start_general_page()

    def __configure_driver(self):
        self.__configured_driver = Driver()
        self.__configured_driver.configure_driver()

    def __login(self):
        attempt = LoginPage()
        attempt.create_login_page()
        attempt.start_main_loop()
        login_credentials = attempt.login_credentials

        Login(
            login_credentials["email"],
            login_credentials["password"],
            login_credentials["saveEmail"],
            self.__configured_driver.driver,
        ).login()

    def __server_selection(self):
        selected_server = ServerSelection(self.__configured_driver.driver)
        selected_server.server_select()

    def __start_general_page(self):
        GeneralPage(self.__configured_driver.driver).mainloop()
