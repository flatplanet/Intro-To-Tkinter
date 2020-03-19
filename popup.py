from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Hello World!")
root.geometry("400x400")
root.iconbitmap('c:/guis/codemy.ico')

# Create Popup function
def popup():
	response = messagebox.showinfo("Popup Title", "Look at my popup message!!")
	my_label = Label(root, text=response).pack(pady=10)

	'''
	if response == 1:
		my_label = Label(root, text="you clicked yes!").pack(pady=10)		
	else:
		my_label = Label(root, text="you clicked no!").pack(pady=10)		
	'''

# Popup Boxes
# showinfo, showwarning, showerror, askquestion, askokcancel, askyesno

pop_button = Button(root, text="Click To Pop Up!", command=popup)
pop_button.pack(pady=20)




root.mainloop()