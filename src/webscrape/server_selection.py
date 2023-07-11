import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from src.gui.pages.server_page import ServerPage


class ServerSelection:
    def __init__(self, driver):
        self.__driver = driver
        self.__wait = WebDriverWait(self.__driver, 10)
        # A dict which has "server_name" : "its button reference" key-values
        self.__all_servers = {}
        self.__all_active_worlds = ""
        self.__selected_world = ""
        self.__first_world = True

    def server_select(self):
        self.__set_all_active_worlds()
        self.__set_selected_world()
        self.__login_to_the_selected_world()

    def __set_all_active_worlds(self):
        time.sleep(3)
        self.__wait.until(EC.visibility_of_element_located((By.TAG_NAME, "body")))
        self.__wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "game-world"))
        )
        self.__all_active_worlds = self.__driver.find_elements(
            By.CLASS_NAME, "game-world"
        )

        max_server_count = self.__get_active_server_count()

        for element in self.__all_active_worlds:
            if max_server_count == 0:
                break

            max_server_count -= 1
            self.__set_world_details(element)

    def __get_active_server_count(self):
        return len(self.__driver.find_elements(By.CLASS_NAME, "avatar-name"))

    def __set_world_details(self, server_element):
        if self.__first_world:
            world_name = self.__get_first_world_name(server_element)
            world_name = world_name.split("-")[1].lstrip()
            world_name += self.__get_avatar_name(server_element)
            self.__first_world = False
            self.__all_servers[world_name] = server_element
        else:
            world_name = self.__get_world_name(server_element)
            world_name += self.__get_avatar_name(server_element)
            self.__all_servers[world_name] = server_element

    def __get_first_world_name(self, server_element):
        return (
            server_element.find_element(By.CLASS_NAME, "game-world-name")
            .find_element(By.TAG_NAME, "span")
            .get_attribute("innerHTML")
        )

    def __get_avatar_name(self, server_element):
        return " - " + server_element.find_element(
            By.CLASS_NAME, "avatar-name"
        ).get_attribute("innerHTML")

    def __get_world_name(self, server_element):
        return server_element.find_element(
            By.CLASS_NAME, "game-world-name"
        ).get_attribute("innerHTML")

    def __set_selected_world(self):
        attempt = ServerPage(self.__all_servers)
        attempt.create_server_page()
        self.__selected_world = attempt.server_details

    def __login_to_the_selected_world(self):
        self.__wait.until(
            EC.element_to_be_clickable(
                (
                    self.__selected_world["serverelement"].find_element(
                        By.CSS_SELECTOR, "div.default-button"
                    )
                )
            )
        ).click()
        time.sleep(5)
