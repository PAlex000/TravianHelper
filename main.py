from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from gui import gui
from tkinter import messagebox
from error_messages import *


# Login gets the email and password using GUI.
# After the user pressed Login on GUI, the GUI automatically closes and the driver logs in.
def login(driver, email, password):
    # Accepting the cookies
    driver.find_element(By.ID, "cmpbntyestxt").click()
    # Clicking loginButton in the top-right corner to get the login iframe
    driver.find_element(By.ID, "loginButton").click()
    # wait.until(EC.frame_to_be_available_and_switch_to_it("easyXDM_default8613_provider"))
    driver.implicitly_wait(5)
    # Searching for the iframe which has "mellon-iframe" class attribute. Only 1 has it.
    driver.switch_to.frame(driver.find_element(By.CLASS_NAME, "mellon-iframe"))

    # Searching for the first iframe after switching to the mellon-iframe iframe.
    driver.switch_to.frame(driver.find_element(By.TAG_NAME, "iframe"))
    driver.implicitly_wait(2)

    email_field = driver.find_element(By.NAME, "email")
    password_field = driver.find_element(By.NAME, "password")

    # Setting the email and password from the GUI entries
    email_field.send_keys(email)
    password_field.send_keys(password)

    # Clicking the Log in button
    driver.implicitly_wait(2)
    driver.find_element(By.NAME, "submit").click()


def main():
    login_credentials = gui()
    if len(login_credentials) == 0:
        messagebox.showerror(LOGIN_ERROR_TITLE, LOGIN_ERROR_MSG)
        return
    options = Options()
    options.add_experimental_option('detach', True)
    driver = webdriver.Edge(options=options)
    driver.get("https://www.kingdoms.com/")
    # login_credentials[0] is email, login_credentials[1] is password
    login(driver, login_credentials[0], login_credentials[1])


if __name__ == '__main__':
    main()
