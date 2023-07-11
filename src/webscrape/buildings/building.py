class Building:
    def __init__(self, location, name, building_id, level):
        self.__location = location
        self.__name = name
        self.__building_id = building_id
        self.__level = level

    @property
    def location(self):
        return self.__location

    @property
    def name(self):
        return self.__name

    @property
    def building_id(self):
        return self.__building_id

    @property
    def level(self):
        return self.__level

    def __str__(self):
        return f"Building(name = {self.name}, location = {self.location}, \
buildingId = {self.building_id}, level = {self.level})"
