import time
from src.webscrape.buildings.fieldBuilding import FieldBuilding
from src.webscrape.views.generalView import GeneralView

class FieldView(GeneralView):
    def __init__(self, driver):
        super().__init__(driver)

    # Resource starts from 1 until 18
    def getAllFieldBuildings(self):
        self._getToSpecificView("navi_resources")
        time.sleep(5)
        for buildingLocation in range(1,19):
            self._getMainView(buildingLocation, "villageViewRes")
            self._fieldSetter(self._buildingId, self._location , self._buildingName, FieldBuilding, self._buildingLevel)

    def __str__(self):
        temp = ""
        for i in self._fields:
            temp += str(i) + "\n"
        return temp
