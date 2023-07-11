from src.webscrape.buildings.building import Building


class FieldBuilding(Building):
    def __str__(self):
        return f"FieldBuilding(name = {self.name}, location = {self.location}, \
buildingId = {self.building_id}, level = {self.level})"
