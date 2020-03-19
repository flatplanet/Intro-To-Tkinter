from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Hello World!")
root.geometry("400x400")
root.iconbitmap('c:/guis/codemy.ico')

# Create second window function
def open_window():
	new = Toplevel()
	new.title("Second Window")
	new.geometry("500x700")
	new.iconbitmap('c:/guis/codemy.ico')
	

	my_label = Label(new, text="Look at my fancy second window!").pack(pady=20)

	my_img = ImageTk.PhotoImage(Image.open("aspen.png"))
	img_label = Label(new, image=my_img)
	img_label.pack(pady=5)



	destroy_button = Button(new, text="Quit", command=new.destroy)
	destroy_button.pack(pady=5)

	# Minimize Original Window
	#hide_button = Button(new, text="Hide Main Window", command=root.iconify)
	#show_button = Button(new, text="Show Main Window", command=root.deiconify)

	# Withdraw Original Window
	hide_button = Button(new, text="Hide Main Window", command=root.withdraw)
	show_button = Button(new, text="Show Main Window", command=root.deiconify)

	kill_original = Button(new, text="Quit Original", command=root.destroy).pack()
	hide_button.pack()
	show_button.pack()

	new.mainloop()

#Create New Windows
my_button = Button(root, text="Open 2nd Window", command=open_window).pack()






root.mainloop()