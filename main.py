from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from gui import *
from tkinter import messagebox
from error_messages import *
from selenium.webdriver.support import expected_conditions as EC

# It's for checking if the selected world is first or not
current_world = True

# A dict which has "server_name" : "its button reference" key-values
container = dict()


# Login gets the email and password using GUI.
# After the user pressed Login on GUI, the GUI automatically closes and the driver logs in.
def login(driver, email, password):
    wait = WebDriverWait(driver, 10)
    # Accept the cookies
    driver.find_element(By.ID, "cmpbntyestxt").click()
    # Click the loginButton in the top-right corner to get the login iframe
    driver.find_element(By.ID, "loginButton").click()
    # Search for the iframe which has "mellon-iframe" class attribute. Only 1 has it.
    wait.until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, "iframe.mellon-iframe")))

    # Search for the first iframe after switching to the mellon-iframe iframe.
    wait.until(EC.frame_to_be_available_and_switch_to_it((By.TAG_NAME, "iframe")))

    # Using element_to_be_clickable instead of implicit waiting.
    wait.until(EC.element_to_be_clickable((By.NAME, "email")))
    wait.until(EC.element_to_be_clickable((By.NAME, "password")))
    email_field = driver.find_element(By.NAME, "email")
    password_field = driver.find_element(By.NAME, "password")

    # Set the email and password from the GUI entries
    email_field.send_keys(email)
    password_field.send_keys(password)

    wait.until(EC.element_to_be_clickable((By.NAME, "submit"))).click()
    # Need to wait for page to be loaded
    try:
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'game-world')))
    except:
        messagebox.showerror(FAILED_LOGIN_TITLE, FAILED_LOGIN_MSG)
        driver.quit()
        return -1


def server_chooser(driver):
    wait = WebDriverWait(driver, 10)
    wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "game-world")))
    container_fluids = driver.find_elements(By.CLASS_NAME, "game-world")
    # TODO: Think a better way to get servers name.
    for element in container_fluids:
        if element\
                .find_element(By.CSS_SELECTOR, "div.default-button") \
                .find_element(By.TAG_NAME, "span") \
                .get_attribute('innerHTML') == "Continue playing":
            if len(container_fluids) > 1:
                global current_world
                if current_world:
                    world_name = element.find_element(By.CLASS_NAME, "game-world-name").find_element(By.TAG_NAME, "span").get_attribute("innerHTML")
                    world_name = world_name.split("-")[1].lstrip()
                    current_world = False
                    container[world_name] = element
                else:
                    world_name = element.find_element(By.CLASS_NAME, "game-world-name").get_attribute("innerHTML")
                    container[world_name] = element
            else:
                world_name = element.find_element(By.CLASS_NAME, "game-world-name").find_element(By.TAG_NAME, "span").get_attribute("innerHTML")
                world_name = world_name.split("-")[1].lstrip()
                container[world_name] = element

    # server_gui returns server_name and server_element (chosen_server[0] and [1]
    chosen_server = server_gui(container)

    # Clicks the correct login button
    chosen_server[1].find_element(By.CSS_SELECTOR, "div.default-button").click()


def main():
    login_credentials = login_gui()
    if len(login_credentials) == 0:
        messagebox.showerror(LOGIN_ERROR_TITLE, LOGIN_ERROR_MSG)
        return
    options = Options()
    options.add_experimental_option('detach', True)
    driver = webdriver.Edge(options=options)
    driver.get("https://www.kingdoms.com/")
    # login_credentials[0] is email, login_credentials[1] is password
    login(driver, login_credentials[0], login_credentials[1])
    server_chooser(driver)


if __name__ == '__main__':
    main()
