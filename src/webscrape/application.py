from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from src.gui.pages.serverPage import ServerPage
from src.messages.errorMessages import *
from src.webscrape.views.infraView import InfraView
from src.webscrape.views.fieldView import FieldView
from src.gui.pages.loginPage import LoginPage
from src.webscrape.login import Login
import time

class App:

    def __init__(self):
        # A dict which has "server_name" : "its button reference" key-values
        self.__allServers = dict()
        # It's for checking if the selected world is first or not
        self.__firstWorld = True

    def run(self):
        options = Options()
        options.add_experimental_option('detach', True)
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.__driver = webdriver.Edge(options=options)
        self.__wait = WebDriverWait(self.__driver, 10)

    def login(self):
        attempt = LoginPage()
        attempt.createLoginPage()
        loginCredentials = attempt.loginCredentials
        Login(email=loginCredentials[0], password=loginCredentials[1], saveEmail=loginCredentials[2], driver=self.__driver).login()

    def serverChooser(self):
        self.__getAllActiveWorlds()
        self.__setSelectedWorld()
        self.__loginToTheSelectedWorld()

    def __getAllActiveWorlds(self):
        self.__wait.until(EC.visibility_of_element_located((By.TAG_NAME, "body")))
        self.__wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "game-world")))
        self.__allActiveWorlds = self.__driver.find_elements(By.CLASS_NAME, "game-world")

        for element in self.__allActiveWorlds:
            self.__getWorld(element)
    
    def __getWorld(self, serverElement):
            self.__driver.implicitly_wait(20)
            if serverElement.find_element(By.CSS_SELECTOR, "div.default-button").find_element(By.TAG_NAME, "span").get_attribute('innerHTML') == "Continue playing":
                if self.__IsServerCountMoreThanOne(self.__allActiveWorlds):
                    if self.__firstWorld:
                        world_name = serverElement.find_element(By.CLASS_NAME, "game-world-name").find_element(By.TAG_NAME, "span").get_attribute("innerHTML")
                        world_name = world_name.split("-")[1].lstrip()
                        self.__firstWorld = False
                        self.__allServers[world_name] = serverElement
                    else:
                        world_name = serverElement.find_element(By.CLASS_NAME, "game-world-name").get_attribute("innerHTML")
                        self.__allServers[world_name] = serverElement
                else:
                    world_name = serverElement.find_element(By.CLASS_NAME, "game-world-name").find_element(By.TAG_NAME, "span").get_attribute("innerHTML")
                    world_name = world_name.split("-")[1].lstrip()
                    self.__allServers[world_name] = serverElement

    def __IsServerCountMoreThanOne(self, servers):
        return True if len(servers) > 1 else False
    
    def __setSelectedWorld(self):
        attempt = ServerPage(self.__allServers)
        attempt.createServerPage()
        self.__selectedWorld = attempt.serverDetails
        
    def __loginToTheSelectedWorld(self):
        self.__wait.until(EC.element_to_be_clickable((self.__selectedWorld[1].find_element(By.CSS_SELECTOR, "div.default-button")))).click()
        # TODO: Try to fix this
        time.sleep(5)

    def getInfraView(self):
        infraView = InfraView(self.__driver)
        infraView.getAllBuildings()
        # print(f"{infra_view}")

    def getFieldView(self):
        fieldView = FieldView(self.__driver)
        fieldView.getAllBuildings()
        # print(f"{field_view}")
