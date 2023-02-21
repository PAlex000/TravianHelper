from tkinter import *
from src.gui.pages.defaultPage import DefaultPage

class ServerPage(DefaultPage):
    def __init__(self, title, serverElements):
        super().__init__(title)
        self.__serverElements = serverElements
        self.__serverName = "Unknown serverNname"
        self.__serverElement = "Unknown serverElement"
        self.__count = IntVar()
        self.__frame = Frame(self, bg="lightblue")
        self.__frame.pack(fill="both", expand=TRUE)

    def serverGui(self):
        Label(self.__frame, text="Please choose which server you want to login: ").pack(**self.properties)
        self.__count.set(1)
        for key, value in self.__serverElements.items():
            # RadioButton are different if their values are different. so I give them var.get(which I increase by 1)
            Radiobutton(self.__frame, text=key, variable=self.__count, value=self.__count.get()).pack(**self.properties)
            self.__count.set(self.__count.get() + 1)
        Button(self.__frame, text="Choose", command=self.__getServerDetails).pack(**self.properties)
        self.__count.set(1)
        self.mainloop()

        return [self.__serverName, self.__serverElement]

    def __getServerDetails(self):
        self.__serverName = list(self.__serverElements.keys())[self.__count.get() - 1]
        self.__serverElement = list(self.__serverElements.values())[self.__count.get() - 1]
        self.destroy()
