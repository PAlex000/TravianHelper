import json

from selenium import webdriver
from selenium.webdriver.edge.options import Options


class BaseTest:
    def _driver_setup(self):
        self._options = Options()
        self._options.add_experimental_option("detach", True)
        self._options.add_experimental_option("excludeSwitches", ["enable-logging"])
        self._driver = webdriver.Edge(options=self._options)

    def _driver_quit(self):
        self._driver.quit()

    def _set_credentials_from_json(self):
        with open("./credentials.json", "r", encoding="utf-8") as file:
            data = json.load(file)
            self._email = data["email"]
            self._password = data["password"]
