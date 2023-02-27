from tkinter import END, Button, Checkbutton, Entry, IntVar

from src.gui.attempts.loginInputCheck import LoginInputCheck
from src.gui.pages.defaultPage import DefaultPage


class LoginPage(DefaultPage):
    def __init__(
        self,
        title="Login Credentials",
    ):
        super().__init__(title)
        self.__loginCredentials = {"email": "", "password": "", "saveEmail": ""}
        self.__emailEntry = Entry()
        self.__passwordEntry = Entry()
        self.__loginButton = Button()
        self.__emailRememberButton = IntVar()

    @property
    def loginCredentials(self):
        return self.__loginCredentials

    @property
    def emailEntry(self):
        return self.__emailEntry

    @emailEntry.setter
    def emailEntry(self, value):
        self.__emailEntry.delete(0, END)
        self.__emailEntry.insert(0, value)

    @property
    def passwordEntry(self):
        return self.__passwordEntry

    @passwordEntry.setter
    def passwordEntry(self, value):
        self.__passwordEntry.delete(0, END)
        self.__passwordEntry.insert(0, value)

    @property
    def loginButton(self):
        return self.__loginButton

    @property
    def emailRememberButton(self):
        return self.__emailRememberButton

    @emailRememberButton.setter
    def emailRememberButton(self, value):
        self.__emailRememberButton.set(value)

    def createLoginPage(self):
        self.__createEntries()
        self.__createButtons()

    def __createEntries(self):
        self.__emailEntry = Entry(self.frame)
        self.__emailEntry.insert(0, "Email")
        self.__emailEntry.pack(**self.properties)
        self.__passwordEntry = Entry(self.frame)
        self.__passwordEntry.config(show="*")
        self.__passwordEntry.pack(**self.properties)

    def __createButtons(self):
        Checkbutton(
            self.frame,
            text="Remember email",
            variable=self.__emailRememberButton,
            onvalue=1,
            offvalue=0,
        ).pack(**self.properties)
        self.__loginButton = Button(
            self.frame,
            text="Login",
            command=lambda: self.__loginAndDestroyLoginPage(self.__emailRememberButton),
        )
        self.__loginButton.pack(**self.properties)

    def __loginAndDestroyLoginPage(self, emailRememberButton):
        attempt = LoginInputCheck(
            self.__emailEntry.get(),
            self.__passwordEntry.get(),
            emailRememberButton.get(),
        )
        self.__loginCredentials = attempt.getLoginCredentials()
        self.__destroyLoginPage()

    def startMainLoop(self):
        self.mainloop()

    def __destroyLoginPage(self):
        self.destroy()
