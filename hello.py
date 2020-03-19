from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Hello World!")
root.geometry("400x900")
root.iconbitmap('c:/guis/codemy.ico')

# Create clicked function

def clicked():
	input = e.get()
	my_label2 = Label(root, text="Hello " + input)
	my_label2.pack()


# Add Images
my_image = ImageTk.PhotoImage(Image.open("aspen.png"))
image_label = Label(image=my_image)
image_label.pack()

# Create labels
my_label = Label(root, text='Enter Your Name:')
my_label.pack()

#Create Entry Widget Input Box
e = Entry(root, font=("Helvetica", 18))
e.pack(pady=20)


# Create Buttons
my_button = Button(root, text="Click Me!", command=clicked)
my_button.pack(pady=20)














root.mainloop()