from tkinter import *
from tkinter import messagebox, filedialog
from schedule import Schedule
from class_info import *
from task_scheduler import create_task
from schedule_item_editor import create_editor

class App:

    def __init__(self, master : Tk) -> None:
        self.schedule = Schedule()
        self.master = master
        self.schedule_grid = {"monday" : {}, "tuesday" : {}, "wednesday" : {}, "thursday" : {}, "friday" : {}}

        self.BOX_SIZE = 100

        class_list = self.schedule.get_list()

        for day in class_list:
            for i in range(5):
                day.append(Class(f'Class {i + 1}'))

        self.init_display()

        self.init_schedule()

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

    # Initializes the display
    def init_display(self):

        # Creating the Days tab

        days_frame = Frame(self.master)
        days_frame.pack(side=TOP)

        # Creating the Reset, Save, and Setup Task buttons
        menu_frame = Frame(self.master)
        menu_frame.pack(side=TOP)
        
        reset = Button(menu_frame, text='Reset Schedule', command=self.reset)
        reset.pack(side=LEFT)
        
        save = Button(menu_frame, text='Save to File', command=self.save)
        save.pack(side=RIGHT)

        save = Button(menu_frame, text='Setup Task', command=self.setup_task)
        save.pack(side=RIGHT)

        open_button = Button(menu_frame, text='Open from File', command=self.open_file)
        open_button.pack()

        # Creating the canvas
        self.canvas = Canvas(self.master, width = 500, height = 700)

        # Binding Mouse Events
        self.canvas.bind('<ButtonPress-1>', self.pickup)
        self.canvas.bind("<B1-Motion>", self.move_item)
        self.canvas.bind("<ButtonRelease-1>", self.release)
        self.canvas.bind("<Double-Button-1>", self.select)

        # Packing and setting focus, so the mouse will always work.
        self.canvas.pack()
        self.canvas.focus_set()

        # Creating the labels for each day
        for index, day in enumerate(Schedule.DAYS):
            day = day[0].upper() + day[1:]
            box_loc = (index * self.BOX_SIZE, 0, index * self.BOX_SIZE + self.BOX_SIZE, self.BOX_SIZE)
            a, b = self.create_box(self.canvas, box_loc, t_text=day, t_font = ("",13))

    # Empties the schedule
    def reset(self):
        will_reset = messagebox.askyesno("Reset", "Are you sure you want to reset your board?")
        if will_reset:
            self.schedule.clear()
            self.init_schedule()

    # Saves the schedule to a file    
    def save(self):
        f = filedialog.asksaveasfile(mode="w", confirmoverwrite=True, defaultextension=".sch")
        if f is None:
            return

        f.write(str(self.schedule))
        f.close()
    
    # Sets up a task to automatically run the schedule.
    def setup_task(self):
        create_task(self.schedule)

    # Select a box, for modification.
    def select(self, event : Event):
        print(self.canvas.find_closest(event.x, event.y))
        pass

 
    def open_file(self):
        filename = filedialog.askopenfilename(defaultextension='.sch')
        self.schedule = Schedule.open(filename)

        # When the box is starting to be drug by the mouse, for movement.
    
    # When the box is starting to be drug by the mouse, for movement.
    def pickup(self, event):
        item_index = self.canvas.find_closest(event.x, event.y)
        # ind = self.schedule_grid.index(
        if (item_index, item_index + 1) in self.schedule_grid:
            self.selected_box = (item_index, item_index + 1)
        elif (item_index, item_index - 1) in self.schedule_grid:
            self.selected_box = (item_index, item_index - 1)
        
        print(self.selected_box)
        self.canvas.move()
        pass

    # While the box is being drug
    def move_item(self, event):
        pass

    # When the box is released
    def release(self, event):
        pass

    # def display_class(self, in_class : Class, *args, **kwargs):
    #     box_loc = (day_index * self.BOX_SIZE, class_index * self.BOX_SIZE + self.BOX_SIZE,
    #                         day_index * self.BOX_SIZE + self.BOX_SIZE, class_index * self.BOX_SIZE + 2 * self.BOX_SIZE)

    #     a, b = self.create_box(self.canvas, box_loc, t_text=_class.name)

    def init_schedule(self):

        class_list = self.schedule.get_list()

        for day_index, day in enumerate(class_list):
            for class_index, _class in enumerate(day):
                box_loc = (day_index * self.BOX_SIZE, class_index * self.BOX_SIZE + self.BOX_SIZE,
                            day_index * self.BOX_SIZE + self.BOX_SIZE, class_index * self.BOX_SIZE + 2 * self.BOX_SIZE)
                    
                a, b = self.create_box(self.canvas, box_loc, t_text=_class.name)
                self.schedule_grid[day][str(_class)] = (a, b)


root = Tk()
app = App(root)

root.title("Schedule Maker")
root.geometry("500x800")

while True:
    app.update()
    root.update()
    root.update_idletasks()
