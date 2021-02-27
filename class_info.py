# import time

class Time:

    def __init__(self) -> None:
        self.minute : int = 1
        self.hour : int = 0

    def __str__(self):
        return f'{self.hour}:{self.minute}'

class Class:

    def __init__(self, name) -> None:
        self.name = name

        self.start = Time()
        self.end = Time()
    
    def __str__(self) -> str:
        return self.name
    
    def __repr__(self) -> str:
        return f'{self.name}, {self.start} - {self.end}'

class ZoomClass(Class):

    zoom_id : str
    zoom_pwd : str

class MeetClass(Class):

    google_meet_link : str