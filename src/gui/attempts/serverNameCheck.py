from src.exceptions.serverNameError import ServerNameError


class ServerNameCheck:
    def __init__(self, serverName, serverElement):
        self.__serverName = serverName
        self.__serverElement = serverElement

    @property
    def serverName(self):
        return self.__serverName

    def getServerDetails(self):
        self.__serverNameCheck()

        return {"servername": self.__serverName, "serverelement": self.__serverElement}

    def __serverNameCheck(self):
        if self.__isServerNameEmpty():
            raise ServerNameError

    def __isServerNameEmpty(self):
        return len(self.__serverName) == 0
