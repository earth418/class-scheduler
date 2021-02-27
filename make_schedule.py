from datetime import datetime
from tkinter import * 
from class_info import *

class Schedule:
    DAYS = ["monday", "tuesday", "wednesday", "thursday", "friday"]

    def __init__(self) -> None: 
        self.monday : list = []
        self.tuesday : list = []
        self.wednesday : list = []
        self.thursday : list = []
        self.friday : list = []

    def get_list(self):
        return [self.monday, self.tuesday, self.wednesday, self.thursday, self.friday]

    '''
    Returns a list of the classes on a given day.
    '''
    def get_classes_on(self, day : str) -> list:
        return getattr(self, day)

class App:

    def __init__(self, master : Tk) -> None:
        self.schedule = Schedule()
        self.master = master

        self.BOX_SIZE = 100

        class_list = self.schedule.get_list()

        for day in class_list:
            for i in range(8):
                day.append(Class(f'Class {i + 1}'))

        self.init_display()

        self.display_schedule()

    def update(self):

        pass

    @staticmethod
    def create_box(canvas : Canvas, box_coords : tuple, **kwargs):

        box_kwargs = {}
        text_kwargs = {}

        for key, val in kwargs.items():
            # print(key)
            if key[0:2] == 't_':
                text_kwargs[key[2:]] = val
            else:
                box_kwargs[key] = val

        a = canvas.create_rectangle(box_coords[0], box_coords[1], box_coords[2], box_coords[3], box_kwargs)
        b = canvas.create_text((box_coords[0] + box_coords[2]) / 2, (box_coords[1] + box_coords[3]) / 2, text_kwargs)
        return a, b

    def set_schedule_item(self, day : str, in_class : Class):
        index = [_class.name for _class in self.schedule.get_classes_on(day)].index(in_class.name)
        if index == -1:
            getattr(self.schedule, day).append(in_class)
        else:
            getattr(self.schedule, day)[index] = in_class

    def init_display(self):
        self.canvas = Canvas(self.master, width = 500, height = 1000)
        self.canvas.pack()

        for index, day in enumerate(Schedule.DAYS):
            day = day[0].upper() + day[1:]
            box_loc = (index * self.BOX_SIZE, 0, index * self.BOX_SIZE + self.BOX_SIZE, self.BOX_SIZE)
            a, b = self.create_box(self.canvas, box_loc, t_text=day, t_font = ("",13))


    def display_schedule(self):

        class_list = self.schedule.get_list()

        for day_index, day in enumerate(class_list):
            for class_index, _class in enumerate(day):
                box_loc = (day_index * self.BOX_SIZE, class_index * self.BOX_SIZE + self.BOX_SIZE,
                            day_index * self.BOX_SIZE + self.BOX_SIZE, class_index * self.BOX_SIZE + 2 * self.BOX_SIZE)
                    
                a, b = self.create_box(self.canvas, box_loc, t_text=_class.name)
                


root = Tk()
app = App(root)

root.title("Schedule Maker")
root.geometry("500x900")

while True:
    app.update()
    root.update()
    root.update_idletasks()
