import sys
from Tkinter import *
import tkFileDialog

root = Tk()
root.title('Text Editor')

W = input('width:')
H = input('Height:')

text=Text(root, width=W, height=H)
text.grid()

def close():
    exit()

def saveas():
    global text
    t = text.get("1.0", "end-1c")
    savelocation= tkFileDialog.asksaveasfilename()
    file1=open(savelocation, "w+")
    file1.write(t)
    file1.close()

def FontHelvetica():
    global text
    text.config(font="Helvetica")

def FontArial():
    global text
    text.config(font="Arial")  

menubar = Menu(root)

filemenu = Menu(menubar, tearoff=0)
fontmenu = Menu(menubar, tearoff=0)
layoutmenu = Menu(menubar, tearoff=0)

filemenu.add_command(label="Save as", command=saveas)
filemenu.add_command(label="Close", command=close)

fontmenu.add_command(label="Arial", command=FontArial)
fontmenu.add_command(label="Helvetica", command=FontHelvetica)

menubar.add_cascade(label="File", menu=filemenu)
menubar.add_cascade(label="Fonts", menu=fontmenu)

root.config(menu=menubar)

root.mainloop()