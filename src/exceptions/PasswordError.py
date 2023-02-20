from tkinter import messagebox
from src.messages.error_messages import INVALID_PASSWORD_TITLE, INVALID_PASSWORD_MSG

class PasswordError(Exception):
    def __init__(self):
        super().__init__(INVALID_PASSWORD_MSG)
        messagebox.showerror(INVALID_PASSWORD_TITLE, INVALID_PASSWORD_MSG)
