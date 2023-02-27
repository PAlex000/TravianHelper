from tkinter import Button, IntVar, Label, Radiobutton

from src.gui.attempts.serverNameCheck import ServerNameCheck
from src.gui.pages.defaultPage import DefaultPage


class ServerPage(DefaultPage):
    def __init__(self, serverElements, title="Server Page"):
        super().__init__(title)
        self.__serverElements = serverElements
        self.__serverDetails = {"servername": "", "serverelement": ""}
        self.__serverCount = IntVar()
        self.__serverCount.set(0)
        self.__serverNames = []
        self.__chooseButton = Button()

    @property
    def serverDetails(self):
        return self.__serverDetails

    @property
    def serverCount(self):
        return self.__serverCount

    @property
    def serverNames(self):
        return self.__serverNames

    @serverNames.setter
    def serverNames(self, name):
        self.__serverNames.append(name)

    @property
    def chooseButton(self):
        return self.__chooseButton

    def createServerPage(self):
        self.__createLabel()
        self.__createButtons()
        self.mainloop()

    def __createLabel(self):
        Label(self.frame, text="Please choose which server you want to login: ").pack(
            **self.properties
        )

    def __createButtons(self):
        self.__getServerNames()
        for serverName in self.__serverNames:
            Radiobutton(
                self.frame,
                text=serverName,
                variable=self.__serverCount,
                value=self.__serverCount.get(),
            ).pack(**self.properties)
            self.__serverCount.set(self.__serverCount.get() + 1)
        self.__chooseButton = Button(
            self.frame, text="Choose", command=self.__serverChooseAndDestroyServerPage
        )
        self.__chooseButton.pack(**self.properties)
        # Make the first element default
        self.__serverCount.set(0)

    def __getServerNames(self):
        for serverName in self.__serverElements.keys():
            self.__serverNames.append(serverName)

    def __serverChooseAndDestroyServerPage(self):
        selectedServerName = list(self.__serverElements.keys())[
            self.__serverCount.get()
        ]
        selectedServerElement = list(self.__serverElements.values())[
            self.__serverCount.get()
        ]
        attempt = ServerNameCheck(selectedServerName, selectedServerElement)
        self.__serverDetails = attempt.getServerDetails()
        self.__destroyServerPage()

    def __destroyServerPage(self):
        self.destroy()
