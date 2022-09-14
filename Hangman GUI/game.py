from tkinter import*
import random
m=Tk() 
m.title("Hangman") 
m.geometry("790x700") 
m.configure(bg="teal") 
m.resizable(0,0) 

guess=5
f=open('words.txt')
f=f.read()
f=f.split(",")
word=random.choice(f)
ltr=[]
for i in word:
    ltr.append(i)
print(ltr)
gaps=[]
for i in range(len(ltr)):
    gaps.append('_')
spaces=Label(m,text=gaps,font=('#DCC4F5',14,'italic'))
spaces.place(x=350,y=600)

class Application(Frame):
    def add_pic_panel(self,pic):
        picture=PhotoImage(file=pic)
        picture_add = picture.subsample(3,3)
        photo=Label(self.master,image=picture_add)
        photo.img=picture_add
        photo.place(x=180,y=130)
        self.pack()
#        return photo

    def __init__(self, master=None):
        Frame.__init__(self, master)

app=Application(master=m)
app.add_pic_panel('man/1.png')

def check(guess_ltr):
    global word
    global guess
    ltr_guessed=''
    if guess_ltr in word:
        ltr_guessed+=guess_ltr      
        def indices(mylist,value):
            return [i for i,x in enumerate(mylist) if x==value]
        x=indices(ltr,guess_ltr)
        for pos in x:
            gaps[pos]=guess_ltr
        spaces=Label(m,text=gaps,font=('#DCC4F5',14,'italic'),fg='beige',bg='#363630')
        spaces.place(x=350,y=600)
    else:
        if guess==5:
            app.add_pic_panel('man/2.png')
            guess-=1
            print(guess)
        elif guess==4:
            app.add_pic_panel('man/3.png')
            guess-=1
            print(guess)
        elif guess==3:
            app.add_pic_panel('man/4.png')
            guess-=1
            print(guess)
        elif guess==2:
            app.add_pic_panel('man/5.png')
            guess-=1
            print(guess)
        elif guess==1:
            app.add_pic_panel('man/6.png')
            guess-=1
            print(guess)
        else:        
            app.add_pic_panel('man/7.png')
            right=Label(m,text=ltr,font=('#DCC4F5',14,'italic'))
            right.place(x=350,y=600)
            
    
class Field(Button):
    def __init__(self, value, **k):
        Button.__init__(self, **k)
        self.value = value

    def get_and_destroy(self):
        letter=self.value
#        check(self.value)
        check(letter)
        self.destroy()
#        return self.value

#frame
r=Frame(m,bg="black") 
r.place(x=0,y=0,width=900,height=120)
# Creating a photoimage object to use image

a_photo=PhotoImage(file = r"letters/a.png") 
a_photoimage = a_photo.subsample(3,3) 
a_bt=Field('a', image = a_photoimage)
a_bt.config(command=a_bt.get_and_destroy)
a_bt.place(x=10,y=10)

b_photo=PhotoImage(file = r"letters/b.png") 
b_photoimage = b_photo.subsample(3,3) 
b_bt=Field('b', image = b_photoimage)
b_bt.config(command=b_bt.get_and_destroy)
b_bt.place(x=70,y=10)

c_photo=PhotoImage(file = r"letters/c.png") 
c_photoimage = c_photo.subsample(3,3) 
c_bt=Field('c', image = c_photoimage)
c_bt.config(command=c_bt.get_and_destroy)
c_bt.place(x=130,y=10)

d_photo=PhotoImage(file = r"letters/d.png") 
d_photoimage = d_photo.subsample(3,3) 
d_bt=Field('d', image = d_photoimage)
d_bt.config(command=d_bt.get_and_destroy)
d_bt.place(x=190,y=10)

e_photo=PhotoImage(file = r"letters/e.png") 
e_photoimage = e_photo.subsample(3,3) 
e_bt=Field('e', image = e_photoimage)
e_bt.config(command=e_bt.get_and_destroy)
e_bt.place(x=250,y=10)

f_photo=PhotoImage(file = r"letters/f.png") 
f_photoimage = f_photo.subsample(3,3) 
f_bt=Field('f', image = f_photoimage)
f_bt.config(command=f_bt.get_and_destroy)
f_bt.place(x=310,y=10)

g_photo=PhotoImage(file = r"letters/g.png") 
g_photoimage = g_photo.subsample(3,3) 
g_bt=Field('g', image = g_photoimage)
g_bt.config(command=g_bt.get_and_destroy)
g_bt.place(x=370,y=10)

h_photo=PhotoImage(file = r"letters/h.png") 
h_photoimage = h_photo.subsample(3,3) 
h_bt=Field('h', image = h_photoimage)
h_bt.config(command=h_bt.get_and_destroy)
h_bt.place(x=430,y=10)

i_photo=PhotoImage(file = r"letters/i.png") 
i_photoimage = i_photo.subsample(3,3) 
i_bt=Field('i', image = i_photoimage)
i_bt.config(command=i_bt.get_and_destroy)
i_bt.place(x=490,y=10)

j_photo=PhotoImage(file = r"letters/j.png") 
j_photoimage = j_photo.subsample(3,3) 
j_bt=Field('j', image = j_photoimage)
j_bt.config(command=j_bt.get_and_destroy)
j_bt.place(x=550,y=10)

k_photo=PhotoImage(file = r"letters/k.png") 
k_photoimage = k_photo.subsample(3,3) 
k_bt=Field('k', image = k_photoimage)
k_bt.config(command=k_bt.get_and_destroy)
k_bt.place(x=610,y=10)

l_photo=PhotoImage(file = r"letters/l.png") 
l_photoimage = l_photo.subsample(3,3) 
l_bt=Field('l', image = l_photoimage)
l_bt.config(command=l_bt.get_and_destroy)
l_bt.place(x=670,y=10)

m_photo=PhotoImage(file = r"letters/m.png") 
m_photoimage = m_photo.subsample(3,3) 
m_bt=Field('m', image = m_photoimage)
m_bt.config(command=m_bt.get_and_destroy)
m_bt.place(x=730,y=10)

n_photo=PhotoImage(file = r"letters/n.png") 
n_photoimage = n_photo.subsample(3,3) 
n_bt=Field('n', image = n_photoimage)
n_bt.config(command=n_bt.get_and_destroy)
n_bt.place(x=10,y=66)

o_photo=PhotoImage(file = r"letters/o.png") 
o_photoimage = o_photo.subsample(3,3) 
o_bt=Field('o', image = o_photoimage)
o_bt.config(command=o_bt.get_and_destroy)
o_bt.place(x=70,y=66)

p_photo=PhotoImage(file = r"letters/p.png") 
p_photoimage = p_photo.subsample(3,3) 
p_bt=Field('p', image = p_photoimage)
p_bt.config(command=p_bt.get_and_destroy)
p_bt.place(x=130,y=66)

q_photo=PhotoImage(file = r"letters/q.png") 
q_photoimage = q_photo.subsample(3,3) 
q_bt=Field('q', image = q_photoimage)
q_bt.config(command=q_bt.get_and_destroy)
q_bt.place(x=190,y=66)

r_photo=PhotoImage(file = r"letters/r.png") 
r_photoimage = r_photo.subsample(3,3) 
r_bt=Field('r', image = r_photoimage)
r_bt.config(command=r_bt.get_and_destroy)
r_bt.place(x=250,y=66)

s_photo=PhotoImage(file = r"letters/s.png") 
s_photoimage = s_photo.subsample(3,3) 
s_bt=Field('s', image = s_photoimage)
s_bt.config(command=s_bt.get_and_destroy)
s_bt.place(x=310,y=66)

t_photo=PhotoImage(file = r"letters/t.png") 
t_photoimage = t_photo.subsample(3,3) 
t_bt=Field('t', image = t_photoimage)
t_bt.config(command=t_bt.get_and_destroy)
t_bt.place(x=370,y=66)

u_photo=PhotoImage(file = r"letters/u.png") 
u_photoimage = u_photo.subsample(3,3) 
u_bt=Field('u', image = u_photoimage)
u_bt.config(command=u_bt.get_and_destroy)
u_bt.place(x=430,y=66)

v_photo=PhotoImage(file = r"letters/v.png") 
v_photoimage = v_photo.subsample(3,3) 
v_bt=Field('v', image = v_photoimage)
v_bt.config(command=v_bt.get_and_destroy)
v_bt.place(x=490,y=66)

w_photo=PhotoImage(file = r"letters/w.png") 
w_photoimage = w_photo.subsample(3,3) 
w_bt=Field('w', image = w_photoimage)
w_bt.config(command=w_bt.get_and_destroy)
w_bt.place(x=550,y=66)

x_photo=PhotoImage(file = r"letters/x.png") 
x_photoimage = x_photo.subsample(3,3) 
x_bt=Field('x', image = x_photoimage)
x_bt.config(command=x_bt.get_and_destroy)
x_bt.place(x=610,y=66)

y_photo=PhotoImage(file = r"letters/y.png") 
y_photoimage = y_photo.subsample(3,3) 
y_bt=Field('y', image = y_photoimage)
y_bt.config(command=y_bt.get_and_destroy)
y_bt.place(x=670,y=66)

z_photo=PhotoImage(file = r"letters/z.png") 
z_photoimage = z_photo.subsample(3,3) 
z_bt=Field('z', image = z_photoimage)
z_bt.config(command=z_bt.get_and_destroy)
z_bt.place(x=730,y=66)

mainloop()