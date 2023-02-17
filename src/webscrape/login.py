from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from src.gui.login_gui import Login_page
from src.messages.error_messages import *
from tkinter import messagebox

class Login():
    def __init__(self, driver, wait):
        self.__driver = driver
        self.__wait = wait
        self.__email = ""
        self.__password = ""
        self.__pw_checkbox = 0

    def __get_login_credentials(self):
        # login_credentials[0] is email, login_credentials[1] is password, login_credentials[2] if user wants to save email for later
        login_credentials = Login_page("Login credentials").login_gui()
        if len(login_credentials) == 0:
            messagebox.showerror(LOGIN_ERROR_TITLE, LOGIN_ERROR_MSG)
            return
        self.__email = login_credentials[0]
        self.__password = login_credentials[1]
        self.__pw_checkbox = login_credentials[2]
        
    def __save_email(self):
        if self.__pw_checkbox:
            temp_dict = dict({
            "Email": self.__email,
            "Password": self.__password 
            })
            with open("login_credentials.json", "w") as file:
                for i in temp_dict:
                    file.write(i)

    def __pageload(self):
        self.__driver.get("https://www.kingdoms.com/")

    def __click_buttons(self):
        self.__wait.until(EC.element_to_be_clickable((By.ID, "cmpbntyestxt"))).click()
        self.__wait.until(EC.element_to_be_clickable((By.ID, "loginButton"))).click()

    def __iframes_switching(self):
        self.__wait.until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, "iframe.mellon-iframe")))
        self.__wait.until(EC.frame_to_be_available_and_switch_to_it((By.TAG_NAME, "iframe")))

    def __get_login_fields(self):
        self.__email_field = self.__wait.until(EC.visibility_of_element_located((By.NAME, "email")))
        self.__password_field = self.__wait.until(EC.visibility_of_element_located((By.NAME, "password")))
        
    def __set_login_fields(self, email, password):
        self.__email_field.send_keys(email)
        self.__password_field.send_keys(password)

    def __click_loginButton(self):
        self.__wait.until(EC.element_to_be_clickable((By.NAME, "submit"))).click()

    def __login_checking(self):
        try:
            self.__wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'game-world')))
        except:
            messagebox.showerror(FAILED_LOGIN_TITLE, FAILED_LOGIN_MSG)
            self.__driver.quit()
            return -1
        
    def login(self):
        self.__get_login_credentials()
        # self.__save_email()
        self.__pageload()
        self.__click_buttons()
        self.__iframes_switching()
        self.__get_login_fields()
        self.__set_login_fields(self.__email, self.__password)
        self.__click_loginButton()
        self.__login_checking()
