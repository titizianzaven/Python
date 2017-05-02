from tkinter import *

root = Tk()
root.title('SpreedSheet')
root.geometry('600x110')

labela = Label(root, text="A").grid(row = 1,column = 2)
labelb = Label(root, text="B").grid(row = 1,column = 3)
labelc = Label(root, text="C").grid(row = 1,column = 4)

labeld = Label(root, text="1").grid(row = 2,column = 1)
labele = Label(root, text="2").grid(row = 3,column = 1)
labelf = Label(root, text="3").grid(row = 4,column = 1)

bara = Entry().grid(row = 2,column = 2)
barb = Entry().grid(row = 3,column = 2)
barc = Entry().grid(row = 4,column = 2)

bard = Entry().grid(row = 2,column = 3)
bare = Entry().grid(row = 3,column = 3)
barf = Entry().grid(row = 4,column = 3)

barg = Entry().grid(row = 2,column = 4)
barh = Entry().grid(row = 3,column = 4)
bari = Entry().grid(row = 4,column = 4)

root.mainloop()
