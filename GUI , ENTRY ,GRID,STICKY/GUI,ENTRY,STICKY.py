from tkinter import  *


class DISPLAY:


    def Massage(self):
        print('His the lord')

    def __init__(self,root):
        frame = Frame(root)
        frame.pack()






        self.button1 = Button(frame,text = 'click',command = self.Massage)
        self.button1.pack()

        self.button2 = Button(frame, text='QUIT',command = frame.quit)
        self.button2.pack()




root = Tk()
root.title(' U APP ')
Show = DISPLAY(root)

root.mainloop()

