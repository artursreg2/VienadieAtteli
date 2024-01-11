from tkinter import *
from PIL import ImageTk, Image
import random
from tkinter import messagebox

gamewindow=Tk()
gamewindow.title("Vienādie attēli")
gamewindow.configure(bg="black")
gamewindow.resizable(1,1)



myimg1=ImageTk.PhotoImage(Image.open("7.jpg"))
myimg2=ImageTk.PhotoImage(Image.open("2.jpg"))
myimg3=ImageTk.PhotoImage(Image.open("3.jpg"))
myimg4=ImageTk.PhotoImage(Image.open("4.jpg"))
myimg5=ImageTk.PhotoImage(Image.open("5.jpg"))
myimg6=ImageTk.PhotoImage(Image.open("6.jpg"))

ImageList=[myimg1,myimg1,myimg2,myimg2,myimg3,myimg3,myimg4,myimg4,myimg5,myimg5,myimg6,myimg6]

myLabel=Label(image=myimg1)

bgImg=ImageTk.PhotoImage(Image.open("8.jpg"))




btn1 = Button(width=200, height=200, image=bgImg,command=lambda: btnClick(btn1,1)
btn2 = Button(width=200, height=200, image=bgImg,command=lambda: btnClick(btn2,2)
btn3 = Button(width=200, height=200, image=bgImg,command=lambda: btnClick(btn3,3)
btn4 = Button(width=200, height=200, image=bgImg,command=lambda: btnClick(btn4,4)
btn5 = Button(width=200, height=200, image=bgImg,command=lambda: btnClick(btn5,5)
btn6 = Button(width=200, height=200, image=bgImg,command=lambda: btnClick(btn6,6)
btn7 = Button(width=200, height=200, image=bgImg,command=lambda: btnClick(btn7,7)
btn8 = Button(width=200, height=200, image=bgImg,command=lambda: btnClick(btn8,8)


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



count=0
correctanswers=0
answers=[]
answer_dict={}
answerCount=0

def reset():
    global count, correctAnswers, answers, answer_dict, answerCount
    btn1.config(state=NORMAL)
    btn2.config(state=NORMAL)
    btn3.config(state=NORMAL)
    btn4.config(state=NORMAL)
    btn5.config(state=NORMAL)
    btn6.config(state=NORMAL)
    btn7.config(state=NORMAL)
    btn8.config(state=NORMAL)

    btn1["image"]="pyimage8"
    btn2["image"]="pyimage8"
    btn3["image"]="pyimage8"
    btn4["image"]="pyimage8"
    btn5["image"]="pyimage8"
    btn6["image"]="pyimage8"
    btn7["image"]="pyimage8"
    btn8["image"]="pyimage8"


random.shuffle(ImageList)

count=0
correctanswers=0
answers=[]
answer_dict={}
answerCount=0



def infoLogs():
    gamewindow=Toplevel()
    gamewindow.title("Info par programmu")
    gamewindow.geometry("500x300")
    apraksts=Label(gamewindow, text="Atmini 2 vienādas kant")
    apraksts.grid(row=0, column=0)
    return 0

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
        if correctanswers==9:
            messagebox.showinfo("Vienādi attēli","Esi uzminējis")
    else:
        messagebox.showinfo("Vienādi attēli","Neesi uzminējis")
        for key in answer_dict:
            key["image"]="pyimage3"
        count=0
        answers=[]
        answer_dict={}  
    return 0









galvenaIzvelne=Menu(gamewindow)
gamewindow.config(menu=galvenaIzvelne)

opcijas=Menu(galvenaIzvelne, tearoff=False)
galvenaIzvelne.add_cascade(label="Opcijas", menu=opcijas)

#opcijas.add_command(label="Jauna spēle",command=reset)
opcijas.add_command(label="Iziet",command=gamewindow.quit)

#galvenaIzvelne.add_command(label="Par programmu",command=infoLogs)














































































































gamewindow.mainloop()