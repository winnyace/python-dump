# I think this is some test I did some time ago idk

import tkinter

def getInput():
    input = entry.get()
    lbl.config(text=input)

root = tkinter.Tk()

entry = tkinter.Entry(root)
entry.pack()

lbl = tkinter.Label(root, text='')
lbl.pack()

btn = tkinter.Button(root, text='submit', command=getInput)
btn.pack()

root.mainloop()
