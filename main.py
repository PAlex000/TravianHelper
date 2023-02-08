from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options

def login(driver):
    # Clicking loginButton in the topright corner to get the login iframe
    driver.find_element(By.ID, "loginButton").click()
    # wait.until(EC.frame_to_be_available_and_switch_to_it("easyXDM_default8613_provider"))
    driver.implicitly_wait(5)
    # Searching for the iframe which has "mellon-iframe" class attribute. Only 1 has it.
    driver.switch_to.frame(driver.find_element(By.CLASS_NAME, "mellon-iframe"))

    # Searching for the first iframe after switching to the mellon-iframe iframe.
    driver.switch_to.frame(driver.find_element(By.TAG_NAME, "iframe"))
    email_field = driver.find_element(By.NAME, "email")
    password_field = driver.find_element(By.NAME, "password")
    # TODO: Make a Tkinter gui for this.
    email_field.send_keys("")
    password_field.send_keys("")


def main():
    options = Options()
    options.add_experimental_option('detach', True)
    driver = webdriver.Edge(options=options)
    driver.get("https://www.kingdoms.com/")
    login(driver)


if __name__ == '__main__':
    main()
