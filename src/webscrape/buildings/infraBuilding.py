from src.webscrape.buildings.building import Building

class InfraBuilding(Building):

    def __init__(self, location, name, buildingId, level):
        super().__init__(location, name, buildingId, level)

    def __str__(self):
        return f"InfraBuilding(name = {self.name}, location = {self.location}, buildingId = {self.buildingId}, level = {self.level})"
