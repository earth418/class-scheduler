# import time

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
        self.end = end #Time(0, 0)
    
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
    
    # def __repr__(self) -> str:
    #     return f'{self.name}, {self.start} - {self.end}'

class ZoomClass(Class):

    zoom_id : str
    zoom_pwd : str

class MeetClass(Class):

    google_meet_link : str