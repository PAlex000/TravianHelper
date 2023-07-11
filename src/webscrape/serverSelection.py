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
        self.__allActiveWorlds = ""
        self.__selectedWorld = ""
        self.__firstWorld = True

    def serverSelect(self):
        self.__setAllActiveWorlds()
        self.__setSelectedWorld()
        self.__loginToTheSelectedWorld()

    def __setAllActiveWorlds(self):
        time.sleep(3)
        self.__wait.until(EC.visibility_of_element_located((By.TAG_NAME, "body")))
        self.__wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "game-world"))
        )
        self.__allActiveWorlds = self.__driver.find_elements(
            By.CLASS_NAME, "game-world"
        )

        maxServerCount = self.__getActiveServerCount()

        for element in self.__allActiveWorlds:
            if maxServerCount == 0:
                break

            maxServerCount -= 1
            self.__setWorldDetails(element)

    def __getActiveServerCount(self):
        return len(self.__driver.find_elements(By.CLASS_NAME, "avatar-name"))

    def __setWorldDetails(self, serverElement):
        if self.__firstWorld:
            world_name = self.__getFirstWorldname(serverElement)
            world_name = world_name.split("-")[1].lstrip()
            world_name += self.__getAvatarName(serverElement)
            self.__firstWorld = False
            self.__allServers[world_name] = serverElement
        else:
            world_name = self.__getWorldName(serverElement)
            world_name += self.__getAvatarName(serverElement)
            self.__allServers[world_name] = serverElement

    def __getFirstWorldname(self, serverElement):
        return (
            serverElement.find_element(By.CLASS_NAME, "game-world-name")
            .find_element(By.TAG_NAME, "span")
            .get_attribute("innerHTML")
        )

    def __getAvatarName(self, serverElement):
        return " - " + serverElement.find_element(
            By.CLASS_NAME, "avatar-name"
        ).get_attribute("innerHTML")

    def __getWorldName(self, serverElement):
        return serverElement.find_element(
            By.CLASS_NAME, "game-world-name"
        ).get_attribute("innerHTML")

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
