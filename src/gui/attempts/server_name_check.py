from src.exceptions.server_name_error import ServerNameError


class ServerNameCheck:
    def __init__(self, server_name, server_element):
        self.__server_name = server_name
        self.__server_element = server_element

    @property
    def server_name(self):
        return self.__server_name

    def get_server_details(self):
        self.__server_name_check()

        return {
            "servername": self.__server_name,
            "serverelement": self.__server_element,
        }

    def __server_name_check(self):
        if self.__is_server_name_empty():
            raise ServerNameError

    def __is_server_name_empty(self):
        return len(self.__server_name) == 0
