from src.webscrape.views.field_view import FieldView
from src.webscrape.views.infra_view import InfraView


class Village:
    def __init__(self, driver):
        self.__driver = driver

    # Set the current village details to the gui
    def set_village(self, canvas_and_ids):
        self.__set_field_view(
            canvas_and_ids["field_canvas"], canvas_and_ids["field_ids"]
        )
        self.__set_infra_view(
            canvas_and_ids["infra_canvas"], canvas_and_ids["infra_ids"]
        )

    def __set_field_view(self, canvas, ids):
        field_view = FieldView(self.__driver)
        field_view.set_all_field_buildings()
        field_view = field_view.get_fields()
        for building in field_view:
            ids[building.location].config(
                text=f"{building.building_name} : Level {building.level}"
            )

    def __set_infra_view(self, canvas, ids):
        infra_view = InfraView(self.__driver)
        infra_view.set_all_infra_buildings()
        infra_view = infra_view.get_fields()
        for building in infra_view:
            ids[building.location].config(
                text=f"{building.building_name} : Level {building.level}"
            )
