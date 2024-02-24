from tkinter import*
import random
window=Tk()
window.title("Rock Paper Scissors")
window.geometry("280x150")
window.config(bg="sky blue")
button=Button(window,text="Rock",command=lambda:user("Rock"))
button.grid(row=0,column=0)
button=Button(window,text="Paper",command=lambda:user("Paper"))
button.grid(row=0,column=1)
button=Button(window,text="Scissors",command=lambda:user("Scissors"))
button.grid(row=0,column=2)
label=Label(window,text="")
label.grid(row=1,column=1)
lable1=Label(window,text="The score is:")
lable1.grid(row=2,column=1)
scoret=[]
clearB=Button(window,text="ResetScore",command=lambda:clear())
clearB.grid(row=3,column=1)
def user(choice):
    score=0
    a=["rock","paper","scissors"]
    b=random.choice(a)
    if(choice=="Rock"):
        if(b=="rock"):
            label.config(text="the game is tie")
            lable1.config(text="The score is:%d"%sum(scoret))
        elif(b=="paper"):
            score=score-1
            scoret.append(score)
            label.config(text="the game is lose")
            lable1.config(text="The score is:%d"%sum(scoret))
        else:
            score=score+1
            scoret.append(score)
            label.config(text="the game is win")
            lable1.config(text="The score is:%d"%sum(scoret))
    elif(choice=="Paper"):
        if(b=="rock"):
            score=score+1
            scoret.append(score)
            label.config(text="the game is win")
            lable1.config(text="The score is:%d"%sum(scoret))
        elif(b=="paper"):
            label.config(text="the game is tie")
            lable1.config(text="The score is:%d"%sum(scoret))
        else:
            score=score-1
            scoret.append(score)
            label.config(text="the game is lose")
            lable1.config(text="The score is:%d"%sum(scoret))
    elif(choice=="Scissors"):
        if(b=="rock"):
            score=score-1
            scoret.append(score)
            label.config(text="the game is lose")
            lable1.config(text="The score is:%d"%sum(scoret))
        elif(b=="paper"):
            score=score+1
            scoret.append(score)
            label.config(text="the game is win")
            lable1.config(text="The score is:%d"%sum(scoret))
        else:
            label.config(text="the game is tie")
            lable1.config(text="The score is:%d"%sum(scoret))
def clear():
    scoret.clear()
    lable1.config(text="The score is:%d"%sum(scoret))
    label.config(text="")
mainloop()
