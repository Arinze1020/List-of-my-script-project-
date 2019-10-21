from tkinter import *
from tkinter import ttk
from tkinter import messagebox
class TRY_app:






    def __init__(self,TRY):
        self.frame1 = ttk.Frame(TRY)
        self.frame1.pack()

        self.style = ttk.Style()
        self.style.configure('TFrame',background = '#e1d8b9')
        self.style.configure('TButton',background = '#e1d8b9')
        self.style.configure('TLabel',background = '#e1d8b9',font = ('Arial',11,))
        self.style.configure('Header.TLabel',font = ('Arial',20,'bold'))

        self.label1 = ttk.Label(self.frame1,text = 'TRY THIS MY APPLICATION IS ALSOM!!!!',style = "Header.TLabel")
        self.label1.grid(row = 0,column = 0,columnspan = 3)
        self.label2 = ttk.Label(self.frame1,text = 'THIS APPLICATION IS ALBOUT GETTING THE INFOMSTION YOU YOU HAVE AND SUBMITING IT TO OU DATDBASE SYSTEM.')
        self.label2.grid(row = 1,column = 0,columnspan = 3)

        self.frame2 = ttk.Frame(TRY)
        self.frame2.pack()
        self.Nlabel = ttk.Label(self.frame2,text = 'Name').grid(row = 0,column = 0,sticky = W)
        self.Elabel = ttk.Label(self.frame2,text = 'Email').grid(row = 0,column = 1,sticky = W)
        self.Clabel = ttk.Label(self.frame2,text = 'Comments').grid(row = 2,column = 0,sticky = W)
        self.entry1 = ttk.Entry(self.frame2,width = 24,font=('Arial',10))
        self.entry1.grid(row=1,column=0,sticky = W)
        self.entry2 = ttk.Entry(self.frame2,width = 24,font=('Arial',10) )
        self.entry2.grid(row = 1,column = 1,sticky = W)
        self.comment = Text(self.frame2,width = 50,height = 10,font=('Arial',10))
        self.comment.grid(row = 3,column = 0,columnspan = 2)
        ttk.Button(self.frame2,text = 'submit',command = self.submit).grid(row = 4,column = 0,sticky = E)
        ttk.Button(self.frame2,text = 'clear',command = self.clear).grid(row = 4,column = 1,sticky = W)
    def submit(self):
        print('Name:{}'.format(self.entry1.get()))
        print('Email:{}'.format(self.entry2.get()))
        print('comment:{}'.format(self.comment.get(1.0,'end')))
        self.clear()
        messagebox.showinfo(title = 'feedback',message = 'your comment was submited')
    def clear(self):
        self.entry1.delete(0,'end')
        self.entry2 .delete(0,'end')
        self.comment .delete(1.0,'end')
root = Tk()
root.title('TRY APP')
root.resizable(False,False)
root.configure(background = '#e1d8b9')
show = TRY_app(root)
root.mainloop()