from tkinter import *

class DefaultPage(Tk):

    def __init__(self, title):
        super().__init__()
        self.geometry("600x400")
        self.__properties = {'ipadx': 20, 'ipady': 10, 'fill': X}
        self.title(title)

    @property
    def properties(self):
        return self.__properties
