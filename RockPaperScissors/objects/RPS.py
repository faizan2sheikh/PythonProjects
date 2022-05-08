from tkinter import*
import random
m=Tk() 
m.title("Rock Paper Scissors") 
m.geometry("900x700") 
m.configure(bg="green") 
m.resizable(0,0)


class Object(Frame):
    def add_pic_panel1(self,pic):
        picture=PhotoImage(file=pic)
        picture_add = picture.subsample(5,5)
        photo=Label(self.master,image=picture_add)
        photo.img=picture_add
        photo.place(x=140,y=300)
        self.pack()

    def add_pic_panel2(self,pic):
        picture=PhotoImage(file=pic)
        picture_add = picture.subsample(5,5)
        photo=Label(self.master,image=picture_add)
        photo.img=picture_add
        photo.place(x=500,y=300)
        self.pack()

    def __init__(self, master=None):
        Frame.__init__(self, master)

score=0
def insert(score): 
    l1=Label(m,text=score)
    l1.place(x=100,y=50)
    l2=Label(m,text="Score")
    l2.place(x=50,y=50)


def check_place(val):
    if val==1:
        place1=Object(master=m)
        place1.add_pic_panel1('objects/rock.png')
    if val==2:
        place1=Object(master=m)
        place1.add_pic_panel1('objects/paper.png')
    if val==3:
        place1=Object(master=m)
        place1.add_pic_panel1('objects/scissors.png')
    def ai_guess(val):
        guess=random.randrange(1,4)
        if guess==1:
            place2=Object(master=m)
            place2.add_pic_panel2('objects/rck2.png')
        if guess==2:
            place2=Object(master=m)
            place2.add_pic_panel2('objects/pap2.png')
        if guess==3:
            place2=Object(master=m)
            place2.add_pic_panel2('objects/sci2.png')
        def compare(val,guess):
            global score
            if val==guess:
                insert(score)
            if val==1 and guess==2:
                score-=1
                insert(score)
            if val==1 and guess==3:
                score+=1
                insert(score)
            if val==2 and guess==1:
                score+=1
                insert(score)
            if val==2 and guess==3:
                score-=1
                insert(score)
            if val==3 and guess==1:
                score-=1
                insert(score)
            if val==3 and guess==2:
                score+=1
                insert(score)









        compare(val,guess)
    ai_guess(val)

rck=Button(m,text='Rock',relief='groove',font=('#DCC4F5',11,'italic','bold'),command= lambda: check_place(1)) 
rck.place(x=40,y=250)

pap=Button(m,text='Paper',relief='groove',font=('#DCC4F5',11,'italic','bold'),command= lambda: check_place(2)) 
pap.place(x=40,y=350)

scr=Button(m,text='Scissors',relief='groove',font=('#DCC4F5',11,'italic','bold'),command= lambda: check_place(3)) 
scr.place(x=40,y=450)


mainloop()