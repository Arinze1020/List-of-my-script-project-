
from tkinter import *

root = Tk()
root.title('u app')
Tfram = Frame(root)
Tfram.pack(side = TOP)
Bfram = Frame(root)
Bfram.pack(side = RIGHT)
Bott1 = Button(Tfram,text = 'click 1',fg ='red')
Bott2 = Button(Bfram,text = 'next')
Bott3 = Button(Tfram,text = 'click2',fg = 'blue')
Bott1.pack(side = LEFT)
Bott2.pack(side = RIGHT)
Bott3.pack(side = LEFT)




root.mainloop()




a = -3

print (abs(a))