from tkinter import BOTH, TRUE, Frame, Tk


class DefaultPage(Tk):
    def __init__(self, title="unnamed"):
        super().__init__()
        self.geometry("600x400")
        self.__properties = {"ipadx": 20, "ipady": 10, "fill": BOTH}
        self.title(title)
        self.__createFrame()

    def __createFrame(self):
        self.__frame = Frame(self, bg="lightblue")
        self.__frame.pack(fill="both", expand=TRUE)

    @property
    def properties(self):
        return self.__properties

    @property
    def frame(self):
        return self.__frame
