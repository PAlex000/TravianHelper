from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from gui import *
from tkinter import messagebox
from error_messages import *
from selenium.webdriver.support import expected_conditions as EC

class App():

    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.options = Options()
        self.options.add_experimental_option('detach', True)
        self.options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.driver = webdriver.Edge(options=self.options)
        self.wait = WebDriverWait(self.driver, 10)
        # A dict which has "server_name" : "its button reference" key-values
        self.container = dict()
        # It's for checking if the selected world is first or not
        self.current_world = True

    # Login gets the email and password using GUI.
    # After the user pressed Login on GUI, the GUI automatically closes and the driver logs in.
        
    def login(self):
        self.driver.get("https://www.kingdoms.com/")
        self.wait.until(EC.element_to_be_clickable((By.ID, "cmpbntyestxt")))
        # Accept the cookies
        self.driver.find_element(By.ID, "cmpbntyestxt").click()
        # Click the loginButton in the top-right corner to get the login iframe
        self.driver.find_element(By.ID, "loginButton").click()
        # Search for the iframe which has "mellon-iframe" class attribute. Only 1 has it.
        self.wait.until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, "iframe.mellon-iframe")))

        # Search for the first iframe after switching to the mellon-iframe iframe.
        self.wait.until(EC.frame_to_be_available_and_switch_to_it((By.TAG_NAME, "iframe")))

        # Using element_to_be_clickable instead of implicit waiting.
        self.wait.until(EC.element_to_be_clickable((By.NAME, "email")))
        self.wait.until(EC.element_to_be_clickable((By.NAME, "password")))
        email_field = self.driver.find_element(By.NAME, "email")
        password_field = self.driver.find_element(By.NAME, "password")

        # Set the email and password from the GUI entries
        email_field.send_keys(self.email)
        password_field.send_keys(self.password)

        self.wait.until(EC.element_to_be_clickable((By.NAME, "submit"))).click()
        # Need to wait for page to be loaded
        try:
            self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'game-world')))
        except:
            messagebox.showerror(FAILED_LOGIN_TITLE, FAILED_LOGIN_MSG)
            self.driver.quit()
            return -1


    def server_chooser(self):
        self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "game-world")))
        container_fluids = self.driver.find_elements(By.CLASS_NAME, "game-world")
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.default-button")))
        # TODO: Think a better way to get servers name.
        for element in container_fluids:
            if element\
                    .find_element(By.CSS_SELECTOR, "div.default-button") \
                    .find_element(By.TAG_NAME, "span") \
                    .get_attribute('innerHTML') == "Continue playing":
                if len(container_fluids) > 1:
                    if self.current_world:
                        world_name = element.find_element(By.CLASS_NAME, "game-world-name").find_element(By.TAG_NAME, "span").get_attribute("innerHTML")
                        world_name = world_name.split("-")[1].lstrip()
                        self.current_world = False
                        self.container[world_name] = element
                    else:
                        world_name = element.find_element(By.CLASS_NAME, "game-world-name").get_attribute("innerHTML")
                        self.container[world_name] = element
                else:
                    world_name = element.find_element(By.CLASS_NAME, "game-world-name").find_element(By.TAG_NAME, "span").get_attribute("innerHTML")
                    world_name = world_name.split("-")[1].lstrip()
                    self.container[world_name] = element

        # server_gui returns server_name and server_element (chosen_server[0] and [1]
        chosen_server = server_gui(self.container)

        # Clicks the correct login button
        chosen_server[1].find_element(By.CSS_SELECTOR, "div.default-button").click()


def main():
    login_credentials = login_gui()
    if len(login_credentials) == 0:
        messagebox.showerror(LOGIN_ERROR_TITLE, LOGIN_ERROR_MSG)
        return
    # login_credentials[0] is email, login_credentials[1] is password
    travian_helper = App(login_credentials[0], login_credentials[1])
    travian_helper.login()
    travian_helper.server_chooser()


if __name__ == '__main__':
    main()
