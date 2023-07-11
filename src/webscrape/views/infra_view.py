from src.webscrape.buildings.infra_building import InfraBuilding
from src.webscrape.views.general_view import GeneralView


class InfraView(GeneralView):
    # Infra starts from 19 until 40
    def set_all_infra_buildings(self):
        self._get_to_specific_view("navi_village")
        for building_location in range(19, 41):
            self._get_main_view(building_location, "villageView")
            self._field_setter(
                self._building_id,
                self._location,
                self._building_name,
                InfraBuilding,
                level=self._building_level,
            )

    def __str__(self):
        temp = ""
        for i in self._fields:
            temp += str(i) + "\n"
        return temp
