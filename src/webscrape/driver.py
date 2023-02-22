from selenium import webdriver
from selenium.webdriver.edge.options import Options

class Driver():

    def __setDriver(self):
        self.__driver = webdriver.Edge(options=self.__options)

    def __addOptions(self):
        self.__options = Options()
        self.__options.add_experimental_option('detach', True)
        self.__options.add_experimental_option('excludeSwitches', ['enable-logging'])

    def configureDriver(self):
        self.__addOptions()
        self.__setDriver()

    @property
    def driver(self):
        return self.__driver
