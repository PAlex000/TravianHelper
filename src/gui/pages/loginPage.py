from tkinter import *
from src.messages.error_messages import *
from src.gui.pages.defaultPage import DefaultPage
from src.gui.loginAttempt import LoginAttempt

class LoginPage(DefaultPage):

    def __init__(self, title="Login Credentials",):
        super().__init__(title)
        self.__emailRememberButton = IntVar()
        self.__loginCredentials = ""

    @property
    def loginCredentials(self):
        return self.__loginCredentials
    
    def createLoginPage(self):
        self.__createFrame()
        self.__createEntries()
        self.__createButtons()
        self.mainloop()

    def __createFrame(self):
        self.__frame = Frame(self, bg="lightblue")
        self.__frame.pack(fill="both", expand=TRUE)

    def __createEntries(self):
        self.__emailEntry = Entry(self.__frame)
        self.__emailEntry.insert(0, 'Email')
        self.__emailEntry.pack(**self.properties)
        self.__passwordEntry = Entry(self.__frame)
        self.__passwordEntry.config(show="*")
        self.__passwordEntry.pack(**self.properties)
    
    def __createButtons(self):
        self.__checkbtn = Checkbutton(self.__frame, text='Remember email', variable=self.__emailRememberButton, onvalue=1, offvalue=0)
        self.__checkbtn.pack(**self.properties)
        Button(self.__frame, text="Login",
               command=self.__loginAndDestroyLoginPage).pack(**self.properties)
        
    def __loginAndDestroyLoginPage(self):
        attempt = LoginAttempt(self.__emailEntry.get(), self.__passwordEntry.get(), self.__emailRememberButton.get())
        self.__loginCredentials = attempt.getStatus()
        self.__destroyLoginPage()

    def __destroyLoginPage(self):
        self.destroy()
