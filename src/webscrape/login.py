import sys
from tkinter import messagebox

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from src.messages.error_messages import FAILED_LOGIN_MSG, FAILED_LOGIN_TITLE


class Login:
    def __init__(self, email, password, save_email, driver):
        self.__email = email
        self.__password = password
        self.__save_email_btn = save_email
        self.__driver = driver
        self.__wait = WebDriverWait(self.__driver, 10)
        self.__email_field = ""
        self.__password_field = ""

    @property
    def email(self):
        return self.__email

    @property
    def password(self):
        return self.__password

    def login(self):
        # self.__save_email()
        self.__load_page()
        self.__click_cookie_and_login_buttons()
        self.__switch_iframes()
        self.__set_login_fields()
        self.__set_login_credentials()
        self.__click_login()
        self.__check_login()

    def __load_page(self):
        self.__driver.get("https://www.kingdoms.com/")

    def __click_cookie_and_login_buttons(self):
        self.__wait.until(EC.element_to_be_clickable((By.ID, "cmpbntyestxt"))).click()
        self.__wait.until(EC.element_to_be_clickable((By.ID, "loginButton"))).click()

    def __switch_iframes(self):
        self.__wait.until(
            EC.frame_to_be_available_and_switch_to_it(
                (By.CSS_SELECTOR, "iframe.mellon-iframe")
            )
        )
        self.__wait.until(
            EC.frame_to_be_available_and_switch_to_it((By.TAG_NAME, "iframe"))
        )

    def __set_login_fields(self):
        self.__email_field = self.__wait.until(
            EC.visibility_of_element_located((By.NAME, "email"))
        )
        self.__password_field = self.__wait.until(
            EC.visibility_of_element_located((By.NAME, "password"))
        )

    def __set_login_credentials(self):
        self.__email_field.send_keys(self.__email)
        self.__password_field.send_keys(self.__password)

    def __click_login(self):
        button = self.__wait.until(EC.element_to_be_clickable((By.NAME, "submit")))
        button.click()

    def __check_login(self):
        try:
            self.__wait.until(
                EC.visibility_of_element_located((By.CLASS_NAME, "game-world"))
            )
        except TimeoutException:
            messagebox.showerror(FAILED_LOGIN_TITLE, FAILED_LOGIN_MSG)
            sys.exit()
