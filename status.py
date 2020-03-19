from tkinter import *

root = Tk()
root.title("Hello World!")
#root.geometry("400x400")
root.iconbitmap('c:/guis/codemy.ico')

# Define our fake command
def fake_command():
	pass

def new():
	hide_menu_frames()
	current_status.set("File Status")
	file_frame.grid(row=0, column=0, columnspan=2, padx=20, pady=20)

def cut():
	hide_menu_frames()
	current_status.set("Cut Status")
	edit_frame.grid(row=0, column=0, columnspan=2, padx=20, pady=20)	

def hide_menu_frames():
	edit_frame.grid_forget()
	file_frame.grid_forget()

#Define a Menu
my_menu = Menu(root)
root.config(menu=my_menu)

#Create Menu Items
file_menu = Menu(my_menu)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

# Create another submenu Edit
edit_menu = Menu(my_menu)
my_menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut", command=cut)
edit_menu.add_command(label="Copy", command=fake_command)
edit_menu.add_command(label="Paste", command=fake_command)



# File Menu Frame
file_frame = Frame(root, width=400, height=400, bd=5, bg="blue", relief="sunken")
#file_frame.grid(row=1, column=0, columnspan=2, padx=20, pady=20)

file_frame_label = Label(file_frame, text="File Frame", font=("Helvetica", 20))
file_frame_label.pack(padx=20, pady=20)


# Edit Menu Frame
edit_frame = Frame(root, width=400, height=400, bd=5, bg="blue", relief="sunken")
#file_frame.grid(row=1, column=0, columnspan=2, padx=20, pady=20)

edit_frame_label = Label(edit_frame, text="Cut Frame", font=("Helvetica", 20))
edit_frame_label.pack(padx=20, pady=20)

current_status = StringVar()
current_status.set("Waiting")

my_status = Label(root, textvariable=current_status, bd=1, relief="sunken", width=56, anchor=E)
my_status.grid(row=1, column=0)


root.mainloop()