import re
from tkinter import *
from tkinter import messagebox
from messages.error_messages import *


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

class Login():

    regex_for_email = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    server = []
    def __init__(self, title, window):
        self.__window = window
        self.__window.geometry("600x400")
        self.__frame = Frame(self.__window, bg="lightblue")
        self.__frame.pack(fill="both", expand=TRUE)
        self.__placing = {'ipadx': 20, 'ipady': 10, 'fill': X}
        self.__window.title(title)

    def __email_check(self):
        if not re.fullmatch(Login.regex_for_email, self.__email.get()):
            messagebox.showerror(INVALID_EMAIL_TITLE, INVALID_EMAIL_MSG)
            return
        
    def __get_login_credentials(self):
        self.__email_check()
        self.__lista = []
        self.__lista.append(self.__email.get())
        self.__lista.append(self.__password.get())
        self.__window.destroy()
    
    def __set_entries(self):
        Label(self.__window, text="Login credentials").pack(**self.__placing)
        self.__email = EntryWithPlaceholder(self.__window, "Email address")
        self.__email.pack(**self.__placing)
        self.__password = EntryWithPlaceholder(self.__window, "Password")
        self.__password.config(show="*")
        self.__password.pack(**self.__placing)
        Button(self.__window, text="Login", command=self.__get_login_credentials).pack(**self.__placing)
        self.__window.mainloop()

    def login_gui(self):
        self.__set_entries()
        return self.__lista
    

# GUI for server choosing. It only contains checkboxes and a submit button, checkboxes are the server names.
def server_gui(container):
    root = Tk()
    root.geometry("600x400")
    root.title("Server choosing")
    frame = Frame(root, bg="lightblue")
    frame.pack(fill="both", expand=TRUE)

    placing = {'ipadx': 20, 'ipady': 10, 'fill': X}
    Label(frame, text="Please choose which server you want to login: ")
    var = IntVar()
    var.set(1)
    for key, value in container.items():
        # RadioButton are different if their values are different. so I give them var.get(which I increase by 1)
        Radiobutton(frame, text=key, variable=var, value=var.get()).pack(**placing)
        var.set(var.get() + 1)
    Button(frame, text="Choose", command=lambda: get_values(container, var, root)).pack(**placing)
    var.set(1)
    root.mainloop()
    return server


# Get the server name and server element from the container, and give it to the server variable
def get_values(container, var, root):
    server_name = list(container.keys())[var.get() - 1]
    server_element = list(container.values())[var.get() - 1]
    global server
    server = [server_name, server_element]
    root.destroy()
