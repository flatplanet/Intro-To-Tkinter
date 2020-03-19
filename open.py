from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk()
root.title("Hello World!")
root.geometry("500x700")
root.iconbitmap('c:/guis/codemy.ico')

# Create open dialog box function
def open_image():
	#Open File Dialog Box
	root.filename = filedialog.askopenfilename(initialdir='/guis', title="Open An Image File", filetypes=( ("PNG File", "*.png"), ("All Files", "*.*") ))
	#my_label = Label(root, text=root.filename).pack(pady=10)
	global my_img
	# Open image and place on screen
	my_img = ImageTk.PhotoImage(Image.open(root.filename))
	img_label = Label(root, image=my_img)
	img_label.pack(pady=10)


my_button = Button(root, text="Open Image", command=open_image).pack(pady=10)


root.mainloop()