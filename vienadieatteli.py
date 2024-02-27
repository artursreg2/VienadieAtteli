import time
from tkinter import *
from PIL import ImageTk, Image
import random
from tkinter import messagebox
#----------------------------------------------------------------------------------




gamewindow=Tk()
gamewindow.title("Vienādie attēli")
gamewindow.configure(bg="black")
gamewindow.resizable(1,1)



myimg1=ImageTk.PhotoImage(Image.open("1.jpg"))
myimg2=ImageTk.PhotoImage(Image.open("2.jpg"))
myimg3=ImageTk.PhotoImage(Image.open("3.jpg"))
myimg4=ImageTk.PhotoImage(Image.open("4.jpg"))
myimg5=ImageTk.PhotoImage(Image.open("5.jpg"))
myimg6=ImageTk.PhotoImage(Image.open("6.jpg"))
myimg7=ImageTk.PhotoImage(Image.open("7.jpg"))


ImageList=[myimg1,myimg1,myimg2,myimg2,myimg3,myimg3,myimg4,myimg4,myimg5,myimg5,myimg6,myimg6,myimg7,myimg7]

myLabel=Label(image=myimg1)

bgImg=ImageTk.PhotoImage(Image.open("8.jpg"))

    
#-----------------------------------------

btn0 = Button(width=200, height=200, image=bgImg,command=lambda: btnClick(btn0,0))
btn1 = Button(width=200, height=200, image=bgImg,command=lambda: btnClick(btn1,1))
btn2 = Button(width=200, height=200, image=bgImg,command=lambda: btnClick(btn2,2))
btn3 = Button(width=200, height=200, image=bgImg,command=lambda: btnClick(btn3,3))
btn4 = Button(width=200, height=200, image=bgImg,command=lambda: btnClick(btn4,4))
btn5 = Button(width=200, height=200, image=bgImg,command=lambda: btnClick(btn5,5))
btn6 = Button(width=200, height=200, image=bgImg,command=lambda: btnClick(btn6,6))
btn7 = Button(width=200, height=200, image=bgImg,command=lambda: btnClick(btn7,7))
btn8 = Button(width=200, height=200, image=bgImg,command=lambda: btnClick(btn8,8))
btn9 = Button(width=200, height=200, image=bgImg,command=lambda: btnClick(btn9,9))

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


#-----------------------------------------

random.shuffle(ImageList)

count=0
correctAnswers=0
answers=[]
answer_dict={}
answerCount=0
#---------------------------------------------------------------------------------


def reset():
    global count, correctAnswers, answers, answer_dict, answerCount
    btn0.config(state=NORMAL)
    btn1.config(state=NORMAL)
    btn2.config(state=NORMAL)
    btn3.config(state=NORMAL)
    btn4.config(state=NORMAL)
    btn5.config(state=NORMAL)
    btn6.config(state=NORMAL)
    btn7.config(state=NORMAL)
    btn8.config(state=NORMAL)
    btn9.config(state=NORMAL)


    btn1["image"]="pyimage8"
    btn2["image"]="pyimage8"
    btn3["image"]="pyimage8"
    btn4["image"]="pyimage8"
    btn5["image"]="pyimage8"
    btn6["image"]="pyimage8"
    btn7["image"]="pyimage8"
    btn8["image"]="pyimage8"
    btn9["image"]="pyimage8"


    random.shuffle(ImageList)

    count=0
    correctAnswers=0
    answers=[]
    answer_dict={}
    answerCount=0




def infoLogs():
    gamewindow=Toplevel()
    gamewindow.title("Info par programmu")
    gamewindow.geometry("500x300")
    apraksts=Label(gamewindow, text="Atmini 2 vienādus attēlus")
    apraksts.grid(row=0, column=0)
    return 0

#----------------------------------------------------------------------------------


def btnClick(btn,number):
    global count, correctAnswers, answers, answer_dict, answerCount
    if btn["image"]=="pyimage8" and count<2:
        btn["image"]=ImageList[number]
        count+=1
        answers.append(number)
        answer_dict[btn]=ImageList[number]
    if len(answers)==2:
        if ImageList[answers[0]]==ImageList[answers[1]]:
            for key in answer_dict:
                key["state"]=DISABLED
            correctAnswers+=2
            if correctAnswers==2:
                correctAnswers=0
                answerCount+=1
        else:
            Tk.update(btn)
            time.sleep(1.5)
            for key in answer_dict:
                key["image"]="pyimage8"
        count=0
        answers=[]
        answer_dict={}
    if answerCount==5:
        messagebox.showinfo("Sheesh!","You win")
        reset()




galvenaIzvelne=Menu(gamewindow)
gamewindow.config(menu=galvenaIzvelne)

opcijas=Menu(galvenaIzvelne, tearoff=False)
galvenaIzvelne.add_cascade(label="Opcijas", menu=opcijas)

opcijas.add_command(label="Jauna spēle",command=reset)
opcijas.add_command(label="Iziet",command=gamewindow.quit)

galvenaIzvelne.add_command(label="Par programmu",command=infoLogs)


gamewindow.mainloop()