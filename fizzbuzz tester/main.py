import tkinter

def getInput():
    try:
        num = int(txtboxInput.get())
        fizzbuzz(num)
    except:
        lblResult.config(text='Not a number.')

def fizzbuzz(input):
    if input == 0:
        lblResult.config(text='Input is 0.')
    elif (input % 3 == 0) and (input % 5 == 0):
        lblResult.config(text='Fizzbuzz!')
    elif input % 3 == 0:
        lblResult.config(text='Fizz!')
    elif input % 5 == 0:
        lblResult.config(text='Buzz!')
    else:
        lblResult.config(text='Input is not a divisible by 3, nor 5.')

rootWindow = tkinter.Tk()
rootWindow.title('Fizzbuzz tester')
rootWindow.geometry('250x100')

lblWelcome = tkinter.Label(rootWindow, text='Please give me a number.')
lblWelcome.pack() 

txtboxInput = tkinter.Entry(rootWindow)
txtboxInput.pack()

btnSubmit = tkinter.Button(rootWindow, text='Submit', command=getInput)
btnSubmit.pack()

lblResult = tkinter.Label(rootWindow, text='')
lblResult.pack(side=tkinter.BOTTOM)

rootWindow.mainloop()
