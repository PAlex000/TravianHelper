from src.webscrape.buildings.fieldBuilding import FieldBuilding


class Test_FieldBuilding:
    def testInfraBuildingStrMethod(self):
        location = "location10"
        name = "testName"
        buildingId = "15"
        level = 10
        building = FieldBuilding(location, name, buildingId, level)
        assert (
            f"FieldBuilding(name = {building.name}, location = {building.location}, buildingId = {building.buildingId}, level = {building.level})"
            == f"{building}"
        )
