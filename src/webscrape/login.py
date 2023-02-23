from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from src.messages.errorMessages import *
from tkinter import messagebox
from selenium.webdriver.support.wait import WebDriverWait
import sys

class Login():

    regexForEmail = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

    def __init__(self, email, password, saveEmail, driver):
        self.__email = email
        self.__password = password
        self.__saveEmailBtn = saveEmail
        self.__driver = driver

    @property
    def email(self):
        return self.__email
    
    @property
    def password(self):
        return self.__password
    
    def login(self):
        self.__wait = WebDriverWait(self.__driver, 10)
        # self.__save_email()
        self.__loadPage()
        self.__clickCookieAndLoginButtons()
        self.__switchIframes()
        self.__getLoginFields()
        self.__setLoginCredentials()
        self.__clickLogin()
        self.__checkLogin()
        

    def __loadPage(self):
        self.__driver.get("https://www.kingdoms.com/")

    def __clickCookieAndLoginButtons(self):
        self.__wait.until(EC.element_to_be_clickable((By.ID, "cmpbntyestxt"))).click()
        self.__wait.until(EC.element_to_be_clickable((By.ID, "loginButton"))).click()

    def __switchIframes(self):
        self.__wait.until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, "iframe.mellon-iframe")))
        self.__wait.until(EC.frame_to_be_available_and_switch_to_it((By.TAG_NAME, "iframe")))

    def __getLoginFields(self):
        self.__email_field = self.__wait.until(EC.visibility_of_element_located((By.NAME, "email")))
        self.__password_field = self.__wait.until(EC.visibility_of_element_located((By.NAME, "password")))
        
    def __setLoginCredentials(self):
        self.__email_field.send_keys(self.__email)
        self.__password_field.send_keys(self.__password)

    def __clickLogin(self):
        button = self.__wait.until(EC.element_to_be_clickable((By.NAME, "submit")))
        button.click()

    def __checkLogin(self):
        try:
            self.__wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'game-world')))
        except:
            messagebox.showerror(FAILED_LOGIN_TITLE, FAILED_LOGIN_MSG)
            sys.exit()
