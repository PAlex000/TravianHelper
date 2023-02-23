from tkinter import Button, IntVar, Label, Radiobutton

from src.gui.attempts.serverChooseAttempt import ServerChooseAttempt
from src.gui.pages.defaultPage import DefaultPage


class ServerPage(DefaultPage):

    def __init__(self, serverElements, title = "Server Page"):
        super().__init__(title)
        self.__serverElements = serverElements
        self.__serverDetails = []
        self.__serverCount = IntVar()
        self.__serverNames = []

    @property
    def serverDetails(self):
        return self.__serverDetails

    def createServerPage(self):
        self.__createLabel()
        self.__createButtons()
        self.mainloop()

    def __createLabel(self):
        Label(self.frame, text="Please choose which server you want to login: ") \
        .pack(**self.properties)

    def __createButtons(self):
        self.__getServerNames()
        for serverName in self.__serverNames:
            Radiobutton(self.frame, text=serverName, variable=self.__serverCount,
                        value=self.__serverCount.get()).pack(**self.properties)
            self.__serverCount.set(self.__serverCount.get() + 1)
        Button(self.frame, text="Choose", command=self.__serverChooseAndDestroyServerPage) \
        .pack(**self.properties)
        # Make the first element default
        self.__serverCount.set(0)

    def __getServerNames(self):
        for serverName in self.__serverElements.keys():
            self.__serverNames.append(serverName)

    def __serverChooseAndDestroyServerPage(self):
        selectedServerName = list(self.__serverElements.keys())[self.__serverCount.get()]
        selectedServerElement = list(self.__serverElements.values())[self.__serverCount.get()]
        attempt = ServerChooseAttempt(selectedServerName, selectedServerElement)
        self.__serverDetails = attempt.getStatus()
        self.__destroyServerPage()

    def __destroyServerPage(self):
        self.destroy()
