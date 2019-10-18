from tkinter import *
from tkinter import ttk
class lord:
    def ans(self):
        self.label.config(text = 'MY LORD JESUS CHRIST.')
    def prev(self):
        self.label.config(text = 'who is you GOD ?')
    def __init__(self,ari):

        self.frame = ttk.Frame(ari)
        self.frame.pack()
        self.label = ttk.Label(self.frame,text = 'who is you GOD ?')
        self.label.grid(row = 0,column = 0,columnspan = 2)

        self.button = ttk.Button(self.frame,text = 'ANS',command = self.ans)
        self.button.grid(row = 1,column = 0)
        self.button2 = ttk.Button(self.frame, text='qus', command=self.prev)
        self.button2.grid(row = 1,column = 1)
        self.button3 = ttk.Button(self.frame, text='QUIT',command = self.frame.quit)
        self.button3.grid(row = 2, column = 0,columnspan = 2 )
root = Tk()
show = lord(root)
root.mainloop()
