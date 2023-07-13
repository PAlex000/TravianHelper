import time

from src.webscrape.buildings.field_building import FieldBuilding
from src.webscrape.views.general_view import GeneralView


class FieldView(GeneralView):
    def __init__(self, driver):
        super().__init__(driver)
        self.__set_all_field_buildings()

    # Resource starts from 1 until 18
    def __set_all_field_buildings(self):
        self._get_to_specific_view("navi_resources")
        time.sleep(5)
        for building_location in range(1, 19):
            self._get_main_view(building_location, "villageViewRes")
            self._field_setter(
                self._building_id,
                self._location,
                self._building_name,
                FieldBuilding,
                self._building_level,
            )

    def __str__(self):
        temp = ""
        for i in self._fields:
            temp += str(i) + "\n"
        return temp
