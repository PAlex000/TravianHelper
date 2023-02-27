from tkinter import messagebox

from src.messages.errorMessages import (
    INVALID_SERVER_NAME_MSG,
    INVALID_SERVER_NAME_TITLE,
)


class ServerNameError(Exception):
    def __init__(self):
        super().__init__(INVALID_SERVER_NAME_MSG)
        messagebox.showerror(INVALID_SERVER_NAME_TITLE, INVALID_SERVER_NAME_MSG)
