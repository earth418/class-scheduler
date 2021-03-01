import keyboard, sys
from time import sleep
import webbrowser as wb

class Time:

    def __init__(self, hr, min) -> None:
        self.minute : int = min
        self.hour : int = hr

    def __str__(self):
        return f'{self.hour:02d}:{self.minute:02d}'

    def __add__(self, other):
        return Time(self.hour + other.hour, self.minute + other.minute)
    
    def __mul__(self, other):
        if isinstance(other, Time):
            return Time(self.hour * other.hour, self.minute * other.minute)
        else:
            return Time(self.hour * other, self.minute * other)

    def __sub__(self, other):
        return self + (other * -1)

    @staticmethod
    def from_str(string):
        # print(rf'"{string}"')
        return Time(int(string[0:2]), int(string[3:5]))

class Class:

    def __init__(self, name, start=Time(0, 0), end=Time(0, 0)) -> None:
        self.name = name

        # if start is not None:
        self.start = start
        self.end = end

        self.is_in_class = False
    
    '''
    Returns each class's name, and start time to end time in the format:
    <class name>, <start_time> - <end time>
    For example, a class named "Physics" starting at 2:00 PM and ending at 3:00 PM would be returned as:
    Physics, 14:00 - 15:00
    '''
    def __str__(self) -> str:
        return f'{self.name}, {self.start}-{self.end}'

    def get_length(self) -> Time:
        return self.end - self.start

class ZoomClass(Class):

    def __init__(self, name, start, end) -> None:
        
        super().__init__(name, start=start, end=end)

        self.zoom_id : str = ''
        self.zoom_pwd : str = ''

    def join_zoom_class(self):
        if self.is_in_class:
            raise "Error; already in class!"
        else:
            pass

    def leave_zoom_class(self):
        if self.is_in_class:
            pass
        else:
            raise "Not in a class!"


class MeetClass(Class):

    CHROME_DIR : str = ''
    path = str(sys.path).split(';')
    
    for path_item in path:
        
        if "chrome" in path_item.lower():
            chrome_dir = path_item
            break

    def __init__(self, name, start, end) -> None:
        
        super().__init__(name, start=start, end=end)
        self.google_meet_link : str = ''

    def join_google_meet(self):

        chrome_dir = ''
        path = str(sys.path).split(';')
        for path_item in path:
            if "chrome" in path.lower():
                chrome_dir = path_item
                break

        wb.BackgroundBrowser(chrome_dir).open_new_tab(self.google_meet_link)

def leave_google_meet(self):
    if self.is_in_class:
        keyboard.send("CTRL+W")
        pass
    else:
        raise "Not in a class!"