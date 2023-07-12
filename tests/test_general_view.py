from selenium import webdriver

from src.webscrape.views.general_view import GeneralView
from tests import BaseTest


class TestGeneralView(BaseTest):
    def test_general_view_with_default_values(self):
        self._driver_setup()
        test_general_view = GeneralView(self._driver)

        assert (
            not test_general_view.fields
            and isinstance(test_general_view.driver, webdriver.Edge)
            and test_general_view.building_id == ""
            and test_general_view.location == ""
            and test_general_view.building_name == ""
            and test_general_view.building_id == ""
            and test_general_view.building_level == ""
        )

        self._driver_quit()
