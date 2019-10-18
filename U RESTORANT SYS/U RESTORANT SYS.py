from tkinter import  *
from tkinter import ttk
import time
import  random

root = Tk()
root.title('U RESTORANT SYS')

root.configure(background = 'powder blue')


style = ttk.Style()
style.configure('TFrame',background = 'powder blue')
style.configure('TButton', background='powder blue',font = ('Arial',12,'bold'))
style.configure('TLabel', background='powder blue')
style.configure('Total.TButton', background='powder blue',font = ('Arial',16,'bold'))


# creating frames
frame1 = ttk.Frame(root,width = 800,height = 50)
frame1.pack(side = TOP)
frame2 = ttk.Frame(root,width = 800,height = 50)
frame2.pack(side = LEFT)

frame = ttk.Frame(root,padding =(2,2))
frame.pack(side = RIGHT)
# TIME
TIME = time.asctime(time.localtime(time.time()))


label = ttk.Label(frame1,text = 'RESTAURANT MANAGEMENT SYSTEM',font = ('Arial',30,'bold'))
label.pack()
label1 = ttk.Label(frame1,text = TIME,font = ('Arial',20,'bold'))
label1.pack()




user_input = StringVar()
operator = ''

#================FUNTIONS=============================

def mainpro(num):
    global operator
    operator = operator + str(num)
    user_input.set(operator)
def clear(num):
    global operator
    operator = operator + str('')
    user_input.set('')
    operator = ''

def eques(num):
    global operator
    sump = str(eval(operator))
    user_input.set(sump)
    operator = ''

def Quit():
    root.destroy()
def Reset():
    referece.set('')
    Rice .set('')
    Akpu .set('')
    Beans .set('')
    Meat .set('')
    Refreshment.set('')
    Yam_beans.set('')
    Price_Yam_beans.set('')
    Price_refreshement.set('')
    Price_meat .set('')
    Price_Beans .set('')
    Price_Rice.set('')
    Price_Akpu.set('')
    Total .set('')

def Total_All():
    creat = random.randint(123495,455673)
    creatX = str(creat)
    referece.set(creatX)

    costRice = float(Rice.get())
    costAkpu = float(Akpu.get())
    costBeans = float(Beans.get())
    costMeat = float(Meat.get())
    costRefreshment = float(Refreshment.get())
    costYam_beans = float(Yam_beans.get())

    Price_Yam_beansA = costYam_beans * 200
    Price_refreshementA = costRefreshment * 150
    Price_meatA = costMeat * 100
    Price_BeansA = costBeans * 150
    Price_RiceA = costRice * 250
    Price_AkpuA = costAkpu * 250

    TotalA = str('%.2f'%(Price_Yam_beansA+Price_refreshementA+Price_meatA+Price_BeansA+ Price_RiceA+Price_AkpuA))
    Total.set(TotalA)

    Price_Yam_beans.set(Price_Yam_beansA)
    Price_refreshement.set(Price_refreshementA)
    Price_meat.set(Price_meatA)
    Price_Beans.set(Price_BeansA)
    Price_Rice.set(Price_RiceA)
    Price_Akpu.set(Price_AkpuA)








entry = ttk.Entry(frame,width = 29,font=('arial',20,'bold'),text = user_input,
                                justify = CENTER)
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

#========================rest-infor1====================================

referece = StringVar()
Rice = StringVar()
Akpu = StringVar()
Beans = StringVar()
Meat = StringVar()
Refreshment = StringVar()
Yam_beans = StringVar()
Price_Yam_beans = StringVar()
Price_refreshement = StringVar()
Price_meat = StringVar()
Price_Beans = StringVar()
Price_Rice = StringVar()
Price_Akpu = StringVar()
Total = StringVar()



libresf = ttk.Label(frame2,text = 'Referece',font = ('Arial',16,'bold'))
libresf.grid(row = 0,column = 0,sticky = E)
resfentry = ttk.Entry(frame2,width =15,font=('arial',16,'bold'),text = referece)
resfentry.grid(row = 0,column = 1)

libAkpu = ttk.Label(frame2,text = 'Akpu',font = ('Arial',16,'bold'))
libAkpu.grid(row = 1,column = 0,sticky = E)

Akpuentry = ttk.Entry(frame2,width =15,font=('arial',16,'bold'),text = Akpu)
Akpuentry.grid(row = 1,column = 1)

librice = ttk.Label(frame2,text = 'Rice',font = ('Arial',16,'bold'))
librice.grid(row = 2,column = 0,sticky = E)
riceentry = ttk.Entry(frame2,width =15,font=('arial',16,'bold'),text = Rice)
riceentry.grid(row = 2,column = 1)

libbeans = ttk.Label(frame2,text = 'Beans',font = ('Arial',16,'bold'))
libbeans.grid(row = 3,column = 0,sticky = E)
beansentry = ttk.Entry(frame2,width =15,font=('arial',16,'bold'),text = Beans)
beansentry .grid(row = 3,column = 1)

libmeat = ttk.Label(frame2,text = 'Meat',font = ('Arial',16,'bold'))
libmeat.grid(row = 4,column = 0,sticky = E)
meatentry = ttk.Entry(frame2,width =15,font=('arial',16,'bold'),text = Meat)
meatentry.grid(row = 4,column = 1)

librefrement = ttk.Label(frame2,text = 'Refreshement',font = ('Arial',16,'bold'))
librefrement.grid(row = 5,column = 0,sticky = E)
refremententry = ttk.Entry(frame2,width =15,font=('arial',16,'bold'),text = Refreshment)
refremententry.grid(row = 5,column = 1)

libyam_beans = ttk.Label(frame2,text = 'YamBeans',font = ('Arial',16,'bold'))
libyam_beans.grid(row = 6,column = 0,sticky = E)
Yam_beansentry = ttk.Entry(frame2,width =15,font=('arial',16,'bold'),text = Yam_beans)
Yam_beansentry.grid(row = 6,column = 1)

#====================rest-infor2 price========================

libAkpu_price = ttk.Label(frame2,text = 'Price',font = ('Arial',16,'bold'))
libAkpu_price.grid(row = 1,column = 2,sticky = E)
Akpu_price_entry = ttk.Entry(frame2,width =12,font=('arial',16,'bold'),text = Price_Akpu)
Akpu_price_entry.grid(row = 1,column = 3)

libRice_price = ttk.Label(frame2,text = 'Price',font = ('Arial',16,'bold'))
libRice_price.grid(row = 2,column = 2,sticky = E)
Rice_price_entry = ttk.Entry(frame2,width =12,font=('arial',16,'bold'),text = Price_Rice)
Rice_price_entry.grid(row = 2,column = 3)

libBeans_price = ttk.Label(frame2,text = 'Price',font = ('Arial',16,'bold'))
libBeans_price.grid(row = 3,column = 2,sticky = E)
Beans_price_entry = ttk.Entry(frame2,width =12,font=('arial',16,'bold'),text = Price_Beans)
Beans_price_entry.grid(row = 3,column = 3)

libMeat_price = ttk.Label(frame2,text = 'Price',font = ('Arial',16,'bold'))
libMeat_price.grid(row = 4,column = 2,sticky = E)
Meat_price_entry = ttk.Entry(frame2,width =12,font=('arial',16,'bold'),text = Price_meat)
Meat_price_entry.grid(row = 4,column = 3)

libRefrement_price = ttk.Label(frame2,text = 'Price',font = ('Arial',16,'bold'))
libRefrement_price.grid(row = 5,column = 2,sticky = E)
Referment_price_entry = ttk.Entry(frame2,width =12,font=('arial',16,'bold'),text = Price_refreshement)
Referment_price_entry.grid(row = 5,column = 3)


libYam_beans_price = ttk.Label(frame2,text = 'Price',font = ('Arial',16,'bold'))
libYam_beans_price.grid(row = 6,column = 2,sticky = E)
Yam_beans_price_entry = ttk.Entry(frame2,width =12,font=('arial',16,'bold'),text = Price_Yam_beans)
Yam_beans_price_entry.grid(row = 6,column = 3)

libTotal = ttk.Label(frame2,text = 'Total',font = ('Arial',16,'bold'))
libTotal.grid(row = 7,column = 1,columnspan = 2,sticky = W)
Total_entry = ttk.Entry(frame2,width =12,font=('arial',16,'bold'),text = Total)
Total_entry.grid(row = 7,column = 3,columnspan =2)

#========================Buttons========================

Tbutton = ttk.Button(frame2,text = 'Total',command =Total_All)
Tbutton.config(style = 'Total.TButton' )
Tbutton.grid(row = 8 , column = 1,sticky = E)

Rbutton = ttk.Button(frame2,text = 'Reset',command = Reset)
Rbutton.config(style = 'Total.TButton' )
Rbutton.grid(row = 8 , column = 2,sticky = W)

Qbutton = ttk.Button(frame2,text = 'Quit',command = Quit)
Qbutton.config(style = 'Total.TButton' )
Qbutton.grid(row = 8 , column = 3,sticky = W)


root.mainloop()