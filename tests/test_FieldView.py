from webscrape.buildings.field_building import FieldBuilding
from src.webscrape.login import Login
from webscrape.server_selection import ServerSelection
from webscrape.views.field_view import FieldView
from tests import BaseTest


class Test_FieldView(BaseTest):
    buildings = {
        "buildingId1": "Woodcutter",
        "buildingId2": "Clay Pit",
        "buildingId3": "Iron Mine",
        "buildingId4": "Cropland",
    }

    def testGetAllFieldBuildings(self):
        self._driverSetUp()
        self._getCredentialsFromJSON()

        Login(self._email, self._password, 0, self._driver).login()
        ServerSelection(self._driver).serverSelect()

        testFieldView = FieldView(self._driver)
        testFieldView.getAllFieldBuildings()

        for field in testFieldView.fields:
            if field.name not in Test_FieldView.buildings.values():
                assert False
            # It's a bug, will be fixed later, location gets location1", location2"... until 9, because then it gets location10
            if field.location[-1] != '"':
                locationId = int(field.location[-2] + field.location[-1])
                if locationId > 18:
                    assert False

            if field.buildingId not in Test_FieldView.buildings.keys():
                assert False

            if int(field.level) > 20:
                assert False

        assert len(testFieldView.fields) == 18

        self._driverQuit()

    def testInfraViewStrMethod(self):
        self._driverSetUp()
        testFieldView = FieldView(self._driver)
        testFieldView._fieldSetter(
            "buildingId1", "location1", "Woodcutter", FieldBuilding, "1"
        )
        testFieldView._fieldSetter(
            "buildingId1", "location2", "Woodcutter", FieldBuilding, "1"
        )
        testFieldView._fieldSetter(
            "buildingId1", "location3", "Woodcutter", FieldBuilding, "1"
        )
        testFieldView._fieldSetter(
            "buildingId1", "location4", "Woodcutter", FieldBuilding, "1"
        )

        formattedOutput = ""
        for field in testFieldView.fields:
            formattedOutput += f"{field}\n"
        assert formattedOutput == f"{testFieldView}"

        self._driverQuit()
