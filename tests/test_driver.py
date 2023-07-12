from selenium import webdriver
from selenium.webdriver.edge.options import Options

from src.webscrape.driver import Driver


class TestDriver:
    def test_driver_with_default_values(self):
        test_driver = Driver()
        assert test_driver.driver == "" and test_driver.options == ""

    def test_driver_with_values(self):
        test_driver = Driver()
        test_options = Options()
        test_options.add_experimental_option("detach", True)
        test_options.add_experimental_option("excludeSwitches", ["enable-logging"])

        test_driver.configure_driver()

        assert (
            isinstance(test_driver.driver, webdriver.Edge)
            and test_driver.options.experimental_options
            == test_options.experimental_options
        )

        test_driver.driver.quit()
