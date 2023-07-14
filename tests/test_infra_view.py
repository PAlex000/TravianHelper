from src.webscrape.buildings.infra_building import InfraBuilding
from src.webscrape.login import Login
from src.webscrape.server_selection import ServerSelection
from src.webscrape.views.infra_view import InfraView
from tests import BaseTest


class TestInfraView(BaseTest):
    buildings = {
        "buildingId5": "Sawmill",
        "buildingId6": "Brickyard",
        "buildingId7": "Iron Foundry",
        "buildingId8": "Grain Mill",
        "buildingId9": "Bakery",
        "buildingId10": "Warehouse",
        "buildingId11": "Granary",
        "buildingId13": "Smithy",
        "buildingId14": "Tournament Square",
        "buildingId15": "Main Building",
        "buildingId16": "Rally Point",
        "buildingId17": "Marketplace",
        "buildingId18": "Embassy",
        "buildingId19": "Barracks",
        "buildingId20": "Stable",
        "buildingId21": "Workshop",
        "buildingId22": "Academy",
        "buildingId23": "Cranny",
        "buildingId24": "Town Hall",
        "buildingId25": "Residence",
        "buildingId26": "Palace",
        "buildingId27": "Unknown Building",
        "buildingId28": "Trade Office",
        "buildingId29": "Unknown Building",
        "buildingId30": "Unknown Building",
        "buildingId31": "City Wall",
        "buildingId33": "Palisade",
        "buildingId34": "Stonemason's Lodge",
        "buildingId36": "Trapper",
        "buildingId41": "Horse Drinking Trough",
        "buildingId45": "Hidden Treasury",
        "buildingId46": "Healing Tent",
        "free_slot": "free_slot",
    }

    def test_set_all_field_buildings(self):
        self._driver_setup()
        self._set_credentials_from_json()

        Login(self._email, self._password, 0, self._driver).login()
        ServerSelection(self._driver).server_select()

        test_infra_view = InfraView(self._driver)
        test_infra_view.set_all_infra_buildings()

        for field in test_infra_view.fields:
            if field.name not in TestInfraView.buildings.values():
                assert False
            if field.location != "free_slot":
                if field.location < 18:
                    assert False

            if field.building_id not in TestInfraView.buildings.keys():
                assert False

            if int(field.level) > 20:
                assert False

        assert True

        self._driver_quit()

    def test_infra_view_str_method(self):
        self._driver_setup()
        test_infra_view = InfraView(self._driver)
        test_infra_view._field_setter(
            "buildingId5", "location19", "Sawmill", InfraBuilding, "1"
        )
        test_infra_view._field_setter(
            "buildingId6", "location20", "Brickyard", InfraBuilding, "1"
        )
        test_infra_view._field_setter(
            "buildingId7", "location21", "Iron Foundry", InfraBuilding, "1"
        )
        test_infra_view._field_setter(
            "buildingId8", "location22", "Grain Mill", InfraBuilding, "1"
        )

        formatted_output = ""
        for field in test_infra_view.fields:
            formatted_output += f"{field}\n"
        assert formatted_output == f"{test_infra_view}"

        self._driver_quit()
