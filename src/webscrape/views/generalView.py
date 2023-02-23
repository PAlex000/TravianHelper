from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from src.webscrape.buildingNames import buildingNames


class GeneralView():
    def __init__(self, driver):
        self._fields = []
        self._driver = driver
        self._wait = WebDriverWait(self._driver, 10)
        self._buildingId = ""
        self._location = ""
        self._buildingName = ""
        self._buildingLevel = ""
        self.__buildingWebElement = ""
        self.__startIndex = 0

    @property
    def fields(self):
        return self._fields

    def _getMainView(self, locationId, villageview : str):
        self._getBuildingId(locationId, villageview)
        self._getBuildingLocation()
        self._getBuildingName()
        self._getBuildingLevel()

    def _getBuildingId(self, locationId, villageView):
        self._wait.until(EC.visibility_of_element_located((By.ID, villageView)))
        self.__getWebElement(locationId)
        self.__getStartIndex("type_")
        if self.__doesBuildingExist():
            self._buildingId = "buildingId" + self.__buildingWebElement \
            .get_attribute('innerHTML') \
            [self.__startIndex + len("type_") :self.__startIndex + len("type_") + 2]
            self._buildingId = self._buildingId.rstrip()
        else:
            self._buildingId = "free_slot"

    def __getWebElement(self, locationId):
        self.__buildingWebElement = self._driver \
        .find_element(By.CLASS_NAME, "buildingLocation" + str(locationId))

    def __getStartIndex(self, stringToSearchFor):
        self.__startIndex = self.__buildingWebElement \
        .get_attribute('innerHTML').find(stringToSearchFor)

    def __doesBuildingExist(self):
        return self.__startIndex != -1

    def _getBuildingLocation(self):
        self.__getStartIndex("location_")
        if self.__doesBuildingExist():
            self._location = "location" + self.__buildingWebElement \
            .get_attribute('innerHTML') \
            [self.__startIndex + len("location_"):self.__startIndex + len("location_") + 2]
        else:
            self._location = "free_slot"

    def _getBuildingName(self):
        if self.__doesBuildingExist():
            self._buildingName = buildingNames[self._buildingId]
        else:
            self._buildingName = "free_slot"

    def _getBuildingLevel(self):
        if self.__doesBuildingExist():
            self._buildingLevel = self.__buildingWebElement \
            .find_element(By.CLASS_NAME, "buildingLevel").get_attribute('innerHTML')
        else:
            self._buildingLevel = 0

    def _fieldSetter(self, buildingId, location, buildingName, buildingType, level):
        self._fields.append(buildingType(location, buildingName, buildingId, level))

    def _getToSpecificView(self, view_name: str):
        self._wait.until(EC.element_to_be_clickable((By.CLASS_NAME, view_name))).click()
