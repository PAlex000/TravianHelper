from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from src.gui.login_gui import Login_page, Server_page
from src.messages.error_messages import *
from src.webscrape.infra_view import Infra_view
from src.webscrape.field_view import Field_view
import time
from tkinter import messagebox

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

    def __get_login_credentials(self):
        # login_credentials[0] is email, login_credentials[1] is password
        login_credentials = Login_page("Login credentials").login_gui()
        if len(login_credentials) == 0:
            messagebox.showerror(LOGIN_ERROR_TITLE, LOGIN_ERROR_MSG)
            return
        self.__email = login_credentials[0]
        self.__password = login_credentials[1]
        
    def __pageload(self):
        self.__driver.get("https://www.kingdoms.com/")

    def __click_buttons(self):
        self.__wait.until(EC.element_to_be_clickable((By.ID, "cmpbntyestxt"))).click()
        self.__wait.until(EC.element_to_be_clickable((By.ID, "loginButton"))).click()

    def __iframes_switching(self):
        self.__wait.until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, "iframe.mellon-iframe")))
        self.__wait.until(EC.frame_to_be_available_and_switch_to_it((By.TAG_NAME, "iframe")))

    def __get_login_fields(self):
        self.__email_field = self.__wait.until(EC.visibility_of_element_located((By.NAME, "email")))
        self.__password_field = self.__wait.until(EC.visibility_of_element_located((By.NAME, "password")))
        
    def __set_login_fields(self, email, password):
        self.__email_field.send_keys(email)
        self.__password_field.send_keys(password)

    def __click_loginButton(self):
        self.__wait.until(EC.element_to_be_clickable((By.NAME, "submit"))).click()

    def __login_checking(self):
        try:
            self.__wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'game-world')))
        except:
            messagebox.showerror(FAILED_LOGIN_TITLE, FAILED_LOGIN_MSG)
            self.__driver.quit()
            return -1

    def login(self):
        self.__get_login_credentials()
        self.__pageload()
        self.__click_buttons()
        self.__iframes_switching()
        self.__get_login_fields()
        self.__set_login_fields(self.__email, self.__password)
        self.__click_loginButton()
        self.__login_checking()

    def __get_all_active_worlds(self):
        self.__wait.until(EC.visibility_of_element_located((By.TAG_NAME, "body")))
        self.__wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "game-world")))

        container_fluids = self.__driver.find_elements(By.CLASS_NAME, "game-world")
        # TODO: Think a better way to get server names.
        time.sleep(5)
        for element in container_fluids:
            if element\
                    .find_element(By.CSS_SELECTOR, "div.default-button") \
                    .find_element(By.TAG_NAME, "span") \
                    .get_attribute('innerHTML') == "Continue playing":
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