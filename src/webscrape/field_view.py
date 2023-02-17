import time
from src.webscrape.building import Field_building
from src.webscrape.general_view import General_view
from selenium.webdriver.support import expected_conditions as EC

# 21 field + 2 optional
class Field_view(General_view):
    def __init__(self, driver):
        super().__init__(driver)

    # Resource starts from 1 until 18
    def get_all_buildings(self):
        self._get_to_specific_view("navi_resources")
        time.sleep(5)
        for building_location in range(1,19):
            self._get_main_view(building_location, "villageViewRes")
            self._field_setter(self._building_id, self._location , self._building_name, Field_building, level = self._building_level)

    def __str__(self):
        temp = ""
        for i in self._fields:
            temp += str(i) + "\n"
        return temp