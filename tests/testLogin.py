import unittest
from selenium import webdriver
from selenium.webdriver.edge.options import Options
from src.webscrape.login import Login
import json

class TestLogin(unittest.TestCase):

    def setUp(self):
        self.__readCredentialsFromJSON()
        self.__options = Options()
        self.__options.add_experimental_option('detach', True)
        self.__options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.__driver = webdriver.Edge(options=self.__options)
        
    def __readCredentialsFromJSON(self):
        with open('./credentials.json', 'r') as f:
            data = json.load(f)
            self.__email = data["email"]
            self.__password = data["password"]
    
    def testLoginWithCorrectCredentials(self):
        saveEmail = 0
        self.login = Login(self.__email, self.__password, saveEmail, self.__driver)
        self.login.login()
        self.assertEqual(self.__driver.current_url, "https://lobby.kingdoms.com/#/")

    def testLoginWithIncorrectCredentials(self):
        email = "definitelyAgoodEmail@gmail.com"
        password = "1234"
        saveEmail = 0
        self.login = Login(email, password, saveEmail, self.__driver)
        with self.assertRaises(SystemExit) as cm:
            self.login.login()
            self.assertEqual(cm.exception.code, 1)
    
    def tearDown(self):
        self.__driver.quit()

if __name__ == '__main__':
    unittest.main()
