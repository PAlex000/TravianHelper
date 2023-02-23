from tkinter import messagebox
from src.messages.errorMessages import INVALID_SERVER_ELEMENT_TITLE, INVALID_SERVER_ELEMENT_MSG

class ServerElementError(Exception):
    def __init__(self):
        super().__init__(INVALID_SERVER_ELEMENT_MSG)
        messagebox.showerror(INVALID_SERVER_ELEMENT_TITLE, INVALID_SERVER_ELEMENT_MSG)
