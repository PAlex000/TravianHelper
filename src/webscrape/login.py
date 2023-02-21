from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from src.messages.error_messages import *
from tkinter import messagebox
import re
from src.exceptions.EmailError import EmailError
from src.exceptions.PasswordError import PasswordError
from selenium.webdriver.support.wait import WebDriverWait

class Login():

    regexForEmail = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

    def __init__(self, email, password, saveEmail):
        self.__email = email
        self.__password = password
        self.__saveEmailBtn = saveEmail

    @property
    def email(self):
        return self.__email
    
    @property
    def password(self):
        return self.__password
    
    def getStatus(self):
        self.__emailCheck()
        self.__passwordCheck()
        return [self.__email, self.__password, self.__saveEmailBtn]

    def __emailCheck(self):
        if not self.__isEmailMatched():
            raise EmailError
    
    def __isEmailMatched(self):
        return True if re.fullmatch(Login.regexForEmail, self.__email) else False

    def __passwordCheck(self):
        if self.__isPasswordEmpty():
            raise PasswordError
    
    def __isPasswordEmpty(self):
        return True if len(self.__password) == 0 else False

    def login(self, driver):
        self.__driver = driver
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
            self.__driver.quit()
            return -1

    def __save_email(self):
        if self.__pw_checkbox:
            temp_dict = dict({
            "Email": self.__email,
            "Password": self.__password 
            })
            with open("login_credentials.json", "w") as file:
                for i in temp_dict:
                    file.write(i)
