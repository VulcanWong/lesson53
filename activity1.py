from tkinter import *
from PIL import Image, ImageTK

root = Tk()
root.title('image')
root.geometry('400x400')

upload = Image.open("img.jpeg")

image = ImageTK.PhotoImage(upload)

label = Label(root, image=image, height=350, width=350)
label.place(x=50, y=50)
label2 = Label(root, text="This is how you add image in Tkinter Window")
label2.place(x=40, y=360)

root.mainloop()