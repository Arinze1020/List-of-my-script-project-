from tkinter import *
import tkinter.messagebox
import sys

root = Tk()
root.title('U APP ')

#tkinter.messagebox.showinfo('windows ','am goin to get there soon than leter')
def option():

    QUIT = tkinter.messagebox.askquestion('QUIT','ARE YOU SURE YOU WANT TO EXIT')

    if QUIT == 'yes':
        sys.exit()
    elif QUIT == 'no':
     print('yes')

bottion1 = Button(root,text = 'QUIT',command = option)
bottion1.pack()


root.mainloop()
