from tkinter import Button, IntVar, Label, Radiobutton

from src.gui.attempts.server_name_check import ServerNameCheck
from src.gui.pages.default_page import DefaultPage


class ServerPage(DefaultPage):
    def __init__(self, server_elements, title="Server Page"):
        super().__init__(title)
        self.__server_elements = server_elements
        self.__server_details = {"servername": "", "serverelement": ""}
        self.__server_count = IntVar()
        self.__server_count.set(0)
        self.__server_names = []
        self.__choose_button = Button()

    @property
    def server_details(self):
        return self.__server_details

    @property
    def server_count(self):
        return self.__server_count

    @property
    def server_names(self):
        return self.__server_names

    @server_names.setter
    def server_names(self, name):
        self.__server_names.append(name)

    @property
    def choose_button(self):
        return self.__choose_button

    def create_server_page(self):
        self.__create_label()
        self.__create_buttons()
        self.mainloop()

    def __create_label(self):
        Label(self.frame, text="Please choose which server you want to login: ").pack(
            **self.properties
        )

    def __create_buttons(self):
        self.__set_server_names()
        for server_name in self.__server_names:
            Radiobutton(
                self.frame,
                text=server_name,
                variable=self.__server_count,
                value=self.__server_count.get(),
            ).pack(**self.properties)
            self.__server_count.set(self.__server_count.get() + 1)
        self.__choose_button = Button(
            self.frame,
            text="Choose",
            command=self.__server_choose_and_destroy_server_page,
        )
        self.__choose_button.pack(**self.properties)
        # Make the first element default
        self.__server_count.set(0)

    def __set_server_names(self):
        for server_name in self.__server_elements.keys():
            self.__server_names.append(server_name)

    def __server_choose_and_destroy_server_page(self):
        selected_server_name = list(self.__server_elements.keys())[
            self.__server_count.get()
        ]
        selected_server_element = list(self.__server_elements.values())[
            self.__server_count.get()
        ]
        attempt = ServerNameCheck(selected_server_name, selected_server_element)
        self.__server_details = attempt.get_server_details()
        self.__destroy_server_page()

    def __destroy_server_page(self):
        self.destroy()
