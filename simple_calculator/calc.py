operator = ''
from tkinter import *
from tkinter import ttk


class calcu:





    def __init__(self,perent):


        user = StringVar()


        def mainpro(num):
            global operator
            operator = operator + str(num)
            user.set(operator)
        def clear(num):
            global operator
            operator = operator + str('')
            user.set('')
            operator = ''

        def eques(num):
            global operator
            sumup = str(eval(operator))
            user.set(sumup)
            operator = ''



        self.frame = ttk.Frame(perent, padding=(2, 2))
        self.frame.pack()
        self.style = ttk.Style()
        # self.style.configure('TFrame',background = 'black')
        # self.style.configure('TButton', background='black')

        self.entry = ttk.Entry(self.frame, width=20, font=('arial', 20, 'bold'),text = user,
                               justify=CENTER)
        self.entry.grid(columnspan=4)
        # ==========================================================
        self.b7 = ttk.Button(self.frame, text='7',command = lambda:mainpro(7))
        self.b7.grid(row=1, column=0)
        self.b8 = ttk.Button(self.frame, text='8',command = lambda:mainpro(8))
        self.b8.grid(row=1, column=1)
        self.b9 = ttk.Button(self.frame, text='9',command = lambda:mainpro(9))
        self.b9.grid(row=1, column=2)
        self.bmult = ttk.Button(self.frame, text='*',command = lambda:mainpro('*'))
        self.bmult.grid(row=1, column=3)
        # ==========================================================
        self.b4 = ttk.Button(self.frame, text='4',command = lambda:mainpro(4))
        self.b4.grid(row=2, column=0)
        self.b5 = ttk.Button(self.frame, text='5',command = lambda:mainpro(5))
        self.b5.grid(row=2, column=1)
        self.b6 = ttk.Button(self.frame, text='6',command = lambda:mainpro(6))
        self.b6.grid(row=2, column=2)
        self.badd = ttk.Button(self.frame, text='+',command = lambda:mainpro('+'))
        self.badd.grid(row=2, column=3)
        # ==========================================================
        self.b1 = ttk.Button(self.frame, text='1',command = lambda:mainpro(1))
        self.b1.grid(row=3, column=0)
        self.b2 = ttk.Button(self.frame, text='2',command = lambda:mainpro(2))
        self.b2.grid(row=3, column=1)
        self.b3 = ttk.Button(self.frame, text='3',command = lambda:mainpro(3))
        self.b3.grid(row=3, column=2)
        self.bdiv = ttk.Button(self.frame, text='/',command = lambda:mainpro('/'))
        self.bdiv.grid(row=3, column=3)
        # ==========================================================
        self.bcan = ttk.Button(self.frame, text='C',command = lambda:clear('C'))
        self.bcan.grid(row=4, column=0)
        self.b0 = ttk.Button(self.frame, text='0',command = lambda:mainpro(0))
        self.b0.grid(row=4, column=1)
        self.bequ = ttk.Button(self.frame, text='=',command = lambda:eques('='))
        self.bequ.grid(row=4, column=2)
        self.bedot = ttk.Button(self.frame, text='.',command = lambda:mainpro('.'))
        self.bedot.grid(row=4, column=3)
def main():
    root = Tk()
    show = calcu(root)

    root.mainloop()
if __name__=='__main__':main()