from tkinter import *

from tkinter import *

root = Tk()
root.title('u app')
lable_1 = Label(root,text ='Name')
lable_2 = Label(root,text='password')

entry_1 = Entry(root)
entry_2 = Entry(root)

lable_1.grid(row=0)
lable_2.grid(row=1)

entry_1.grid(colum = 1)
entry_2.grid(colum = 1)

root.mainloop()
