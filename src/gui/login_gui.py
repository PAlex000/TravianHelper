import re
from tkinter import *
from tkinter import messagebox
from src.messages.error_messages import *

class EntryWithPlaceholder(Entry):
    def __init__(self, master=None, placeholder="PLACEHOLDER", color='grey'):
        super().__init__(master)

        self.placeholder = placeholder
        self.placeholder_color = color
        self.default_fg_color = self['fg']

        self.bind("<FocusIn>", self.foc_in)
        self.bind("<FocusOut>", self.foc_out)

        self.put_placeholder()

    def put_placeholder(self):
        self.insert(0, self.placeholder)
        self['fg'] = self.placeholder_color

    def foc_in(self, *args):
        if self['fg'] == self.placeholder_color:
            self.delete('0', 'end')
            self['fg'] = self.default_fg_color

    def foc_out(self, *args):
        if not self.get():
            self.put_placeholder()

class DefaultPage(Tk):

    def __init__(self, title):
        super().__init__()
        self.geometry("600x400")
        self.__properties = {'ipadx': 20, 'ipady': 10, 'fill': X}
        self.title(title)

    @property
    def properties(self):
        return self.__properties

class LoginPage(DefaultPage):

    regexForEmail = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

    def __init__(self, title):
        super().__init__(title)
        self.__email = ""
        self.__password = ""
        self.__frame = Frame(self, bg="lightblue")
        self.__frame.pack(fill="both", expand=TRUE)
    
    def loginGui(self):
        self.__setEntries()
        return [self.__email, self.__password, self.__emailRememberButton]

    def __setEntries(self):
        self.__emailEntry = EntryWithPlaceholder(self.__frame, "Email address")
        self.__emailEntry.pack(**self.properties)
        self.__passwordEntry = EntryWithPlaceholder(self.__frame, "Password")
        self.__passwordEntry.config(show="*")
        self.__passwordEntry.pack(**self.properties)
        self.__emailRememberButton = IntVar()
        Checkbutton(self.__frame, text='Remember email', variable=self.__emailRememberButton, onvalue=1, offvalue=0).pack(**self.properties)
        Button(self.__frame, text="Login", command=self.__getLoginCredentials).pack(**self.properties)
        self.mainloop()

    def __getLoginCredentials(self):
        self.__emailCheck()
        self.__email = self.__emailEntry.get()
        self.__password = self.__passwordEntry.get()
        self.destroy()

    def __emailCheck(self):
        if not re.fullmatch(LoginPage.regexForEmail, self.__emailEntry.get()):
            messagebox.showerror(INVALID_EMAIL_TITLE, INVALID_EMAIL_MSG)
            return

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
