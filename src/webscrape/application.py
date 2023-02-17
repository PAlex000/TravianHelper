from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from src.gui.login_gui import Server_page
from src.messages.error_messages import *
from src.webscrape.infra_view import Infra_view
from src.webscrape.field_view import Field_view
from src.webscrape.login import Login
import time

class App:

    def __init__(self):
        self.__options = Options()
        self.__options.add_experimental_option('detach', True)
        self.__options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.__driver = webdriver.Edge(options=self.__options)
        self.__wait = WebDriverWait(self.__driver, 10)
        # A dict which has "server_name" : "its button reference" key-values
        self.__container = dict()
        # It's for checking if the selected world is first or not
        self.__first_world = True

    def login(self):
        Login(self.__driver, self.__wait).login()
    
    def __get_all_active_worlds(self):
        self.__wait.until(EC.visibility_of_element_located((By.TAG_NAME, "body")))
        self.__wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "game-world")))

        container_fluids = self.__driver.find_elements(By.CLASS_NAME, "game-world")
        
        for element in container_fluids:
            self.__driver.implicitly_wait(20)
            if element.find_element(By.CSS_SELECTOR, "div.default-button").find_element(By.TAG_NAME, "span").get_attribute('innerHTML') == "Continue playing":
                if len(container_fluids) > 1:
                    if self.__first_world:
                        world_name = element.find_element(By.CLASS_NAME, "game-world-name").find_element(By.TAG_NAME, "span").get_attribute("innerHTML")
                        world_name = world_name.split("-")[1].lstrip()
                        self.__first_world = False
                        self.__container[world_name] = element
                    else:
                        world_name = element.find_element(By.CLASS_NAME, "game-world-name").get_attribute("innerHTML")
                        self.__container[world_name] = element
                else:
                    world_name = element.find_element(By.CLASS_NAME, "game-world-name").find_element(By.TAG_NAME, "span").get_attribute("innerHTML")
                    world_name = world_name.split("-")[1].lstrip()
                    self.__container[world_name] = element
            
    def __set_selected_world(self):
        # server_gui returns server_name and server_element (self.__selected_world[0] and [1])
        self.__selected_world = Server_page("Server Page", self.__container).server_gui()

    def __login_to_the_selected_world(self):
        self.__wait.until(EC.element_to_be_clickable((self.__selected_world[1].find_element(By.CSS_SELECTOR, "div.default-button")))).click()
        # TODO: Try to fix this
        time.sleep(5)


    def server_chooser(self):
        self.__get_all_active_worlds()
        self.__set_selected_world()
        self.__login_to_the_selected_world()

    def get_infra_view(self):
        infra_view = Infra_view(self.__driver)
        infra_view.get_all_buildings()
        # print(f"{infra_view}")

    def get_field_view(self):
        field_view = Field_view(self.__driver)
        field_view.get_all_buildings()
        # print(f"{field_view}")