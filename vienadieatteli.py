from tkinter import *
from PIL import ImageTk, Image
import random
from tkinter import messagebox
gamewindow=Tk()
gamewindow.title("Vienādie attēli")



count=0
correctanswers=0
answers=[]
answer_dict={}

def btnClick(btn,number):
    global count, correctanswers, answers, answer_dict
    if btn["image"]=="pyimage1" and count<2:
        btn["image"]=ImageList[number]
        count+=1
        answers.append(number)
        answer_dict[btn]=ImageList[number]
    if len(answers)==2:
        if ImageList[answers[0]]==ImageList[answers[1]]:
            for key in answer_dict:
                key["state"]=DISABLED
        correctanswers+=1
        if correctanswers==2:
            messagebox.showinfo("Vienādi attēli","Esi uzminējis")
    else:
        messagebox.showinfo("Vienādi attēli","Neesi uzminējis")
        for key in answer_dict:
            key["image"]="pyimage3"
        count=0
        answers=[]
        answer_dict={}  
    return 0




myimg1=ImageTk.PhotoImage(Image.open("7.jpg"))
myimg2=ImageTk.PhotoImage(Image.open("2.jpg"))
myimg3=ImageTk.PhotoImage(Image.open("3.jpg"))
myimg4=ImageTk.PhotoImage(Image.open("4.jpg"))
myimg5=ImageTk.PhotoImage(Image.open("5.jpg"))
myimg6=ImageTk.PhotoImage(Image.open("6.jpg"))

bgImg=ImageTk.PhotoImage(Image.open("8.jpg"))

ImageList=[myimg1,myimg1,myimg2,myimg2,myimg3,myimg3,myimg4,myimg4,myimg5,myimg5,myimg6,myimg6]

random.shuffle(ImageList)



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



galvenaIzvelne=Menu(gamewindow)
gamewindow.config(menu=galvenaIzvelne)

opcijas=Menu(galvenaIzvelne, tearoff=False)
galvenaIzvelne.add_cascade(label="Opcijas", menu=opcijas)

opcijas.add_command(label="Jauna spēle",command=reset)
opcijas.add_command(label="Iziet",command=gamewindow.quit)

galvenaIzvelne.add_command(label="Par programmu",command=reset)














































































































gamewindow.mainloop()