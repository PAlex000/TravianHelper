from src.webscrape.views.villageView import Village
from src.gui.pages.loginPage import LoginPage
from src.webscrape.login import Login
from src.webscrape.serverSelection import ServerSelection
from src.webscrape.driver import Driver

class App:

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

        Login(loginCredentials[0], loginCredentials[1], loginCredentials[2], self.__configuredDriver.driver).login()

    def __serverSelection(self):
        selectedServer = ServerSelection(self.__configuredDriver.driver)
        selectedServer.serverSelect()

    def __getvillageView(self):
        village = Village(self.__configuredDriver.driver)
        village.getVillage()
