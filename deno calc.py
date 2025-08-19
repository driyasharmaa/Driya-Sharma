from tkinter import * 
from tkinter import messagebox 
from PIL import Image, ImageTk 

# Setting up Main Window 
root = Tk()
root.title('Denomination Counter')
root.configure(bg='light blue')
root.geometry('650x400')

# Adding Image and Labels in the Main Window
upload = Image.open("app_img.jpg")
# Resize the image using resize() method
upload = upload.resize((300, 300))
image = ImageTk.PhotoImage(upload)
label = Label (root, image=image, bg='light blue')
label .place(x=180, y=20)

