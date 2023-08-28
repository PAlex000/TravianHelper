from src.webscrape.buildings.field_building import FieldBuilding


class TestFieldBuilding:
    def test_infra_building_str_method(self):
        location = "location10"
        name = "testName"
        building_id = "15"
        level = 10
        building = FieldBuilding(location, name, building_id, level)
        assert (
            f"FieldBuilding(name = {building.building_name}, location = {building.location}, \
buildingId = {building.building_id}, level = {building.level})"
            == f"{building}"
        )
