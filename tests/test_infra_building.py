from src.webscrape.buildings.infra_building import InfraBuilding


class TestInfraBuilding:
    def test_infra_building_str_method(self):
        location = "location10"
        name = "testName"
        building_id = "15"
        level = 10
        building = InfraBuilding(location, name, building_id, level)
        assert (
            f"InfraBuilding(name = {building.name}, location = {building.location}, buildingId = {building.building_id}, level = {building.level})"
            == f"{building}"
        )
