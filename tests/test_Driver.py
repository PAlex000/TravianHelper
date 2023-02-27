from selenium import webdriver
from selenium.webdriver.edge.options import Options

from src.webscrape.driver import Driver


class Test_Driver:
    def testDriverWithDefaultValues(self):
        testDriver = Driver()
        assert testDriver.driver == "" and testDriver.options == ""

    def testDriverWithValues(self):
        testDriver = Driver()
        testOptions = Options()
        testOptions.add_experimental_option("detach", True)
        testOptions.add_experimental_option("excludeSwitches", ["enable-logging"])

        testDriver.configureDriver()

        assert (
            isinstance(testDriver.driver, webdriver.Edge)
            and testDriver.options.experimental_options
            == testOptions.experimental_options
        )

        testDriver.driver.quit()
