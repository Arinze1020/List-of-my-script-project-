from tkinter import *
from tkinter import ttk
class ENG_APP:

    def __init__(self,master):
        self.frame = ttk.Frame(master)
        self.frame.pack()
        self.label = ttk.Label(self.frame,text = 'All Engineering formulas',justify = CENTER,font = ('Courier',13,'bold')).grid(row = 0,column = 0,columnspan = 2)

        self.main_frame = ttk.Frame(master)
        self.main_frame.pack()

        button = ttk.Button(self.main_frame,text = 'LOGARITHMS')
        button.grid(row = 3,column = 0)
        ''''
        ttk.Button(self.main_frame, text='TRIGONOMETRY').grid(row = 4,column = 0)
        ttk.Button(self.main_frame, text='DERIVATIVES').grid(row = 5,column = 0)
        ttk.Button(self.main_frame, text='INTEGRATION').grid(row = 6,column = 0)
        ttk.Button(self.main_frame, text='LAPLACE').grid(row = 7,column = 0)
        ttk.Button(self.main_frame, text='FOURIER SERIES').grid(row = 8,column = 0)
        '''
        ''''
        ttk.Button(master, text='prev', command=self.prv).grid(row=1, column=2)
    def prebuton(self):
        self.label.config(text = '(a+c+v+b+e)')
    def prv(self):
        self.label.config(text='(a+b+e+f+s)')
        '''





root = Tk()

root.title('ENG APP')

app = ENG_APP(root)

root.mainloop()



