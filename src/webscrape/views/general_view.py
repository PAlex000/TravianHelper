from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from src.webscrape.building_names import building_names


class GeneralView:
    def __init__(self, driver):
        self._fields = []
        self._driver = driver
        self._wait = WebDriverWait(self._driver, 10)
        self._building_id = ""
        self._location = ""
        self._building_name = ""
        self._building_level = ""
        self.__building_web_element = ""
        self.__start_index = 0

    @property
    def fields(self):
        return self._fields

    @property
    def driver(self):
        return self._driver

    @property
    def building_id(self):
        return self._building_id

    @property
    def location(self):
        return self._location

    @property
    def building_name(self):
        return self._building_name

    @property
    def building_level(self):
        return self._building_level

    def _get_main_view(self, location_id, village_view: str):
        self._set_building_id(location_id, village_view)
        self._set_building_location()
        self._set_building_name()
        self._set_building_level()

    def _set_building_id(self, location_id, village_view):
        self._wait.until(EC.visibility_of_element_located((By.ID, village_view)))
        self.__set_web_element(location_id)
        self.__set_start_index("type_")
        if self.__does_building_exist():
            self._building_id = (
                "buildingId"
                + self.__building_web_element.get_attribute("innerHTML")[
                    self.__start_index
                    + len("type_") : self.__start_index
                    + len("type_")
                    + 2
                ]
            )
            self._building_id = self._building_id.rstrip()
        else:
            self._building_id = "free_slot"

    def __set_web_element(self, location_id):
        self.__building_web_element = self._driver.find_element(
            By.CLASS_NAME, "buildingLocation" + str(location_id)
        )

    def __set_start_index(self, string_to_search_for):
        self.__start_index = self.__building_web_element.get_attribute(
            "innerHTML"
        ).find(string_to_search_for)

    def __does_building_exist(self):
        return self.__start_index != -1

    def _set_building_location(self):
        self.__set_start_index("location_")
        if self.__does_building_exist():
            self._location = (
                "location"
                + self.__building_web_element.get_attribute("innerHTML")[
                    self.__start_index
                    + len("location_") : self.__start_index
                    + len("location_")
                    + 2
                ]
            )
        else:
            self._location = "free_slot"

    def _set_building_name(self):
        if self.__does_building_exist():
            self._building_name = building_names[self._building_id]
        else:
            self._building_name = "free_slot"

    def _set_building_level(self):
        if self.__does_building_exist():
            self._building_level = self.__building_web_element.find_element(
                By.CLASS_NAME, "buildingLevel"
            ).get_attribute("innerHTML")
        else:
            self._building_level = 0

    def _field_setter(self, building_id, location, building_name, building_type, level):
        self._fields.append(building_type(location, building_name, building_id, level))

    def _get_to_specific_view(self, view_name: str):
        self._wait.until(EC.element_to_be_clickable((By.CLASS_NAME, view_name))).click()
