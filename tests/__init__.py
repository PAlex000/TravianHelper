import json

from selenium import webdriver
from selenium.webdriver.edge.options import Options


class BaseTest:
    def _driverSetUp(self):
        self._options = Options()
        self._options.add_experimental_option("detach", True)
        self._options.add_experimental_option("excludeSwitches", ["enable-logging"])
        self._driver = webdriver.Edge(options=self._options)

    def _driverQuit(self):
        self._driver.quit()

    def _getCredentialsFromJSON(self):
        with open("./credentials.json", "r") as f:
            data = json.load(f)
            self._email = data["email"]
            self._password = data["password"]
