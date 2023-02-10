import re
from tkinter import *
from tkinter import messagebox
from error_messages import *

login_credentials = []
# Regex for emails.
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'


def get_login_credentials(root, email, password):
    if not re.fullmatch(regex, email.get()):
        messagebox.showerror(INVALID_EMAIL_TITLE, INVALID_EMAIL_MSG)
        return
    global login_credentials
    login_credentials = [email.get(), password.get()]
    root.destroy()


def get_server(server):
    print("SERVER: " + server)
    pass


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


def login_gui():
    root = Tk()
    root.geometry("600x400")
    root.title("Login credentials")
    frame = Frame(root, bg="lightblue")
    frame.pack(fill="both", expand=TRUE)

    placing = {'ipadx': 20, 'ipady': 10, 'fill': X}

    Label(frame, text="Enter your login credentials:").pack(**placing)

    email = EntryWithPlaceholder(frame, "Email address")
    email.pack(**placing)
    password = EntryWithPlaceholder(frame, "Password")
    password.config(show="*")
    password.pack(**placing)

    Button(frame, text="Login", command=lambda: get_login_credentials(root, email, password)).pack(**placing)
    root.mainloop()

    return login_credentials


# GUI for server choosing. It only contains checkboxes and a submit button, checkboxes are the server names.
def server_gui(container):
    root = Tk()
    root.geometry("600x400")
    root.title("Server choosing")
    frame = Frame(root, bg="lightblue")
    frame.pack(fill="both", expand=TRUE)

    placing = {'ipadx': 20, 'ipady': 10, 'fill': X}
    Label(frame, text="Please choose which server you want to login: ")
    #TODO Make radiobuttons unique, and make them to return the correct button.
    for key, value in container.items():
        print("Well yea: " + key)
        Radiobutton(frame, text=key, variable=key).pack(**placing)
    Button(frame, text="Choose", command=lambda: get_server(key)).pack(**placing)
    root.mainloop()
