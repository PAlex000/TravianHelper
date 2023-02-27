from selenium import webdriver

from src.webscrape.login import Login
from src.webscrape.serverSelection import ServerSelection
from src.webscrape.views.generalView import GeneralView
from tests import BaseTest


class Test_GeneralView(BaseTest):
    def testGeneralViewWithDefaultValues(self):
        self._driverSetUp()
        testGeneralView = GeneralView(self._driver)

        assert (
            not testGeneralView.fields
            and isinstance(testGeneralView.driver, webdriver.Edge)
            and testGeneralView.buildingId == ""
            and testGeneralView.location == ""
            and testGeneralView.buildingId == ""
            and testGeneralView.buildingLevel == ""
        )

        self._driverQuit()
