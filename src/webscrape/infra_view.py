from src.webscrape.general_view import General_view
from src.webscrape.building import Infra_building
from src.webscrape.building_names import building_names
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class Infra_view(General_view):
    def __init__(self, driver):
        super().__init__(driver)

    # Infra starts from 19 until 40
    def get_all_buildings(self):
        self._get_to_specific_view("navi_village")
        for building_location in range(19,41):
            self._get_main_view(building_location, "villageView")
            self._field_setter(self._building_id, self._location , self._building_name, Infra_building, level = self._building_level)

    def __str__(self):
        temp = ""
        for i in self._fields:
            temp += str(i) + "\n"
        return temp
