from src.webscrape.views.generalView import GeneralView
from src.webscrape.buildings.infraBuilding import InfraBuilding

class InfraView(GeneralView):
    def __init__(self, driver):
        super().__init__(driver)

    # Infra starts from 19 until 40
    def getAllInfraBuildings(self):
        self._getToSpecificView("navi_village")
        for buildingLocation in range(19,41):
            self._getMainView(buildingLocation, "villageView")
            self._fieldSetter(self._buildingId, self._location , self._buildingName, InfraBuilding, level = self._buildingLevel)

    def __str__(self):
        temp = ""
        for i in self._fields:
            temp += str(i) + "\n"
        return temp
