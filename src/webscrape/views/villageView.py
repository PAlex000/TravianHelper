from src.webscrape.views.fieldView import FieldView
from src.webscrape.views.infraView import InfraView


class Village():
    def __init__(self, driver):
        self.__driver = driver

    def getVillage(self):
        self.__getInfraView()
        self.__getFieldView()

    def __getInfraView(self):
        infraView = InfraView(self.__driver)
        infraView.getAllInfraBuildings()
        # print(f"{infraView}")

    def __getFieldView(self):
        fieldView = FieldView(self.__driver)
        fieldView.getAllFieldBuildings()
        # print(f"{fieldView}")
