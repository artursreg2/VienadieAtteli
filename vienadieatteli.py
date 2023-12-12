from tkinter import *
from PIL import ImageTk, Image
import random 
from tkinter import messagebox
gamewindow=Tk()
gamewindow.title("Vienādie attēli")

myimg1=ImageTk.PhotoImage(Image.open("7.jpg"))
myimg2=ImageTk.PhotoImage(Image.open("2.jpg"))
myimg3=ImageTk.PhotoImage(Image.open("3.jpg"))
myimg4=ImageTk.PhotoImage(Image.open("4.jpg"))
myimg5=ImageTk.PhotoImage(Image.open("5.jpg"))
myimg6=ImageTk.PhotoImage(Image.open("6.jpg"))

bgImg=ImageTk.PhotoImage(Image.open("8.jpg"))



btn0 = Button(width=200, height=200, image=bgImg)
btn1 = Button(width=200, height=200, image=bgImg)
btn2 = Button(width=200, height=200, image=bgImg)
btn3 = Button(width=200, height=200, image=bgImg)
btn4 = Button(width=200, height=200, image=bgImg)
btn5 = Button(width=200, height=200, image=bgImg)
btn6 = Button(width=200, height=200, image=bgImg)
btn7 = Button(width=200, height=200, image=bgImg)
btn8 = Button(width=200, height=200, image=bgImg)
btn9 = Button(width=200, height=200, image=bgImg)
btn10 = Button(width=200, height=200, image=bgImg)


btn0.grid(row=0, column=0)
btn1.grid(row=0, column=1)
btn2.grid(row=0, column=2)
btn3.grid(row=0, column=3)
btn4.grid(row=0, column=4)
btn5.grid(row=1, column=0)
btn6.grid(row=1, column=1)
btn7.grid(row=1, column=2)
btn8.grid(row=1, column=3)
btn9.grid(row=1, column=4)














gamewindow.mainloop()