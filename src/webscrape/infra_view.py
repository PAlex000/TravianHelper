from src.webscrape.building import Building
from src.webscrape.building_names import building_names
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class Infra_view():
    def __init__(self, driver):
        self.__fields = []
        self.__driver = driver
        self.__wait = WebDriverWait(self.__driver, 10)
        self.__building_id = ""
        self.__location = ""
        self.__building_name = ""

    @property
    def fields(self):
        return self.__fields

    def __get_building_id(self, locationId):
        self.__wait.until(EC.visibility_of_element_located((By.ID, "villageView")))
        self.__element = self.__driver.find_element(By.CLASS_NAME, "buildingLocation" + str(locationId)).get_attribute('innerHTML')
        start_index = self.__element.find("buildingId")
        if start_index == -1:
            self.__building_id = "free_slot"
        else:
            self.__building_id = "buildingId" + self.__element[start_index + 10] + self.__element[start_index + 11]
        
    def __get_building_location(self):
        start_index = self.__element.find("location_")
        if start_index == -1:
            self.__location = "free_slot"
        else:
            self.__location = "location" + self.__element[start_index + 9] + self.__element[start_index + 10]

    def __get_building_name(self):
        if self.__building_id == "free_slot":
            self.__building_name = "free_slot"
        else:
            self.__building_name = building_names[self.__building_id]

    def __get_main_view(self, id):
        self.__get_building_id(id)
        self.__get_building_location()
        self.__get_building_name()
        
    def __field_setter(self, buildingid, location, name):
        self.__fields.append(Building(location, name, buildingid))

    # Infra starts from 18 until 40
    def get_all_buildings(self):
        for building_location in range(18,41):
            self.__get_main_view(building_location)
            self.__field_setter(self.__building_id, self.__location , self.__building_name)

