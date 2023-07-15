from tkinter import END, Button, Checkbutton, Entry, IntVar

from src.gui.pages.default_page import DefaultPage
from src.webscrape.login import Login


class LoginPage(DefaultPage):
    def __init__(self, driver="", title="Login Credentials"):
        super().__init__(title)
        self.__login_credentials = {"email": "", "password": "", "saveEmail": ""}
        self.__email_entry = Entry()
        self.__password_entry = Entry()
        self.__login_button = Button()
        self.__email_remember_button = IntVar()
        self.__driver = driver

    @property
    def login_credentials(self):
        return self.__login_credentials

    @property
    def email_entry(self):
        return self.__email_entry

    @email_entry.setter
    def email_entry(self, value):
        self.__email_entry.delete(0, END)
        self.__email_entry.insert(0, value)

    @property
    def password_entry(self):
        return self.__password_entry

    @password_entry.setter
    def password_entry(self, value):
        self.__password_entry.delete(0, END)
        self.__password_entry.insert(0, value)

    @property
    def login_button(self):
        return self.__login_button

    @property
    def email_remember_button(self):
        return self.__email_remember_button

    @email_remember_button.setter
    def email_remember_button(self, value):
        self.__email_remember_button.set(value)

    def create_login_page(self):
        self.__create_entries()
        self.__create_buttons()

    def __create_entries(self):
        email, password = Login.get_credentials_from_json("credentials.json").values()
        self.__email_entry = Entry(self.frame)
        self.__email_entry.insert(0, email)
        self.__email_entry.pack(**self.properties)
        self.__password_entry = Entry(self.frame)
        self.__password_entry.config(show="*")
        self.__password_entry.insert(0, password)
        self.__password_entry.pack(**self.properties)

    def __create_buttons(self):
        Checkbutton(
            self.frame,
            text="Remember email",
            variable=self.__email_remember_button,
            onvalue=1,
            offvalue=0,
        ).pack(**self.properties)
        self.__login_button = Button(
            self.frame,
            text="Login",
            command=lambda: Login.login_and_destroy_login_page(
                self.__email_entry.get(),
                self.__password_entry.get(),
                self.__email_remember_button.get(),
                self.__driver,
                self,
            ),
        )
        self.__login_button.pack(**self.properties)

    def start_main_loop(self):
        self.mainloop()
