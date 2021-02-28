from class_info import *

class Schedule:
    DAYS = ["monday", "tuesday", "wednesday", "thursday", "friday"]

    def __init__(self) -> None: 
        self.monday : list = []
        self.tuesday : list = []
        self.wednesday : list = []
        self.thursday : list = []
        self.friday : list = []

    '''
    Reinterprets the Schedule as a list of 'Class' objects, indexed from 0 -> 4 for Monday through Friday. 
    '''
    def get_list(self):
        return [self.monday, self.tuesday, self.wednesday, self.thursday, self.friday]

    '''
    Returns a list of the classes on a given day.
    '''
    def get_classes_on(self, day : str) -> list:
        return getattr(self, day)

    '''
    Clears the schedule of its classes.
    '''
    def clear(self):
        [getattr(self, day).clear() for day in self.DAYS]

    '''
    Returns the schedule as a string, with each class separated by lines.
    '''
    def __str__(self):
        s = ''
        for day in self.DAYS:
            s += day + "\n"
            for _class in getattr(self, day):
                s += f'{_class};'
            s += "\n"
        return s

    '''
    Opens a schedule from a file (with the ending .sch) and returns a schedule object.
    '''
    @staticmethod
    def open(filepath):
        ret = Schedule()
        d = open(filepath, 'r').readlines()

        # print(d[1::2])

        for day_index, classes in enumerate(d[1::2]):

            for day_classes in classes.split(";"):
                day_classes = day_classes.replace('\n', '')
                if len(day_classes) > 0:
                    each_class = day_classes.split(";")
                    for _class in each_class:
                        name_index = _class.index(",")
                        class_name = _class[0:name_index]
                        time_sep = _class.index("-")
                        class_start = _class[time_sep - 5: time_sep]
                        class_end = _class[time_sep + 1: time_sep + 6]
                        ret.get_list()[day_index].append(Class(class_name, Time.from_str(class_start), Time.from_str(class_end)))
        return ret


if __name__ == "__main__":
    
    s = Schedule()
    s.monday.append(Class("Math"))
    s.monday.append(Class("French"))
    s.tuesday.append(Class("French"))

    print(s.tuesday[0].get_length())

    open("something.sch", "w+").write(str(s))

    z = str(Schedule.open("something.sch"))
    print(z)