from class_info import *
from tkinter import *

class Editor:

    CLASS_TYPES : list = ["None", "Google Meet", "Zoom"]

    def __init__(self, master : Tk, in_class : Class) -> None:
        self.in_class = in_class
        self.root = master

        # self.name_entry_val = StringVar(value="")

        Label(self.root, text="Class Name", font=("", 10)).pack()

        self.name_entry = Entry(self.root, font=("", 22))
        self.name_entry.pack(padx = 50, pady=0)

        # classname = Label(self.root, text=in_class.name, font=("", 20))
        # classname.pack()

        self.info_frame = Frame(self.root)
        self.info_frame.pack(pady = 10)

        Label(self.info_frame, text="Type:", font=("", 10)).grid(row = 0, column = 0)
        
        self.link_entry_val = StringVar(value=self.CLASS_TYPES[0])
        options = OptionMenu(self.info_frame, self.link_entry_val, *self.CLASS_TYPES) #, text="What type of class is this?")
        options.grid(row = 0, column = 1)

        Label(self.info_frame, text="Link: ", font=("", 10)).grid(row = 1, column = 0)
        
        self.link_entry = Entry(self.info_frame, font=("", 10))
        self.link_entry.grid(row = 1, column = 1)

        exit_frame = Frame(self.root)
        exit_frame.pack(side=BOTTOM)

        Button(exit_frame, text="Cancel", command=self.cancel).pack(side=LEFT, padx=15, pady=25)
        Button(exit_frame, text="Save", command=self.save_close).pack(side=RIGHT, padx=15, pady=25)

    # def update(self):
    #     link = self.text_entry.get()

    def save_close(self):
        if self.link_entry_val.get() == "None":
        
            self.in_class
        
        else:

            self.in_class
        

        self.root.destroy()

    def cancel(self):
        self.root.destroy()



def create_editor(in_class : Class):

    root = Tk()

    root.geometry("250x250")

    app = Editor(root, in_class)

    root.mainloop()
    # while True:
    #     app.update()
    #     root.update()

if __name__ == "__main__":

    create_editor(Class("Yuh!"))