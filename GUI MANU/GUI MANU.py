from tkinter import *
import sys
def file ():
    print("MY FILE")

def editi():
    print('editii')
def exit():
    sys.exit()

root = Tk()
root.title(' U APP ')
MAmenu = Menu(root)
root.config(menu = MAmenu)

FILE = Menu(MAmenu)
MAmenu.add_cascade(label = 'FILE',menu = FILE)
FILE.add_command(label = 'New',command = file)
FILE.add_separator()
FILE.add_command(label = 'exit',command = exit)

EDITI = Menu(MAmenu)
MAmenu.add_cascade(label = 'editi',menu = EDITI)
EDITI.add_command(label = 'cut',command = editi)

# ***** toolbar ******

TOOL = Frame(root,bg = 'black')

helpbutton = Button(TOOL,text = 'HELP',command = help)
helpbutton.pack(side = LEFT)
saechbutton = Button(TOOL,text = 'sreach',command = EDITI)
saechbutton.pack(side = LEFT )


# ***** statsbar ******

stats = Label(root,text = 'expression expected...',bd= 1 ,relief = SUNKEN ,anchor = W)
stats.pack(side = BOTTOM,fill = X)

TOOL.pack(side = TOP,fill = X)







root.mainloop()