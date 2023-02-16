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


class Default_page(Tk):

    def __init__(self, title):
        super().__init__()
        self.geometry("600x400")
        self.__placing = {'ipadx': 20, 'ipady': 10, 'fill': X}
        self.title(title)

    @property
    def placing(self):
        return self.__placing


class Login_page(Default_page):

    regex_for_email = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

    def __init__(self, title):
        super().__init__(title)
        self.__text = title
        self.__credentials = []
        self.__frame = Frame(self, bg="lightblue")
        self.__frame.pack(fill="both", expand=TRUE)

    def __email_check(self):
        if not re.fullmatch(Login_page.regex_for_email, self.__email.get()):
            messagebox.showerror(INVALID_EMAIL_TITLE, INVALID_EMAIL_MSG)
            return
        
    def __get_login_credentials(self):
        self.__email_check()
        self.__credentials.append(self.__email.get())
        self.__credentials.append(self.__password.get())
        self.destroy()
    
    def __set_entries(self):
        Label(self.__frame, text=self.__text).pack(**self.placing)
        self.__email = EntryWithPlaceholder(self.__frame, "Email address")
        self.__email.pack(**self.placing)
        self.__password = EntryWithPlaceholder(self.__frame, "Password")
        self.__password.config(show="*")
        self.__password.pack(**self.placing)
        Button(self.__frame, text="Login", command=self.__get_login_credentials).pack(**self.placing)
        self.mainloop()
        
    def login_gui(self):
        self.__set_entries()
        return self.__credentials


class Server_page(Default_page):
    def __init__(self, title, container):
        super().__init__(title)
        self.__container = container
        self.__server_name = "Unknown_server_name"
        self.__server_element = "Unknown_server_element"
        self.__var = IntVar()
        self.__frame = Frame(self, bg="lightblue")
        self.__frame.pack(fill="both", expand=TRUE)

    def server_gui(self):
        Label(self.__frame, text="Please choose which server you want to login: ").pack(**self.placing)
        self.__var.set(1)
        for key, value in self.__container.items():
            # RadioButton are different if their values are different. so I give them var.get(which I increase by 1)
            Radiobutton(self.__frame, text=key, variable=self.__var, value=self.__var.get()).pack(**self.placing)
            self.__var.set(self.__var.get() + 1)
        Button(self.__frame, text="Choose", command=self.__get_server_details).pack(**self.placing)
        self.__var.set(1)
        self.mainloop()

        return [self.__server_name, self.__server_element]

    def __get_server_details(self):
        self.__server_name = list(self.__container.keys())[self.__var.get() - 1]
        self.__server_element = list(self.__container.values())[self.__var.get() - 1]
        self.destroy()
