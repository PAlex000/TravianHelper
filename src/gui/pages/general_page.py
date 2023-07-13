import math
from tkinter import Button, Canvas, Frame, Label, Menu, Tk
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


# def __add_village_frame(self):
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
        draw_field_view(self.__field_canvas, 300, 150, 18, field_ids=self.__field_ids)
        draw_field_view(self.__infra_canvas, 300, 150, 22, infra_ids=self.__infra_ids)

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
            height=300,
            highlightbackground="black",
            highlightthickness=1,
        )
        self.__village_field_view_frame.pack(side="top", anchor="w")
        self.__village_field_view_frame.pack_propagate(False)

    def __add_village_infra_view_frame(self):
        self.__village_infra_view_frame = Frame(
            self,
            width=600,
            height=300,
            highlightbackground="black",
            highlightthickness=1,
        )
        self.__village_infra_view_frame.pack(side="left", anchor="n")
        self.__village_infra_view_frame.pack_propagate(False)

    def __add_village_names_to_frame(self):
        Label(self.__village_name_frame, text="village1").pack(side="left", anchor="n")

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
            command=lambda: Village(self.__driver).set_village(
                {
                    "infra_canvas": self.__infra_canvas,
                    "field_canvas": self.__field_canvas,
                    "infra_ids": self.__infra_ids,
                    "field_ids": self.__field_ids,
                }
            ),
        )
        refresh_button.pack(side="left")


def draw_field_view(canvas, x, y, triangle_count, field_ids={}, infra_ids={}):
    angle = 360 / triangle_count

    for i in range(triangle_count):
        x1 = x + 150 * math.cos(math.radians(angle * i))
        y1 = y + 150 * math.sin(math.radians(angle * i))
        x2 = x + 150 * math.cos(math.radians(angle * (i + 1)))
        y2 = y + 150 * math.sin(math.radians(angle * (i + 1)))
        x3 = x
        y3 = y

        canvas.create_polygon(x1, y1, x2, y2, x3, y3, outline="black", fill="")
        x_center = (x1 + x2 + x3) / 3
        y_center = (y1 + y2 + y3) / 3
        canvas.create_oval(
            x_center - 10, y_center - 10, x_center + 10, y_center + 10, fill="white"
        )
        id = canvas.create_text(x_center, y_center, text=str(0))
        # Field view has 18 buildings but infra view has 20 (+2)
        if triangle_count == 18:
            field_ids[i + 1] = id
        else:
            infra_ids[i + 19] = id
