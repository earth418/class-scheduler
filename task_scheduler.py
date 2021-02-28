import os
from join_class import *
from schedule import Schedule

def create_task(schedule : Schedule):
    task_name = "Class Scheduler Task"
    
    f = open("current_schedule.sch", "w+")
    f.write(str(schedule))
    current_dir = os.getcwd()

    # Calls Microsoft's Task Creation; task name     schedule   what days it'll run       What task it'll run         Start/end times 
    os.system(rf'SchTasks /Create  /TN "{task_name}" /SC DAILY /D MON, TUE, WED, THU, FRI /TR "py {current_dir}/task_scheduler.py" /ST 08:30 /ET 14:00').read()
    
if __name__ == "__main__":

    sch = Schedule.open("current_schedule.sch")