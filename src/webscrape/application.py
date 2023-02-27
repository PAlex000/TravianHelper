from src.gui.pages.loginPage import LoginPage
from src.webscrape.driver import Driver
from src.webscrape.login import Login
from src.webscrape.serverSelection import ServerSelection
from src.webscrape.views.villageView import Village


class App:
    def __init__(self):
        self.__configuredDriver = ""

    def run(self):
        self.__configureDriver()
        self.__login()
        self.__serverSelection()
        self.__getvillageView()

    def __configureDriver(self):
        self.__configuredDriver = Driver()
        self.__configuredDriver.configureDriver()

    def __login(self):
        attempt = LoginPage()
        attempt.createLoginPage()
        loginCredentials = attempt.loginCredentials

        Login(
            loginCredentials["email"],
            loginCredentials["password"],
            loginCredentials["saveEmail"],
            self.__configuredDriver.driver,
        ).login()

    def __serverSelection(self):
        selectedServer = ServerSelection(self.__configuredDriver.driver)
        selectedServer.serverSelect()

    def __getvillageView(self):
        village = Village(self.__configuredDriver.driver)
        village.getVillage()
