from tkinter import messagebox
from src.messages.errorMessages import INVALID_EMAIL_MSG, INVALID_EMAIL_TITLE

class EmailError(Exception):
    def __init__(self):
        super().__init__(INVALID_EMAIL_MSG)
        messagebox.showerror(INVALID_EMAIL_TITLE, INVALID_EMAIL_MSG)
