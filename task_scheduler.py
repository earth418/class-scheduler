# import time, pythoncom, win32api
# import win32com #.taskscheduler import taskscheduler

# task_name = 'Class_Scheduler'

# scheduler = win32com.client.Dispatch('Schedule.Service')
# scheduler.Connect()

# root_folder = scheduler.GetFolder('\\')
# task_def = scheduler.NewTask(0)

# # Create the Trigger

import os

task_name = ''

current_dir = os.getcwd()

os.system(rf'''SchTasks /Create 
    /TN "{task_name}"               # Task name
    /SC DAILY                       # Run every day
    /D MON, TUE, WED, THU, FRI      # only on days Mon-Fri
    /TR "{current_dir}/run.bat"     # Program will compile into an .exe; replace with that.
    /ST 08:30                       # Start at 8:30 am
    /ET 14:00                       # End at 2:00 pm
    ''').read()