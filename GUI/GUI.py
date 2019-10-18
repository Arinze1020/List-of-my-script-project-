from tkinter import *
from tkinter import ttk

root = Tk()
root.title('U APP')
#root.state('zoomed')

entry = ttk.Entry(root)
entry.pack(side = LEFT)
entry.bind('<<Copy>>',lambda e:print('copy'))
entry.bind('<<Paste>>',lambda e:print('paste'))
entry.event_add('<<odd num>>')
entry.bind('<<odd num>>',lambda e:print('odd num'))






















''''
def num(num):
    print(num)

button = ttk.Button(root,text = '1',command = lambda :num(1))
button.pack()
'''
''''
def mouse_press(event):
    global prev
    prev = event
    print('type:{}'.format(event.type))
    print('widget:{}'.format(event.widget))
    print('num:{}'.format(event.num))
    print('x:{}'.format(event.x))
    print('y:{}'.format(event.y))
    print('x_root:{}'.format(event.x_root))
    print('y_root:{}'.format(event.y_root))

canves = Canvas(root,width = 300,height = 400,background= 'red')
canves.pack()
#def shortcut(action):
    #print(action)

def draw(event):
    global prev
    canves.create_line(prev.x,prev.y,event.x,event.y,width = 6)
    prev = event
canves.bind('<ButtonPress>',mouse_press)
canves.bind('<B1-Motion>',draw)
'''
''''
treeview = ttk.Treeview(root)
treeview.pack()
treeview.insert('','0','item',text = 'item')
treeview.insert('','2','item2',text = 'item2')
treeview.insert('','1','item1')

button = ttk.Button(treeview)
button.pack()
treeview.insert('item2','1','button',text = 'button')
'''
'''
text = Text(root,width = 30,height = 10)
text.config(wrap='word')
text.insert('1.0 + 1 lines','this we apper')
text.tag_add('my','1.3','1.4')
text.tag_configure('my',background='red')
text.insert('insert','_')
text.pack()
note = ttk.Notebook(root)
note.pack()
frame1 = ttk.Frame(note)
frame2 = ttk.Frame(note)

note.add(frame1,text = 'one')
note.add(frame2,text = 'two')
button = ttk.Button(frame1,text = 'click me')
button.pack()
'''
root.mainloop()