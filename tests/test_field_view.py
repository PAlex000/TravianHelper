from src.webscrape.buildings.field_building import FieldBuilding
from src.webscrape.login import Login
from src.webscrape.server_selection import ServerSelection
from src.webscrape.views.field_view import FieldView
from tests import BaseTest


class TestFieldView(BaseTest):
    buildings = {
        "buildingId1": "Woodcutter",
        "buildingId2": "Clay Pit",
        "buildingId3": "Iron Mine",
        "buildingId4": "Cropland",
    }

    def test_set_all_field_buildings(self):
        self._driver_setup()
        self._set_credentials_from_json()

        Login(self._email, self._password, 0, self._driver).login()
        ServerSelection(self._driver).server_select()

        test_field_view = FieldView(self._driver)
        test_field_view.set_all_field_buildings()

        for field in test_field_view.fields:
            if field.name not in TestFieldView.buildings.values():
                assert False
            # It's a bug, will be fixed later, location gets location1", location2"... until 9, because then it gets location10
            if field.location > 18:
                assert False

            if field.building_id not in TestFieldView.buildings.keys():
                assert False

            if int(field.level) > 20:
                assert False

        for i in test_field_view.fields:
            print(i)
        assert len(test_field_view.fields) == 18

        self._driver_quit()

    def test_field_view_str_method(self):
        self._driver_setup()
        test_field_view = FieldView(self._driver)
        test_field_view._field_setter(
            "buildingId1", "location1", "Woodcutter", FieldBuilding, "1"
        )
        test_field_view._field_setter(
            "buildingId1", "location2", "Woodcutter", FieldBuilding, "1"
        )
        test_field_view._field_setter(
            "buildingId1", "location3", "Woodcutter", FieldBuilding, "1"
        )
        test_field_view._field_setter(
            "buildingId1", "location4", "Woodcutter", FieldBuilding, "1"
        )

        formatted_output = ""
        for field in test_field_view.fields:
            formatted_output += f"{field}\n"
        assert formatted_output == f"{test_field_view}"

        self._driver_quit()
