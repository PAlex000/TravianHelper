from exceptions.serverNameError import ServerNameError

class ServerChooseAttempt():

    def __init__(self, serverName, serverElement):
        self.__serverName = serverName
        self.__serverElement = serverElement

    @property
    def email(self):
        return self.__email
    
    @property
    def password(self):
        return self.__password
    
    def getStatus(self):
        self.__serverNameCheck()

        return [self.__serverName, self.__serverElement]

    def __serverNameCheck(self):
        if self.__isServerNameEmpty():
            raise ServerNameError

    def __isServerNameEmpty(self):
        return True if len(self.__serverName) == 0 else False
    
