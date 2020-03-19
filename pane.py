from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.geometry("400x400")


pane1 = PanedWindow(bd=4, relief="raised", bg="red")
pane1.pack(fill=BOTH, expand=1)

left = Label(pane1, text="left pane")
pane1.add(left)

pane2 = PanedWindow(pane1, orient=VERTICAL, bd=4, relief="raised", bg="blue")
pane1.add(pane2)

top = Label(pane2, text="top pane")
pane2.add(top)

bottom = Label(pane2, text="bottom pane")
pane2.add(bottom)

'''
def new():
	news = Toplevel()
	my_img = ImageTk.PhotoImage(Image.open("aspen.png"))
	my_label = Label(news, image=my_img)
	#my_label.image = my_img
	my_label.pack()


	news.mainloop()
'''

#Button(root, text="Click", command=new).pack()
mainloop()