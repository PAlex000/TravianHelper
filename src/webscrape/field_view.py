# 21 field + 2 optional
class Field_view():
    def __init__(self):
        self.__fields = []
        # Starts from 0
        i = 1
        while i < 21:
            my_dict = {"Name" : i, "Location" : 2}
            self.__fields.append(my_dict)
            i += 1

    @property
    def fields(self):
        return self.__fields
