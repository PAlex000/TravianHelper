from src.webscrape.views.field_view import FieldView
from src.webscrape.views.infra_view import InfraView


class Village:
    def __init__(self, driver):
        self.__driver = driver

    def set_village(self):
        self.__set_infra_view()
        self.__set_field_view()

    def __set_infra_view(self):
        infra_view = InfraView(self.__driver)
        infra_view.set_all_infra_buildings()
        # print(f"{infraView}")

    def __set_field_view(self):
        field_view = FieldView(self.__driver)
        field_view.set_all_field_buildings()
        # print(f"{fieldView}")
