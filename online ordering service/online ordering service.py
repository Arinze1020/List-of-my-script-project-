
from tkinter import *
from tkinter import ttk



class calcu:

    def __init__(self,master):

        self.fream = ttk.Frame(master)
        self.fream.pack(side = TOP)
        self.fream1 = ttk.Frame(master)
        self.fream1.pack(side = LEFT)
        self.fream2 = ttk.Frame(master)
        self.fream2.pack(side=RIGHT)
        self.fream1top= ttk.Frame(self.fream1)
        self.fream1top.pack(side = TOP)
        self.fream12 = ttk.Frame(self.fream1)
        self.fream12.pack()
       
        self.label  = ttk.Label(self.fream,text = '        Online Ordering System          ',justif = CENTER,

                                font = ('courier',20,'bold')).pack(side = TOP)

#########################################frram1###############################################

        self.label = ttk.Label(self.fream1, text='Customer Name',
                               font=('courier',12, 'bold')).grid(row = 0,column = 0,sticky = W)
        
        self.entryName = ttk.Entry(self.fream1,width = 30, font = ('courier',10,'bold')).grid(row = 0,column = 1)
        self.label = ttk.Label(self.fream1, text='Customer Phone Num',
                               font=('courier',12, 'bold')).grid(row = 1,column = 0)
        self.entryPhone = ttk.Entry(self.fream1, width=30, font = ('courier',10,'bold')).grid(row=1, column=1)
        self.label = ttk.Label(self.fream1, text='Customer Email',
                               font=('courier',12, 'bold')).grid(row = 2,column = 0,sticky = W)
        self.entryEmail = ttk.Entry(self.fream1, width=30, font = ('courier',10,'bold')).grid(row=2, column=1)
#########################################fream1 - 2#######################################

        self.labetem = ttk.Label(self.fream1, text='Itemorder',
                               font=('courier',16, 'bold')).grid(row=3, column=0,sticky = W)
        self.labeQty= ttk.Label(self.fream1, text='Qty',
                                 font=('courier', 16, 'bold')).grid(row=3, column=1,sticky = W)
        self.labecost= ttk.Label(self.fream1, text='Cost of Item',
                                 font=('courier', 16, 'bold')).grid(row=3, column=2,sticky = W)

        self.labeljens = ttk.Label(self.fream1, text='Jeans',
                               font=('courier', 12, 'bold')).grid(row=4, column=0,sticky = W)
        self.entryQjeans = ttk.Entry(self.fream1, width=10, font=('courier', 16, 'bold')).grid(row=4, column=1,sticky = W)
        self.entryCjeans = ttk.Entry(self.fream1, width=10, font=('courier', 16, 'bold')).grid(row=4, column=2,sticky = W)
        self.labePolo = ttk.Label(self.fream1, text='Polo',
                               font=('courier', 12, 'bold')).grid(row=5, column=0,sticky = W)
        self.entryQpolo = ttk.Entry(self.fream1, width=10, font=('courier', 16, 'bold')).grid(row=5, column=1,sticky = W)
        self.entryCpolo = ttk.Entry(self.fream1, width=10, font=('courier', 16, 'bold')).grid(row=5, column=2,sticky = W)

        self.labeOthers = ttk.Label(self.fream1, text='Others',
                                  font=('courier', 12, 'bold')).grid(row=6, column=0,sticky = W)
        self.entryQothers = ttk.Entry(self.fream1, width=10, font=('courier', 16, 'bold')).grid(row=6, column=1,sticky = W)
        self.entryCothers = ttk.Entry(self.fream1, width=10, font=('courier', 16, 'bold')).grid(row=6, column=2,sticky = W)



def main():
    root = Tk()

    show = calcu(root)




    root.mainloop()
if __name__ == '__main__':main()


