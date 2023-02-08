from tkinter import *

login_credentials = []


def get_login_credentials(root, email, password):
    global login_credentials
    login_credentials = [email.get(), password.get()]
    root.destroy()


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


def gui():
    root = Tk()
    root.geometry("600x400")

    frame = Frame(root, bg="lightblue")
    frame.pack(fill="both", expand=True)

    Label(frame, text="Enter your login credentials:").pack(anchor=CENTER)

    email = EntryWithPlaceholder(frame, "Email address")
    email.pack()
    password = EntryWithPlaceholder(frame, "Password")
    password.config(show="*")
    password.pack()

    Button(frame, text="Login", command=lambda: get_login_credentials(root, email, password)).pack()
    root.mainloop()

    return login_credentials
