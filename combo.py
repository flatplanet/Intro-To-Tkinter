from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Hello World!")
root.geometry("400x400")
root.iconbitmap('c:/guis/codemy.ico')



#Create Select function
def select():
	if my_combo.get() == "Monday":
		my_label = Label(root, text="You Clicked Monday!").pack(pady=10)
	if my_combo.get() == "Tuesday":
		my_label = Label(root, text="You Clicked Tuesday!").pack(pady=10)
	if my_combo.get() == "Wednesday":
		my_label = Label(root, text="You Clicked Wednesday!").pack(pady=10)

# Combo Boxes
options = [
	"Monday",
	"Tuesday",
	"Wednesday",
]

my_combo = ttk.Combobox(root, value=options)
my_combo.current(0)
my_combo.pack(pady=10)

my_button = Button(root, text="Select", command=select).pack()



root.mainloop()