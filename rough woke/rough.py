from tkinter import *

ari = Tk()
ari.title('U APP')
def num1():
    user_input = int(input())
    return user_input
def num2():
    user_input2 = int(input())
    return  user_input2
def sum1():
    x = num1() + num2()
    print(x)

button = Button(ari,text = 'input',command = num1)
button2 = Button(ari,text = 'sinput',command = num2)
buttonsum = Button(ari,text = 'OUT',command = sum1)
Quit = Button(ari,text = 'QUIT',command = Frame.quit)
#button.bind('<Button-1>',arinze)
button.pack()
button2.pack(side = RIGHT)
buttonsum.pack(side = LEFT)
Quit.pack()

ari.mainloop()












