from tkinter import *

root = Tk()
root.geometry("400x400")

def show():
	my_label = Label(root, text=v.get()).pack()

#Radio
v = StringVar()
v.set("two")

Radiobutton(root, text="One", variable=v, value="one").pack()
Radiobutton(root, text="Two", variable=v, value="two").pack()

my_button = Button(root, text="select", command=show).pack()


#CheckBox #######################################################

def check():
	label = Label(root, text=var.get()).pack()

#var = IntVar()
#c = Checkbutton(root, text="Expand", variable=var)
#c.pack()

var = StringVar()
c = Checkbutton(root, text="Expand", variable=var, onvalue="pizza", offvalue="hello")
c.deselect()
c.pack()

two_button = Button(root, text='check', command=check).pack()

# POPUP###############################
from tkinter import messagebox
def pop():
	messagebox.showinfo("Title", "Hello World!")

pop_button = Button(root, text="Popup", command=pop).pack()

mainloop()