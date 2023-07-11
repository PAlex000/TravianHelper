from webscrape.buildings.infra_building import InfraBuilding


class Test_InfraBuilding:
    def testInfraBuildingStrMethod(self):
        location = "location10"
        name = "testName"
        buildingId = "15"
        level = 10
        building = InfraBuilding(location, name, buildingId, level)
        assert (
            f"InfraBuilding(name = {building.name}, location = {building.location}, buildingId = {building.buildingId}, level = {building.level})"
            == f"{building}"
        )
