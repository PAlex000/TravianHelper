from src.webscrape.buildings.building import Building


class Test_Building:
    def testWithValues(self):
        location = "location10"
        name = "testName"
        buildingId = "15"
        level = 10
        building = Building(location, name, buildingId, level)
        assert (
            building.location == location
            and building.name == name
            and building.buildingId == buildingId
            and building.level == level
        )

    def testBuildingStrMethod(self):
        location = "location10"
        name = "testName"
        buildingId = "15"
        level = 10
        building = Building(location, name, buildingId, level)
        assert (
            f"Building(name = {building.name}, location = {building.location}, buildingid = {building.buildingId}, level = {building.level})"
            == f"{building}"
        )
