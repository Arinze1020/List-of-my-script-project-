from tkinter import  *
from tkinter import ttk

class DISPLAY:


    def Massage(self):
        print('His the lord')

    def __init__(self,root):
        frame = Frame(root)
        frame.pack()






        self.button1 = ttk.Button(frame,text = 'click',command = self.Massage)
        self.button1.pack()

        self.button2 = ttk.Button(frame, text='QUIT',command = frame.quit)
        self.button2.pack()
root = Tk()
root.title(' U APP ')
Show = DISPLAY(root)

root.mainloop()

