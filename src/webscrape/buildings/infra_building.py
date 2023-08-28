from src.webscrape.buildings.building import Building


class InfraBuilding(Building):
    def __str__(self):
        return f"InfraBuilding(name = {self.building_name}, location = {self.location}, \
buildingId = {self.building_id}, level = {self.level})"
