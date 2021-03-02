from class_info import *
from tkinter import *

class Editor:

    def __init__(self, master, in_class : Class) -> None:
        self.in_class = in_class
        self.root = master

        classname = Label(self.root, text=in_class.name)
        classname.pack()

        self.text_entry = Entry(self.root)
        self.text_entry.pack()

        val = StringVar()
        options = OptionMenu(self.root, val, "Zoom", "Google Meet") #, text="What type of class is this?")
        options.pack()
        # Text(self.root) # Multi-line input

    def update(self):
        
        link = self.text_entry.get()
        # self.in_class



def create_editor(in_class : Class):

    root = Tk()

    root.geometry("200x200")

    app = Editor(root, in_class)

    while True:
        app.update()
        root.update()

    # in_class.end

if __name__ == "__main__":


    create_editor(Class("Yuh!"))