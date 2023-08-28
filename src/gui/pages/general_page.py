import math
from tkinter import Button, Canvas, Frame, Label, Menu, Tk

from selenium.webdriver.common.by import By

from src.webscrape.views.village_view import Village


class MenuBar(Menu):
    def __init__(self, ws):
        Menu.__init__(self, ws)

    def _add_file_to_the_menubar(self):
        file = Menu(self, tearoff=False)
        file.add_command(label="Settings")
        file.add_command(label="Help")
        file.add_command(label="Exit", command=self.quit)
        self.add_cascade(label="File", menu=file)


class GeneralPage(Tk):
    def __init__(self, driver):
        super().__init__()
        self.__driver = driver
        self.title("General Page")
        self.geometry("1024x768")

        self.__under_frame = ""
        self.__village_name_frame = ""
        self.__task_view_frame = ""
        self.__village_field_view_frame = ""
        self.__village_infra_view_frame = ""
        self.__field_canvas = ""
        self.__infra_canvas = ""
        self.__field_ids = {}
        self.__infra_ids = {}

        menu_bar = MenuBar(self)
        menu_bar._add_file_to_the_menubar()

        self.config(menu=menu_bar)

        self.__add_under_frame()
        self.__add_village_name_frame()
        self.__add_task_view_frame()
        self.__add_village_field_view_frame()
        self.__add_village_infra_view_frame()

        self.__add_village_names_to_frame()
        self.__add_tasks_to_frame()

        self.__add_canvas_to_field_frame()
        self.__add_canvas_to_infra_frame()
        self.__create_labels_for_fields()
        self.__create_labels_for_infra()

        self.__add_refresh_button()

    def __add_under_frame(self):
        self.__under_frame = Frame(
            self,
            width=1024,
            height=168,
            highlightbackground="black",
            highlightthickness=1,
        )
        self.__under_frame.pack(side="bottom", anchor="s")
        self.__under_frame.pack_propagate(False)

    def __add_village_name_frame(self):
        self.__village_name_frame = Frame(
            self,
            width=200,
            height=600,
            highlightbackground="black",
            highlightthickness=1,
        )
        self.__village_name_frame.pack(side="left", anchor="n")
        self.__village_name_frame.pack_propagate(False)

    def __add_task_view_frame(self):
        self.__task_view_frame = Frame(
            self,
            width=224,
            height=600,
            highlightbackground="black",
            highlightthickness=1,
        )
        self.__task_view_frame.pack(side="right", anchor="n")
        self.__task_view_frame.pack_propagate(False)

    def __add_village_field_view_frame(self):
        self.__village_field_view_frame = Frame(
            self,
            width=600,
            height=260,
            highlightbackground="black",
            highlightthickness=1,
        )
        self.__village_field_view_frame.pack(side="top", anchor="w")
        self.__village_field_view_frame.pack_propagate(0)

    def __add_village_infra_view_frame(self):
        self.__village_infra_view_frame = Frame(
            self,
            width=600,
            height=340,
            highlightbackground="black",
            highlightthickness=1,
        )
        self.__village_infra_view_frame.pack(side="left", anchor="n")
        self.__village_infra_view_frame.pack_propagate(False)

    def __add_village_names_to_frame(self, village_name="Unknown village"):
        Label(
            self.__village_name_frame,
            text=village_name,
            width=30,
            height=2,
            relief="raised",
            bg="grey",
            cursor="hand2",
        ).pack()
        # label.bind("<Button-1>", lambda event: self.say_something("Hi"))

    def __add_tasks_to_frame(self):
        Label(self.__task_view_frame, text="Task1").pack(side="left", anchor="n")

    def __add_canvas_to_field_frame(self):
        self.__field_canvas = Canvas(
            self.__village_field_view_frame, width=600, height=300
        )
        self.__field_canvas.pack()

    def __add_canvas_to_infra_frame(self):
        self.__infra_canvas = Canvas(
            self.__village_infra_view_frame, width=600, height=300
        )
        self.__infra_canvas.pack()

    def __add_refresh_button(self):
        refresh_button = Button(
            self.__under_frame,
            text="Refresh all villages",
            command=lambda: self.__refresh_everything(
                {
                    "infra_canvas": self.__infra_canvas,
                    "field_canvas": self.__field_canvas,
                    "infra_ids": self.__infra_ids,
                    "field_ids": self.__field_ids,
                },
            ),
        )
        refresh_button.pack(side="left")

    def __refresh_everything(self, ids):
        village_names = self.__get_village_names_from_html()
        self.__destroy_frame_widgets(self.__village_name_frame)
        self.__set_village_names(village_names)
        Village(self.__driver).set_village(ids)

    def __get_village_names_from_html(self):
        # It has several scroll_content, we need the last one
        scroll_content = self.__driver.find_elements(By.CLASS_NAME, "scrollContent")[-1]
        return scroll_content.find_elements(By.CLASS_NAME, "villageEntry")

    def __destroy_frame_widgets(self, frame):
        for widget in frame.winfo_children():
            widget.destroy()

    def __set_village_names(self, names):
        for name in names:
            self.__add_village_names_to_frame(name.get_attribute("innerHTML"))

    def __create_labels_for_fields(self, names=[]):
        for i in range(18):
            id = Label(
                self.__field_canvas,
                text=f"Unknown field{i + 1}",
                width=28,
                height=2,
                relief="raised",
                bg="grey",
                cursor="hand2",
            )
            id.grid(row=i % 6, column=int(i / 6))
            self.__field_ids[i + 1] = id

    def __create_labels_for_infra(self, names=[]):
        for i in range(25):
            id = Label(
                self.__infra_canvas,
                text=f"Unknown building{i + 1}",
                width=28,
                height=2,
                relief="raised",
                bg="grey",
                cursor="hand2",
            )
            id.grid(row=i % 9, column=int(i / 9))
            self.__infra_ids[i + 19] = id
