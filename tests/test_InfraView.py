from src.webscrape.buildings.infraBuilding import InfraBuilding
from src.webscrape.login import Login
from src.webscrape.serverSelection import ServerSelection
from src.webscrape.views.infraView import InfraView
from tests import BaseTest


class Test_InfraView(BaseTest):
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

    def testGetAllFieldBuildings(self):
        self._driverSetUp()
        self._getCredentialsFromJSON()

        Login(self._email, self._password, 0, self._driver).login()
        ServerSelection(self._driver).serverSelect()

        testInfraView = InfraView(self._driver)
        testInfraView.getAllInfraBuildings()

        for field in testInfraView.fields:
            if field.name not in Test_InfraView.buildings.values():
                assert False
            if field.location != "free_slot":
                locationId = int(field.location[-2] + field.location[-1])
                if locationId < 18:
                    assert False

            if field.buildingId not in Test_InfraView.buildings.keys():
                assert False

            if int(field.level) > 20:
                assert False

        assert True

        self._driverQuit()

    def testInfraViewStrMethod(self):
        self._driverSetUp()
        testInfraView = InfraView(self._driver)
        testInfraView._fieldSetter(
            "buildingId5", "location19", "Sawmill", InfraBuilding, "1"
        )
        testInfraView._fieldSetter(
            "buildingId6", "location20", "Brickyard", InfraBuilding, "1"
        )
        testInfraView._fieldSetter(
            "buildingId7", "location21", "Iron Foundry", InfraBuilding, "1"
        )
        testInfraView._fieldSetter(
            "buildingId8", "location22", "Grain Mill", InfraBuilding, "1"
        )

        formattedOutput = ""
        for field in testInfraView.fields:
            formattedOutput += f"{field}\n"
        assert formattedOutput == f"{testInfraView}"

        self._driverQuit()
