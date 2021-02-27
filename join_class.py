import sys
from .class_info import *
import webbrowser as wb 
import keyboard



def join_zoom_class(in_class : ZoomClass):
    pass

def join_google_meet(in_class : MeetClass):

    chrome_dir = ''
    path = str(sys.path).split(';')
    for path_item in path:
        if "chrome" in path.lower():
            chrome_dir = path_item
            break

    wb.BackgroundBrowser(chrome_dir).open_new_tab(in_class.google_meet_link)

def leave_google_meet():

    keyboard.send("CTRL+W")