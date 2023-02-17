class Building():
    def __init__(self, location, name, buildingid, level):
        self.__location = location
        self.__name = name
        self.__buildingid = buildingid
        self.__level = level
        
    @property
    def location(self):
        return self.__location
    
    @property
    def name(self):
        return self.__name
    
    @property
    def buildingid(self):
        return self.__buildingid

    @property
    def level(self):
        return self.__level
    
    def __str__(self):
        return f"Building(name = {self.name}, location = {self.location}, buildingid = {self.buildingid}, level = {self.level})"

class Infra_building(Building):

    def __init__(self, location, name, buildingid, level):
        super().__init__(location, name, buildingid, level)

    def __str__(self):
        return f"Infra_building(name = {self.name}, location = {self.location}, buildingid = {self.buildingid}, level = {self.level})"
    
class Field_building(Building):

    def __init__(self, location, name, buildingid, level):
        super().__init__(location, name, buildingid, level)

    def __str__(self):
        return f"Field_building(name = {self.name}, location = {self.location}, buildingid = {self.buildingid}, level = {self.level})"
    