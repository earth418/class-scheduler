import os
from class_info import Time
from schedule import Schedule

def create_task(schedule : Schedule):

    first_class, last_class = Time(), Time()
    for day in schedule:
        first_class = min(first_class, day[0].start_time)
        last_class = max(last_class, day[-1].end_time)

    task_name = "Class Scheduler Task"
    
    f = open("current_schedule.sch", "w+")
    f.write(str(schedule))
    current_dir = os.getcwd()

    # Calls Microsoft's Task Creation; task name     schedule   what days it'll run       What task it'll run         Start/end times 
    os.system(rf'SchTasks /Create  /TN "{task_name}" \
    /SC DAILY /D MON, TUE, WED, THU, FRI /TR "py {current_dir}/task_scheduler.py" \
    /ST {str(first_class)} /ET {str(last_class)}').read()
    
if __name__ == "__main__":

    sch = Schedule.open("current_schedule.sch")

    sch.clear()

    print(sch)