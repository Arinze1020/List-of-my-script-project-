from tkinter import *
from tkinter import ttk



root = Tk()

root.title('U Calculator APP')
root.resizable(False,False)
root.configure(background = '#e1d869')


frame = ttk.Frame(root,padding =(2,2))
frame.pack()
style = ttk.Style()
#style.configure('TFrame',background = 'black')
#style.configure('TButton', background='black')


user_input = StringVar()
operator = ''



def mainpro(num):
    global operator
    operator = operator + str(num)
    user_input.set(operator)
def clear(num):
    global operator
    operator = operator + str('')
    user_input.set('')
def eques(num):
    global operator
    sump = str(eval(operator))
    user_input.set(sump)
    operator = ''







entry = ttk.Entry(frame,width = 20,font=('arial',20,'bold'),text = user_input,
                                justify = CENTER )
entry.grid(columnspan = 4)
#==========================================================
b7 = ttk.Button(frame,text ='7',command=lambda:mainpro(7))
b7.grid(row = 1,column = 0)
b8 = ttk.Button(frame, text='8',command=lambda:mainpro(8))
b8.grid(row=1, column=1)
b9 = ttk.Button(frame, text='9',command=lambda:mainpro(9))
b9.grid(row=1, column=2)
bmult = ttk.Button(frame, text='*',command=lambda:mainpro('*'))
bmult.grid(row=1, column=3)
# ==========================================================
b4 = ttk.Button(frame, text='4',command=lambda:mainpro(4))
b4.grid(row=2, column=0)
b5 = ttk.Button(frame, text='5',command=lambda:mainpro(5))
b5.grid(row=2, column=1)
b6 = ttk.Button(frame, text='6',command=lambda:mainpro(6))
b6.grid(row=2, column=2)
badd = ttk.Button(frame, text='+',command=lambda:mainpro('+'))
badd.grid(row=2, column=3)
# ==========================================================
b1 = ttk.Button(frame, text='1',command=lambda:mainpro(1))
b1.grid(row=3, column=0)
b2 = ttk.Button(frame, text='2',command=lambda:mainpro(2))
b2.grid(row=3, column=1)
b3 = ttk.Button(frame, text='3',command=lambda:mainpro(3))
b3.grid(row=3, column=2)
bdiv = ttk.Button(frame, text='/',command=lambda:mainpro('/'))
bdiv.grid(row=3, column=3)
# ==========================================================
bcan = ttk.Button(frame, text='C',command=lambda:clear('C'))
bcan.grid(row=4, column=0)
b0 = ttk.Button(frame, text='0',command=lambda:mainpro(0))
b0.grid(row=4, column=1)
bequ = ttk.Button(frame, text='=',command=lambda:eques('='))
bequ.grid(row=4, column=2)
bedot = ttk.Button(frame, text='.',command=lambda:mainpro('.'))
bedot.grid(row=4, column=3)

root.mainloop()