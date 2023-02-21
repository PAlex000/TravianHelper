from src.webscrape.buildings.infraBuilding import InfraBuilding
from src.webscrape.buildings.fieldBuilding import FieldBuilding
from src.webscrape.buildingNames import buildingNames
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class GeneralView():
    def __init__(self, driver):
        self._fields = []
        self._driver = driver
        self._wait = WebDriverWait(self._driver, 10)
        self._buildingId = ""
        self._location = ""
        self._buildingName = ""
        self._buildingLevel = ""

    @property
    def fields(self):
        return self._fields
    
    def _getMainView(self, id, villageview : str, infra=True):
        self._getBuildingId(id, villageview)
        self._getBuildingLocation()
        self._getBuildingName()
        self._getBuildingLevel()

    def _getBuildingId(self, locationId, villageView):
        # villageView for Infra, villageViewRes for resource
        self._wait.until(EC.visibility_of_element_located((By.ID, villageView)))
        self.__elementWithoutAttribute = self._driver.find_element(By.CLASS_NAME, "buildingLocation" + str(locationId))
        self.__element = self._driver.find_element(By.CLASS_NAME, "buildingLocation" + str(locationId)).get_attribute('innerHTML')
        startIndex = self.__element.find("type_")
        if startIndex == -1:
            self._buildingId = "free_slot"
        else:
            self._buildingId = "buildingId" + self.__element[startIndex + 5] + self.__element[startIndex + 6]
            self._buildingId = self._buildingId.rstrip()
        
    def _getBuildingLocation(self):
        startIndex = self.__element.find("location_")
        if startIndex == -1:
            self._location = "free_slot"
        else:
            self._location = "location" + self.__element[startIndex + 9] + self.__element[startIndex + 10]
        
    def _getBuildingName(self):
        if self._buildingId == "free_slot":
            self._buildingName = "free_slot"
        else:
            self._buildingName = buildingNames[self._buildingId]

    def _getBuildingLevel(self):
        if self._location == "free_slot":
            self._buildingLevel = 0
        else:
            self._buildingLevel = self.__elementWithoutAttribute.find_element(By.CLASS_NAME, "buildingLevel").get_attribute('innerHTML')
        
    def _fieldSetter(self, buildingid, location, name, buildingType : InfraBuilding | FieldBuilding, level=2):
        self._fields.append(buildingType(location, name, buildingid, level))

    def _getToSpecificView(self, view_name: str):
        self._wait.until(EC.element_to_be_clickable((By.CLASS_NAME, view_name))).click()
