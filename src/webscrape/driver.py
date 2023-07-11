from selenium import webdriver
from selenium.webdriver.edge.options import Options


class Driver:
    def __init__(self):
        self.__driver = ""
        self.__options = ""

    @property
    def driver(self):
        return self.__driver

    @property
    def options(self):
        return self.__options

    def configure_driver(self):
        self.__add_options()
        self.__set_driver()

    def __add_options(self):
        self.__options = Options()
        self.__options.add_experimental_option("detach", True)
        self.__options.add_experimental_option("excludeSwitches", ["enable-logging"])

    def __set_driver(self):
        self.__driver = webdriver.Edge(options=self.__options)
