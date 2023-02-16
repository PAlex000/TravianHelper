class Building():
    def __init__(self, location, name, buildingid):
        self.__location = location
        self.__name = name
        self.__buildingid = buildingid
        
    @property
    def location(self):
        return self.__location
    
    @property
    def name(self):
        return self.__name
    
    @property
    def buildingid(self):
        return self.__buildingid

    def __str__ (self):
        return f"Building(name = {self.name}, location = {self.location}, buildingid = {self.buildingid})"
