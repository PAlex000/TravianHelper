import pytest
from selenium import webdriver
from selenium.webdriver.edge.options import Options
from src.webscrape.login import Login
import json

class Test_Login():
    
    def testLoginWithCorrectCredentials(self):
        self.driverSetUp()
        self.getCredentials()
        saveEmail = 0
        self.login = Login(self.__email, self.__password, saveEmail, self.__driver)
        self.login.login()
        assert self.__driver.current_url == "https://lobby.kingdoms.com/#/"
        self.driverQuit()

    def driverSetUp(self):
        self.__options = Options()
        self.__options.add_experimental_option('detach', True)
        self.__options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.__driver = webdriver.Edge(options=self.__options)
        
    def getCredentials(self):
        self.readCredentialsFromJSON()

    def readCredentialsFromJSON(self):
        with open('./credentials.json', 'r') as f:
            data = json.load(f)
            self.__email = data["email"]
            self.__password = data["password"]
            
    def driverQuit(self):
        self.__driver.quit()

    def testLoginWithIncorrectCredentials(self):
        self.driverSetUp()
        email = "definitelyAgoodEmail@gmail.com"
        password = "1234"
        saveEmail = 0
        self.login = Login(email, password, saveEmail, self.__driver)
        with pytest.raises(SystemExit):
            self.login.login()
        self.driverQuit()
