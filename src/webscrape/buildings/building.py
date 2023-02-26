class Building:
    def __init__(self, location, name, buildingId, level):
        self.__location = location
        self.__name = name
        self.__buildingId = buildingId
        self.__level = level

    @property
    def location(self):
        return self.__location

    @property
    def name(self):
        return self.__name

    @property
    def buildingId(self):
        return self.__buildingId

    @property
    def level(self):
        return self.__level

    def __str__(self):
        return f"Building(name = {self.name}, location = {self.location}, \
    buildingid = {self.buildingId}, level = {self.level})"
