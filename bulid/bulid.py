from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import time
import datetime
root = Tk()
root.title('  ONLINE ORDERING SERVICE. ')


class order:
    def __init__(self, master):
        self.fream = ttk.Frame(master)
        self.fream.pack(side=TOP)
        self.fream1 = ttk.Frame(master)
        self.fream1.pack(side=LEFT)
        self.fream2 = ttk.Frame(master)
        self.fream2.pack(side=RIGHT)
####################fream1#############################
        self.fream1top = ttk.Frame(self.fream1)
        self.fream1top.pack(side = TOP)

        self.fream1bottom = ttk.Frame(self.fream1)
        self.fream1bottom.pack(side=BOTTOM)
###################fram2##################################
        self.fream2top = ttk.Frame(self.fream2)
        self.fream2top.pack(side = TOP)

        self.fream2bottom = ttk.Frame(self.fream2)
        self.fream2bottom.pack(side = BOTTOM)
        ##################################3variable#############################################

        CustomerPhoneNum = StringVar()
        CustomerName = StringVar()
        CustomerEmail = StringVar()
        Qeans = StringVar()
        Cjeans = StringVar()
        Qpolo = StringVar()
        Cpolo = StringVar()
        Qothers = StringVar()
        Cothers = StringVar()
        DateOfOrder = StringVar()
        TimeOfOrder = StringVar()
        CustomarRef = StringVar()
        Total = StringVar()

        Qeans .set(0)
        Cjeans .set(0)
        Qpolo .set(0)
        Cpolo.set(0)
        Qothers .set(0)
        Cothers .set(0)
        DateOfOrder .set(time.strftime('%d-%m-%y'))
        TimeOfOrder .set(time.strftime('%H:%M:%S'))
        CustomarRef .set(0)
        Total .set(0)
        ###################################funtions#############################################

        def Exit():
            qquit = messagebox.askyesno(title ='Orderin System' ,message =  'Do you want to exit')
            if qquit>0:
                root.destroy()

        def reset():
            CustomerPhoneNum . set('')
            CustomerName .set('')
            CustomerEmail . set('')
            Qeans . set('')
            Cjeans . set('')
            Qpolo . set('')
            Cpolo .set('')
            Qothers . set('')
            Cothers . set('')
            DateOfOrder . set('')
            TimeOfOrder . set('')
            CustomarRef . set('')
            Total . set('')







        self.label = ttk.Label(self.fream, text='        Online Ordering System          ', justif=CENTER,

                               font=('courier', 30, 'bold')).pack(side=TOP)
        #########################################frram1###############################################

        self.label = ttk.Label(self.fream1top, text='Customer Name',
                               font=('courier', 12, 'bold')).grid(row=0, column=0, sticky=E)

        self.entryName = ttk.Entry(self.fream1top, width=30, font=('courier', 16, 'bold'),textvariable = CustomerName).grid(row=0, column=1,pady=5)
        self.label = ttk.Label(self.fream1top, text='Customer Phone Num',
                               font=('courier', 12, 'bold')).grid(row=1, column=0)
        self.entryPhone = ttk.Entry(self.fream1top, width=30, font=('courier', 16, 'bold'),textvariable = CustomerPhoneNum).grid(row=1, column=1,pady=5)
        self.label = ttk.Label(self.fream1top, text='Customer Email',
                               font=('courier', 12, 'bold')).grid(row=2, column=0, sticky=E)
        self.entryEmail = ttk.Entry(self.fream1top, width=30, font=('courier', 16, 'bold'),textvariable=CustomerEmail).grid(row=2, column=1,pady=5)
        #########################################fream1 - 2#######################################

        self.labetem = ttk.Label(self.fream1bottom, text='Item   ',
                                 font=('courier', 16, 'bold')).grid(row=3, column=0, sticky=W)
        self.labeQty = ttk.Label(self.fream1bottom, text='    Qty ',
                                 font=('courier', 16, 'bold')).grid(row=3, column=1, sticky=W)
        self.labecost = ttk.Label(self.fream1bottom, text=' Cost of Item',
                                  font=('courier', 16, 'bold')).grid(row=3, column=2, sticky=W)

        self.labeljens = ttk.Label(self.fream1bottom, text='Jeans',
                                   font=('courier', 12, 'bold')).grid(row=4, column=0, sticky=W)
        self.entryQjeans = ttk.Entry(self.fream1bottom, width=15,textvariable = Qeans, font=('courier', 16, 'bold')).grid(row=4, column=1,
                                                                                               sticky=W,padx=5,)
        self.entryCjeans = ttk.Entry(self.fream1bottom, width=15,textvariable = Cjeans, font=('courier', 16, 'bold')).grid(row=4, column=2,
                                                                                               sticky=W,pady=5)
        self.labePolo = ttk.Label(self.fream1bottom, text='Polo',
                                  font=('courier', 12, 'bold')).grid(row=5, column=0, sticky=W)
        self.entryQpolo = ttk.Entry(self.fream1bottom, width=15,textvariable = Qpolo, font=('courier', 16, 'bold')).grid(row=5, column=1, sticky=W,padx=5)
        self.entryCpolo = ttk.Entry(self.fream1bottom, width=15,textvariable = Cpolo ,font=('courier', 16, 'bold')).grid(row=5, column=2, sticky=W,pady=5)

        self.labeOthers = ttk.Label(self.fream1bottom, text='Others',
                                    font=('courier', 12, 'bold')).grid(row=6, column=0, sticky=W)
        self.entryQothers = ttk.Entry(self.fream1bottom, width=15,textvariable = Qothers, font=('courier', 16, 'bold')).grid(row=6, column=1,
                                                                                                sticky=W,padx=5)
        self.entryCothers = ttk.Entry(self.fream1bottom, width=15,textvariable = Cothers, font=('courier', 16, 'bold')).grid(row=6, column=2,
                                                                                                sticky=W,pady=5)

        ############################################fream 1###################################################
        self.label = ttk.Label(self.fream2top,text = 'Date Of Order',font=('courier', 12, 'bold')).grid(row = 0,column = 0)
        self.entry_date_of_order = ttk.Entry(self.fream2top,textvariable =DateOfOrder  ,width = 30,font=('courier', 16, 'bold')).grid(row = 0,column = 1,pady=5)

        self.label= ttk.Label(self.fream2top, text='Time Of Order', font=('courier', 12, 'bold')).grid(
            row=2, column=0)
        self.entry_time_of_order = ttk.Entry(self.fream2top, textvariable=TimeOfOrder, width=30,
                                             font=('courier', 16, 'bold')).grid(row=2, column=1,pady=5)
        self.label = ttk.Label(self.fream2top, text=' Customar Ref ', font=('courier', 12, 'bold')).grid(row = 3,column = 0 )
        self.entry_customar_ref  = ttk.Entry(self.fream2top, textvariable = CustomarRef , width=30,
                                             font=('courier', 16, 'bold')).grid(row=3, column=1,pady=5)
        #########################################FREAM 1 2 ################################################################################

        self.label_mathod_of_payment = ttk.Label (self.fream2bottom,text = 'Mathod of payment ',font=('courier', 12, 'bold')).grid(row = 0,column = 0)
        self.combox = ttk.Combobox(self.fream2bottom,font=('courier',10, 'bold'))
        self.combox['value'] = ('','cash','master card','Debit card','visa card')
        self.combox.grid(row=0, column=1,pady=5,sticky = W)

        self.label_Total = ttk.Label(self.fream2bottom,text = 'TOTAL',font=('courier', 12, 'bold')).grid(row = 1,column = 0)
        self.entry_Total = ttk.Entry(self.fream2bottom,textvariable = Total, font=('courier', 16, 'bold'),width = 20).grid(row = 1,column = 1,pady=5)

        #####################################button######################################################################################



        self.butTotal = Button(self.fream2bottom,text = 'Total',width = 20,height = 3,font=('courier', 10, 'bold'),relief = GROOVE).grid(row = 2,column = 0)
        self.butReset = Button(self.fream2bottom, text='Reset', width=20,height = 3,font=('courier', 10, 'bold'),relief = GROOVE,command = reset).grid(row=2, column=1)
        self.butExit = Button(self.fream2bottom, text='Exit', width=20,height = 3,font=('courier', 10, 'bold'),relief = GROOVE,command = Exit).grid(row=2, column=2)








dispay = order(root)

root.mainloop()