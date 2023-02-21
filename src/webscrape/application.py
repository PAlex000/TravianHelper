from selenium import webdriver
from selenium.webdriver.edge.options import Options
from src.messages.errorMessages import *
from src.webscrape.views.infraView import InfraView
from src.webscrape.views.fieldView import FieldView
from src.gui.pages.loginPage import LoginPage
from src.webscrape.login import Login
from src.webscrape.serverSelection import ServerSelection

class App:

    def run(self):
        self.__configureDriver()
        self.__login()
        self.__serverSelection()
        self.__getInfraView()
        self.__getFieldView()

    def __configureDriver(self):
        self.__addOptions()
        self.__setDriver()

    def __addOptions(self):
        self.__options = Options()
        self.__options.add_experimental_option('detach', True)
        self.__options.add_experimental_option('excludeSwitches', ['enable-logging'])

    def __setDriver(self):
        self.__driver = webdriver.Edge(options=self.__options)

    def __login(self):
        attempt = LoginPage()
        attempt.createLoginPage()
        loginCredentials = attempt.loginCredentials
        Login(loginCredentials[0], loginCredentials[1], loginCredentials[2], self.__driver).login()

    def __serverSelection(self):
        selectedServer = ServerSelection(self.__driver)
        selectedServer.serverSelect()

    def __getInfraView(self):
        infraView = InfraView(self.__driver)
        infraView.getAllBuildings()
        # print(f"{infra_view}")

    def __getFieldView(self):
        fieldView = FieldView(self.__driver)
        fieldView.getAllBuildings()
        # print(f"{field_view}")
