from src.webscrape.building import Infra_building, Field_building
from src.webscrape.building_names import building_names
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class General_view():
    def __init__(self, driver):
        self._fields = []
        self._driver = driver
        self._wait = WebDriverWait(self._driver, 10)
        self._building_id = ""
        self._location = ""
        self._building_name = ""
        self._building_level = ""

    @property
    def fields(self):
        return self._fields
    
    def _get_building_id(self, locationId, villageview):
        # villageView for Infra, villageViewRes for resource
        self._wait.until(EC.visibility_of_element_located((By.ID, villageview)))
        self.__element_without_attribute = self._driver.find_element(By.CLASS_NAME, "buildingLocation" + str(locationId))
        self.__element = self._driver.find_element(By.CLASS_NAME, "buildingLocation" + str(locationId)).get_attribute('innerHTML')
        start_index = self.__element.find("type_")
        if start_index == -1:
            self._building_id = "free_slot"
        else:
            self._building_id = "buildingId" + self.__element[start_index + 5] + self.__element[start_index + 6]
            self._building_id = self._building_id.rstrip()
        
    def _get_building_location(self):
        start_index = self.__element.find("location_")
        if start_index == -1:
            self._location = "free_slot"
        else:
            self._location = "location" + self.__element[start_index + 9] + self.__element[start_index + 10]
        
    def _get_building_name(self):
        if self._building_id == "free_slot":
            self._building_name = "free_slot"
        else:
            self._building_name = building_names[self._building_id]

    def _get_building_level(self):
        if self._location == "free_slot":
            self._building_level = 0
        else:
            self._building_level = self.__element_without_attribute.find_element(By.CLASS_NAME, "buildingLevel").get_attribute('innerHTML')

    def _get_main_view(self, id, villageview : str, infra=True):
        self._get_building_id(id, villageview)
        self._get_building_location()
        self._get_building_name()
        self._get_building_level()
        
    def _field_setter(self, buildingid, location, name, building_type : Infra_building | Field_building, level=2):
        self._fields.append(building_type(location, name, buildingid, level))

    def _get_to_specific_view(self, view_name: str):
        self._wait.until(EC.element_to_be_clickable((By.CLASS_NAME, view_name))).click()
