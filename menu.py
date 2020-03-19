from tkinter import *

root = Tk()
root.title("Hello World!")
root.geometry("400x400")
root.iconbitmap('c:/guis/codemy.ico')

# Define our fake command
def fake_command():
	pass

def hide():
	my_frame.grid_forget()

def show():
	my_frame.grid(row=1, column=0, columnspan=2, padx=20, pady=20)

#Define a Menu
my_menu = Menu(root)
root.config(menu=my_menu)

#Create Menu Items
file_menu = Menu(my_menu)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=fake_command)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

# Create another submenu Edit
edit_menu = Menu(my_menu)
my_menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut", command=fake_command)
edit_menu.add_command(label="Copy", command=fake_command)
edit_menu.add_command(label="Paste", command=fake_command)


show_button = Button(root, text="Show", command=show) 
hide_button = Button(root, text="Hide", command=hide) 

show_button.grid(row=0, column=0)
hide_button.grid(row=0, column=1)

my_frame = Frame(root, width=200, height=200, bd=5, bg="blue", relief="sunken")
my_frame.grid(row=1, column=0, columnspan=2, padx=20, pady=20)

frame_label = Label(my_frame, text="Hello World!", font=("Helvetica", 20))
frame_label.pack(padx=20, pady=20)

root.mainloop()