from src.webscrape.buildings.building import Building


class TestBuilding:
    def test_with_values(self):
        location = "location10"
        name = "testName"
        building_id = "15"
        level = 10
        building = Building(location, name, building_id, level)
        assert (
            building.location == location
            and building.name == name
            and building.building_id == building_id
            and building.level == level
        )

    def test_building_str_method(self):
        location = "location10"
        name = "testName"
        building_id = "15"
        level = 10
        building = Building(location, name, building_id, level)
        assert (
            f"Building(name = {building.name}, location = {building.location}, \
buildingId = {building.building_id}, level = {building.level})"
            == f"{building}"
        )
