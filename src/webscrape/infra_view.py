from src.webscrape.building import Building

# 21 field + 2 optional
class Infra_view():
    def __init__(self):
        self.__fields = []
        # Starts from 19

    def field_setter(self, buildingid, location, name = "Unknown"):
        self.__fields.append(Building(location, name, buildingid))
        # self.__fields.append({"BuildingID" : buildingid, "LocationID" : location, "Name" : name})

    @property
    def field(self):
        return self.__fields
    