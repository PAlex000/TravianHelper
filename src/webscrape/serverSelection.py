import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from src.gui.pages.serverPage import ServerPage


class ServerSelection:
    def __init__(self, driver):
        self.__driver = driver
        self.__wait = WebDriverWait(self.__driver, 10)
        # A dict which has "server_name" : "its button reference" key-values
        self.__allServers = {}
        # It's for checking if the selected world is first or not
        self.__firstWorld = True
        self.__allActiveWorlds = ""
        self.__selectedWorld = ""

    def serverSelect(self):
        self.__getAllActiveWorlds()
        self.__setSelectedWorld()
        self.__loginToTheSelectedWorld()

    def __getAllActiveWorlds(self):
        time.sleep(3)
        self.__wait.until(EC.visibility_of_element_located((By.TAG_NAME, "body")))
        self.__wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "game-world"))
        )
        self.__allActiveWorlds = self.__driver.find_elements(
            By.CLASS_NAME, "game-world"
        )

        for element in self.__allActiveWorlds:
            self.__getWorld(element)

    def __getWorld(self, serverElement):
        self.__driver.implicitly_wait(20)
        if (
            serverElement.find_element(By.CSS_SELECTOR, "div.default-button")
            .find_element(By.TAG_NAME, "span")
            .get_attribute("innerHTML")
            == "Continue playing"
        ):
            if self.__IsServerCountMoreThanOne(self.__allActiveWorlds):
                if self.__firstWorld:
                    world_name = (
                        serverElement.find_element(By.CLASS_NAME, "game-world-name")
                        .find_element(By.TAG_NAME, "span")
                        .get_attribute("innerHTML")
                    )
                    world_name = world_name.split("-")[1].lstrip()
                    self.__firstWorld = False
                    self.__allServers[world_name] = serverElement
                else:
                    world_name = serverElement.find_element(
                        By.CLASS_NAME, "game-world-name"
                    ).get_attribute("innerHTML")
                    self.__allServers[world_name] = serverElement
            else:
                world_name = (
                    serverElement.find_element(By.CLASS_NAME, "game-world-name")
                    .find_element(By.TAG_NAME, "span")
                    .get_attribute("innerHTML")
                )
                world_name = world_name.split("-")[1].lstrip()
                self.__allServers[world_name] = serverElement

    def __IsServerCountMoreThanOne(self, servers):
        return len(servers) > 1

    def __setSelectedWorld(self):
        attempt = ServerPage(self.__allServers)
        attempt.createServerPage()
        self.__selectedWorld = attempt.serverDetails

    def __loginToTheSelectedWorld(self):
        self.__wait.until(
            EC.element_to_be_clickable(
                (
                    self.__selectedWorld["serverelement"].find_element(
                        By.CSS_SELECTOR, "div.default-button"
                    )
                )
            )
        ).click()
        time.sleep(5)
