import sys
from tkinter import *

root = Tk()
root.title('Text Editor')

N = input('Name:')
W = input('width:')
H = input('Height:')
S = input('Save Location:')

text=Text(root, width=W, height=H)
text.grid()

def close():
    exit()

def save():
    global text
    t = text.get("1.0", "end-1c")
    N=open(S , "w+")
    N.write(t)
    N.close()

menubar = Menu(root)

filemenu = Menu(menubar, tearoff=0)

filemenu.add_command(label="Save", command=save)
filemenu.add_command(label="Close", command=close)

menubar.add_cascade(label="File", menu=filemenu)

root.config(menu=menubar)

root.mainloop()
