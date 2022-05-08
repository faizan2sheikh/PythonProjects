# Libraries used is this code
from dataclasses import Field
from inspect import Parameter
from multiprocessing.sharedctypes import Value
from os import error
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from turtle import width
from PIL import Image,ImageTk
from datetime import datetime
import os.path
import sqlite3

# Establishing the connection
conn = sqlite3.connect('library.db')

c = conn.cursor()

# Creating required tables if they do not already exist in our database
c.execute("""CREATE TABLE if not exists books (
            id integer,
            name text,
            author text,
            publication integer,
            cover text,
            description text,
            borrowed integer,
            reserve integer,
            rating float
            )""")

c.execute("""CREATE TABLE if not exists records (
            id integer,
            name text,
            action text,
            member text,
            date text,
            time text
            )
            """)

c.execute("""CREATE TABLE if not exists members (
            name text,
            email text,
            address text,
            phone text
            )
            """)

# Username and password for entering in admin panel
admin_user='admin'
admin_pass='admin'

class Books:
    '''This class contains books with their respective attributes''' 
    def __init__(self):
        self.books={}

## Below function contains sorting algorithm

    def load_product(self):
        '''Function for loading the books from file'''
        self.__init__()
        with conn:
            c.execute("SELECT * FROM books")
        sorted_books=c.fetchall()

# SORTING ALGORITHM

        for k in range(len(sorted_books)):
            for j in range(len(sorted_books)):
                if sorted_books[j][1].lower()>sorted_books[k][1].lower():
                    sorted_books[k],sorted_books[j]=sorted_books[j],sorted_books[k]
       
# Conveting list into dictionary

        for i in sorted_books:   
            self.books.update({i[0]:[i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]})

class Admin(Books):
    '''This admin class contains all the functionality of admin panel'''
    def destroy_frames(self):
        '''This function destroy previous frames to avoid overlapping'''
        if self.current_frame=='showbooks':
            self.books_frame.destroy()
        if self.current_frame=='add':
            self.add_frame.destroy()
        if self.current_frame=='search':
            self.tree_frame.destroy()
            self.search_frame.destroy()
        if self.current_frame=='manage':
            self.manage_frame.destroy()
        if self.current_frame=='transact':
            self.transact_frame.destroy()
        if self.current_frame=='remove':
            self.tree_frame.destroy()
            self.remove_frame.destroy()
        if self.current_frame=='edit':
            self.tree_frame.destroy()
            self.edit_frame.destroy()
        if self.current_frame=='add_mem':
            self.add_mem_frame.destroy()
        if self.current_frame=='mem':
            self.memtree_frame.destroy()
        
    def create_admin_treeview(self):
        '''This function is created to avoid repitition of code for creating Treeview component'''
        self.style=ttk.Style()
        self.style.theme_use('default')
        self.style.configure('Treeview',
            background='#E0CCE3',
            foreground='black',
            rowheight=20,
            fieldbackground='D3D3D3'
            )
        self.style.map('Treeview',
            background=[('selected','#8C5394')])

        #Frame for treeview
        self.tree_frame=Frame(self.root)
        self.tree_frame.place(x=450,y=130,height=520,width=700)
        self.tree_frame.config(bg='#C2C2AE')

        #Scrollbar
        self.tree_scroll=Scrollbar(self.tree_frame)
        self.tree_scroll.pack(side=RIGHT,fill=Y)

        #Defining
        self.my_tree=ttk.Treeview(self.tree_frame,yscrollcommand=self.tree_scroll.set,selectmode='browse')
        self.my_tree['columns']=('Product Id','Name','Author','Published','Rating')
        self.tree_scroll.config(command=self.my_tree.yview)

        #Formatting
        self.my_tree.column('#0',width=0,stretch=NO)
        self.my_tree.column('Product Id',anchor=CENTER,width=80)
        self.my_tree.column('Name',anchor=CENTER,width=160)
        self.my_tree.column('Author',anchor=CENTER,width=160)
        self.my_tree.column('Published',anchor=CENTER,width=100)
        self.my_tree.column('Rating',anchor=CENTER,width=180)

        #Headings
        self.my_tree.heading('#0',text='',anchor=W)
        self.my_tree.heading('Product Id',text='Product Id',anchor=CENTER)
        self.my_tree.heading('Name',text='Name',anchor=CENTER)
        self.my_tree.heading('Author',text='Author',anchor=CENTER)
        self.my_tree.heading('Published',text='Published',anchor=CENTER)
        self.my_tree.heading('Rating',text='Rating',anchor=CENTER)
        self.my_tree.place(x=0,y=0,height=520,width=683)

        #For Striped Treeview
        self.my_tree.tag_configure('odd',background='#F5DCD0')
        self.my_tree.tag_configure('even',background='#F5F5C4')   

    def add_to_lib(self,id,name,author,publication,cover,desc,borrowed,reserve,rating):
        '''This function actually adds book to library'''
        with conn:
            c.execute("SELECT * FROM books WHERE id= ? OR name = ?",(id,name))
            if len(c.fetchall())==0:
                c.execute("INSERT INTO books VALUES (?,?,?,?,?,?,?,?,?)",(id,name,author,publication,cover,desc,borrowed,reserve,rating))
            else:
                messagebox.showinfo("Error", "Book with similar id or name already exists!")

    def add(self):
        '''This function checks all the prerequisites for storage in library'''
        try:
            if len(self.entry_id.get())==0 or len(self.entry_image.get())==0 or len(self.entry_auth.get())==0 or len(self.entry_pub.get())==0 or len(self.entry_rating.get())==0 or len(self.text.get("1.0",'end-1c'))==0:
                self.message='Please enter values in all entry fields'
                raise ValueError
            if self.entry_id.get() in self.books.keys():
                self.message='Books with similar id exist in records'
                raise KeyError
            if os.path.isfile(self.entry_image.get())==False:
                self.message='Image file does not exist'
                raise KeyError
            if True:
                self.message='Please enter an integer in publication'
                if isinstance(int(self.entry_pub.get()),int)==False:
                    raise ValueError
            if True:
                self.message='Please enter float in rating'
                if isinstance(float(self.entry_rating.get()),float)==False:
                    raise ValueError
            self.add_to_lib(int(self.entry_id.get()),self.entry_name.get(),self.entry_auth.get(),int(self.entry_pub.get()),self.entry_image.get(),self.text.get("1.0",'end-1c'),0,0,float(self.entry_rating.get()))
            messagebox.showinfo('Success!','Books added to library')
        except:
            messagebox.showwarning('Invalid entry',self.message)
        
    def update_book(self):
        '''This function updates parameter of books in records'''
        def edit():
            id=int(entry_id1.get())
            parameter=mycombo.get()
            value=entry_id2.get()
            with conn:
                c.execute("SELECT * FROM books WHERE id= ?",(id,))
            fetched=c.fetchall()
            if len(fetched)==0:
                messagebox.showerror('Wrong Id','Sorry this book does not exist in records')
            else:
                with conn:
                        c.execute("SELECT * FROM books WHERE id= ?",(id,))
                        if len(c.fetchall())>0:
                            c.execute("""UPDATE books SET {}=?
                                        WHERE id=?""".format(parameter),
                                        (value,id))
                messagebox.showinfo('Deleted','Book edited')
        self.destroy_frames
        self.create_admin_treeview()
        self.current_frame='edit'
        self.edit_frame=Frame(self.root)
        self.edit_frame.config(bg='#C4F5EF')
        self.edit_frame.place(x=450,y=550,width=683,height=100)
        label_head=Label(self.edit_frame,text="Edit Product",bg='#8C5394',fg='#FFFFFF',font=('Constantia',16))
        label_head.place(x=0,y=0,height=40,width=683)
        label_id=Label(self.edit_frame,text="Enter ID:",font=('#DCC4F5',11,'italic','bold'))
        label_id.place(x=10,y=60)
        entry_id1=Entry(self.edit_frame)
        entry_id1.place(x=120,y=60,width=80)
        label_id2=Label(self.edit_frame,text="Data:",font=('#DCC4F5',11,'italic','bold'))
        label_id2.place(x=200,y=60)
        entry_id2=Entry(self.edit_frame)
        entry_id2.place(x=280,y=60)
        para=['name','author','rating','description','publication']
        mycombo=ttk.Combobox(self.edit_frame, value=para, state="readonly")
        mycombo.current(0)
        mycombo.bind("<<ComboboxSelected>>",)
        mycombo.place(x=350,y=60)
        b=Button(self.edit_frame,text='Enter',bg='#FFF5CF',font=('Constantia',12),command=edit)
        b.place(x=480,y=60)

    def search(self):
        '''This function searches for product in records using its product Id'''
        self.destroy_frames()
        self.current_frame='search'
        self.create_admin_treeview()
        self.search_frame=Frame(self.root)
        self.search_frame.config(bg='#C4F5EF')
        self.search_frame.place(x=450,y=550,width=683,height=100)
        with conn:
            c.execute("SELECT * FROM books")
        items=c.fetchall()
        self.my_tree.delete(*self.my_tree.get_children())
        def check():
            item_id=1
            data=book_info.get()
            param=mycombo.get()
            if param=='id':
                data=int(data)
            with conn:
                c.execute("SELECT * FROM books WHERE {}= ?".format(param),(data,))
            searched=c.fetchall()
            if len(searched)!=0:
                for item in searched:
                    if item_id%2==0:self.my_tree.insert(parent='',index='end',iid=item_id,text='',values=(str(item[0]),str(item[1]),str(item[2]),str(item[3]),str(str(item[8])+' Stars')),tags=('even',))
                    else:self.my_tree.insert(parent='',index='end',iid=item_id,text='',values=(str(item[0]),str(item[1]),str(item[2]),str(item[3]),str(str(item[8])+' Stars')),tags=('odd',)) 
                    item_id+=1                   
            else:
                self.my_tree.insert(parent='',index='end',iid=item_id,text='',values=('Sorry item not found'))
            self.search_frame.destroy()
        label_head=Label(self.search_frame,text="Search Product",bg='#8C5394',fg='#FFFFFF',font=('Constantia',16))
        label_head.place(x=0,y=0,height=40,width=683)      
        book_info=Entry(self.search_frame)
        book_info.place(x=120,y=60)
        instruction=Label(self.search_frame,text='Enter data:',font=('#DCC4F5',11,'italic','bold'))
        instruction.place(x=10,y=60)
        para=['id','name','author']
        mycombo=ttk.Combobox(self.search_frame, value=para, state="readonly")
        mycombo.current(0)
        mycombo.bind("<<ComboboxSelected>>",)
        mycombo.place(x=300,y=60)
        search_btn=Button(self.search_frame,text='Search record',font=('#DCC4F5',11,'italic','bold'),relief='groove',command=check)
        search_btn.place(x=480,y=60)

    def add_book(self):
        '''This function provides data for add function to add books in file'''
        self.destroy_frames()
        self.current_frame='add'
        self.add_frame=Frame(self.root)
        self.add_frame.config(bg='#E0CCE3')
        self.add_frame.place(x=450,y=130,width=700,height=520)
        label_head=Label(self.add_frame,text="Add book in library",bg='#8C5394',fg='#FFFFFF',font=('Constantia',24))
        label_head.place(x=0,y=0,width=700,height=80)
        label_id=Label(self.add_frame,text="Enter Book ID:",bg='#FFF5CF',font=('Constantia',16))
        label_id.place(x=10,y=110,height=30)
        self.entry_id=Entry(self.add_frame)
        self.entry_id.place(x=200,y=110,height=30)
        label_name=Label(self.add_frame,text='Enter Book Name:',bg='#FFF5CF',font=('Constantia',16))
        label_name.place(x=10,y=150,height=30)
        self.entry_name=Entry(self.add_frame)
        self.entry_name.place(x=200,y=150,height=30)
        label_auth=Label(self.add_frame,text='Enter Author:',bg='#FFF5CF',font=('Constantia',16))
        label_auth.place(x=10,y=190,height=30)
        self.entry_auth=Entry(self.add_frame)
        self.entry_auth.place(x=200,y=190,height=30)
        label_image=Label(self.add_frame,text='Image address:',bg='#FFF5CF',font=('Constantia',16))
        label_image.place(x=10,y=230,height=30)
        self.entry_image=Entry(self.add_frame)
        self.entry_image.place(x=200,y=230,height=30)
        label_pub=Label(self.add_frame,text="Publication year:",bg='#FFF5CF',font=('Constantia',16))
        label_pub.place(x=10,y=270,height=30)
        self.entry_pub=Entry(self.add_frame)
        self.entry_pub.place(x=200,y=270,height=30)
        label_rating=Label(self.add_frame,text="Enter Rating:",bg='#FFF5CF',font=('Constantia',16))
        label_rating.place(x=10,y=310,height=30)
        self.entry_rating=Entry(self.add_frame)
        self.entry_rating.place(x=200,y=310,height=30)
        label_desc=Label(self.add_frame,text="Enter Description:",bg='#FFF5CF',font=('Constantia',16))
        label_desc.place(x=10,y=350,height=30)
        self.text =Text(self.add_frame, undo = True, height = 5, width = 50)
        self.text.place(x=200,y=350)
        b=Button(self.add_frame,text='Enter Record',bg='#FFF5CF',font=('Constantia',12),command=self.add)
        b.place(x=300,y=470)

    def remove_book(self):
        '''This function provides data for remove function'''
        self.destroy_frames
        self.create_admin_treeview()
        def remove():
            '''This function removes the product from file'''
            data=entry_id.get()
            param=mycombo.get()
            if param=='id':data=int(data)
            with conn:
                c.execute("SELECT * FROM books WHERE {}= ?".format(param),(data,))
            fetched=c.fetchall()
            if len(fetched)==0:
                messagebox.showerror('Wrong Id','Sorry this book does not exist in records')
            else:
                with conn:
                    c.execute("DELETE from books WHERE {}=?".format(param),(data,))
                messagebox.showinfo('Deleted','The book with id/name/author {} deleted!'.format(data))
        self.current_frame='remove'
        self.remove_frame=Frame(self.root)
        self.remove_frame.config(bg='#C4F5EF')
        self.remove_frame.place(x=450,y=550,width=683,height=100)
        label_head=Label(self.remove_frame,text="Remove Product",bg='#8C5394',fg='#FFFFFF',font=('Constantia',16))
        label_head.place(x=0,y=0,height=40,width=683)
        label_id=Label(self.remove_frame,text="Enter Data:",font=('#DCC4F5',11,'italic','bold'))
        label_id.place(x=10,y=60)
        entry_id=Entry(self.remove_frame)
        entry_id.place(x=120,y=60)
        para=['id','name','author']
        mycombo=ttk.Combobox(self.remove_frame, value=para, state="readonly")
        mycombo.current(0)
        mycombo.bind("<<ComboboxSelected>>",)
        mycombo.place(x=300,y=60)
        b=Button(self.remove_frame,text='Enter',bg='#FFF5CF',font=('Constantia',12),command=remove)
        b.place(x=480,y=60)

    def show_members(self):
        self.destroy_frames()
        self.current_frame='mem_frame'
        self.style=ttk.Style()
        self.style.theme_use('default')
        self.style.configure('Treeview',
            background='#E0CCE3',
            foreground='black',
            rowheight=20,
            fieldbackground='D3D3D3'
            )
        self.style.map('Treeview',
            background=[('selected','#8C5394')])

        #Frame for treeview
        self.memtree_frame=Frame(self.root)
        self.memtree_frame.place(x=450,y=130,height=520,width=700)
        self.memtree_frame.config(bg='#C2C2AE')

        #Scrollbar
        self.memtree_scroll=Scrollbar(self.memtree_frame)
        self.memtree_scroll.pack(side=RIGHT,fill=Y)

        #Defining
        self.memmy_tree=ttk.Treeview(self.memtree_frame,yscrollcommand=self.memtree_scroll.set,selectmode='browse')
        self.memmy_tree['columns']=('Name','Email','Address','Phone')
        self.memtree_scroll.config(command=self.memmy_tree.yview)

        #Formatting
        self.memmy_tree.column('#0',width=0,stretch=NO)
        self.memmy_tree.column('Name',anchor=CENTER,width=150)
        self.memmy_tree.column('Email',anchor=CENTER,width=170)
        self.memmy_tree.column('Address',anchor=CENTER,width=190)
        self.memmy_tree.column('Phone',anchor=CENTER,width=170)

        #Headings
        self.memmy_tree.heading('#0',text='',anchor=W)
        self.memmy_tree.heading('Name',text='Name',anchor=CENTER)
        self.memmy_tree.heading('Email',text='Email',anchor=CENTER)
        self.memmy_tree.heading('Address',text='Address',anchor=CENTER)
        self.memmy_tree.heading('Phone',text='Phone',anchor=CENTER)
        self.memmy_tree.place(x=0,y=0,height=520,width=683)

        #For Striped Treeview
        self.memmy_tree.tag_configure('odd',background='#F5DCD0')
        self.memmy_tree.tag_configure('even',background='#F5F5C4')   

        with conn:
            c.execute("SELECT * FROM members")
        items=c.fetchall()
        self.memmy_tree.delete(*self.memmy_tree.get_children())
        item_id=1
        if len(items)!=0:
            for item in items:
                if item_id%2==0:self.memmy_tree.insert(parent='',index='end',iid=item_id,text='',values=(str(item[0]),str(item[1]),str(item[2]),str(item[3])),tags=('even',))
                else:self.memmy_tree.insert(parent='',index='end',iid=item_id,text='',values=(str(item[0]),str(item[1]),str(item[2]),str(item[3])),tags=('odd',)) 
                item_id+=1                   
        else:
            self.memmy_tree.insert(parent='',index='end',iid=item_id,text='',values=('No members registered'))

    def add_members(self):
        def remove_mem():
            try:
                if len(self.del_name.get())==0:
                    raise ValueError
                with conn:
                    c.execute("SELECT * FROM members WHERE name= ?",(self.del_name.get()))
                if len(c.fetchall())!=0:
                    with conn:
                        c.execute("DELETE from members WHERE name=?",(self.del_name.get(),))
                    messagebox.showinfo('Success!','Member removed')
                else:
                    raise ValueError
            except:
                messagebox.showwarning('Invalid entry','Enter valid name')

        def add_mem():
            try:
                if len(self.name.get())==0 or len(self.address.get())==0 or len(self.phone.get())==0 or len(self.mail.get())==0:
                    raise ValueError
                with conn:
                    c.execute("INSERT INTO members VALUES (?,?,?,?)",(self.name.get(),self.mail.get(),self.address.get(),self.phone.get()))
                    messagebox.showinfo('Success!','Member registered to library')
            except:
                messagebox.showwarning('Invalid entry','Enter values in each entry')
        '''This function provides data for add function to add members in file'''
        self.destroy_frames()
        self.current_frame='add_mem'
        self.add_mem_frame=Frame(self.root)
        self.add_mem_frame.config(bg='#E0CCE3')
        self.add_mem_frame.place(x=450,y=130,width=700,height=520)
        label_head=Label(self.add_mem_frame,text="Membership registration",bg='#8C5394',fg='#FFFFFF',font=('Constantia',24))
        label_head.place(x=0,y=0,width=700,height=80)
        label_name=Label(self.add_mem_frame,text="Enter Name:",bg='#FFF5CF',font=('Constantia',16))
        label_name.place(x=10,y=110,height=30)
        self.name=Entry(self.add_mem_frame)
        self.name.place(x=200,y=110,height=30,width=150)
        label_mail=Label(self.add_mem_frame,text='Enter Email:',bg='#FFF5CF',font=('Constantia',16))
        label_mail.place(x=10,y=150,height=30)
        self.mail=Entry(self.add_mem_frame)
        self.mail.place(x=200,y=150,height=30,width=150)
        label_phone=Label(self.add_mem_frame,text='Enter Phone No.:',bg='#FFF5CF',font=('Constantia',16))
        label_phone.place(x=10,y=190,height=30)
        self.phone=Entry(self.add_mem_frame)
        self.phone.place(x=200,y=190,height=30,width=150)
        label_address=Label(self.add_mem_frame,text='Address:',bg='#FFF5CF',font=('Constantia',16))
        label_address.place(x=10,y=230,height=30)
        self.address=Entry(self.add_mem_frame)
        self.address.place(x=200,y=230,height=30,width=150)
        b=Button(self.add_mem_frame,text='Register',bg='#FFF5CF',font=('Constantia',12),command=add_mem)
        b.place(x=480,y=200)

        head=Label(self.add_mem_frame,text="Cancel Membership",bg='#8C5394',fg='#FFFFFF',font=('Constantia',24))
        head.place(x=0,y=340,height=80,width=700)
        label_dat=Label(self.add_mem_frame,text="Enter Member:",bg='#FFF5CF',font=('Constantia',16))
        label_dat.place(x=10,y=460)
        self.del_name=Entry(self.add_mem_frame)
        self.del_name.place(x=280,y=460,width=150,height=30)
        d=Button(self.add_mem_frame,text='Enter',bg='#FFF5CF',font=('Constantia',12),command=remove_mem)
        d.place(x=480,y=460)

    def manage(self):
        '''This function helps to restock books using thier id and quanitity'''
        def borrow():
            id=int(self.id1.get())
            name=self.name1.get()
            with conn:
                c.execute("SELECT * FROM books WHERE id = ?",(id,))
            found=c.fetchall()
            print(found)
            if len(found)==0:
                messagebox.showerror('Not Availabe','Sorry the book with this id is not in library!')
            elif found[0][6]==0:
                with conn:
                    bname=found[0][1]
                    c.execute("SELECT * FROM members WHERE name = ?",(name,))
                    members = c.fetchall()
                    if len(members)!=0:
                        bor=members[0][0]
                        c.execute("UPDATE books SET borrowed=? WHERE id=?",(1,int(self.id1.get())))
                        c.execute("INSERT INTO records VALUES (?,?,?,?,?,?)",(id,bname,'borrow',bor,datetime.now().strftime("%d-%b-%y"),datetime.now().strftime("%H:%M:%S")))
                        messagebox.showinfo('Success','Book successfully borrowed!')
                    else:
                        messagebox.showerror('Unregistered','No such registered member!')
            else:
                messagebox.showerror('Not Availabe','Sorry the book with this id is not currently available!')

        def reserve():
            id=int(self.id2.get())
            name=self.name2.get()
            with conn:
                c.execute("SELECT * FROM books WHERE id = ?",(id,))
            found=c.fetchall()
            print(found)
            if len(found)==0:
                messagebox.showerror('Not Availabe','Sorry the book with this id is not in library!')
            elif found[0][7]==0:
                with conn:
                    bname=found[0][1]
                    c.execute("SELECT * FROM members WHERE name = ?",(name,))
                    members = c.fetchall()
                    if len(members)!=0:
                        res=members[0][0]
                        c.execute("UPDATE books SET reserve=? WHERE id=?",(1,int(self.id2.get())))
                        c.execute("INSERT INTO records VALUES (?,?,?,?,?,?)",(id,bname,'reserve',res,datetime.now().strftime("%d-%b-%y"),datetime.now().strftime("%H:%M:%S")))
                        messagebox.showinfo('Success','Book successfully reserved!')
                    else:
                        messagebox.showerror('Unregistered','No such registered member!')
            else:
                messagebox.showerror('Not Availabe','Sorry the book with this id is already reserved!')

        def renew():
            id=int(self.id3.get())
            name=self.name3.get()
            with conn:
                c.execute("SELECT * FROM books WHERE id = ?",(id,))
            found=c.fetchall()
            print(found)
            if len(found)==0:
                messagebox.showerror('Not Availabe','Sorry the book with this id is not in library!')
            elif found[0][6]==1:
                with conn:
                    bname=found[0][1]
                    c.execute("SELECT * FROM members WHERE name = ?",(name,))
                    members = c.fetchall()
                    if len(members)!=0:
                        res=members[0][0]
                        c.execute("UPDATE books SET borrowed=? WHERE id=?",(2,int(self.id3.get())))
                        c.execute("INSERT INTO records VALUES (?,?,?,?,?,?)",(id,bname,'renew',res,datetime.now().strftime("%d-%b-%y"),datetime.now().strftime("%H:%M:%S")))
                        messagebox.showinfo('Success','Book successfully renewed!')
                    else:
                        messagebox.showerror('Unregistered','No such registered member!')
            else:
                messagebox.showerror('Not Availabe','Sorry the book with this id is not currently borrowed!')

        def returned():
            id=int(self.id4.get())
            name=self.name4.get()
            with conn:
                c.execute("SELECT * FROM books WHERE id = ?",(id,))
            found=c.fetchall()
            if len(found)==0:
                messagebox.showerror('Not Availabe','Sorry the book with this id is not in library!')
            elif found[0][6]!=0:
                with conn:
                    bname=found[0][1]
                    c.execute("SELECT * FROM members WHERE name = ?",(name,))
                    members = c.fetchall()
                    if len(members)!=0:
                        res=members[0][0]
                        c.execute("UPDATE books SET borrowed=? AND reserve=? WHERE id=?",(0,0,int(self.id4.get())))
                        c.execute("INSERT INTO records VALUES (?,?,?,?,?,?)",(id,bname,'return',res,datetime.now().strftime("%d-%b-%y"),datetime.now().strftime("%H:%M:%S")))
                        messagebox.showinfo('Success','Book successfully returned!')
                    else:
                        messagebox.showerror('Unregistered','No such registered member!')
            else:
                messagebox.showerror('Not Availabe','Sorry the book with this id is not currently borrowed!')


        self.destroy_frames()
        self.current_frame='manage'
        self.manage_frame=Frame(self.root)
        self.manage_frame.config(bg='#E0CCE3')
        self.manage_frame.place(x=450,y=130,width=700,height=520)
        label_head1=Label(self.manage_frame,text="Borrow Book",bg='#8C5394',fg='#FFFFFF',font=('Constantia',22))
        label_head1.place(x=0,y=0,height=50,width=700)
        label_id1=Label(self.manage_frame,text="Book ID:",bg='#FFF5CF',font=('Constantia',16))
        label_id1.place(x=20,y=80,height=30)
        self.id1=Entry(self.manage_frame)
        self.id1.place(x=120,y=80,height=30)
        label_name1=Label(self.manage_frame,text="Member name:",bg='#FFF5CF',font=('Constantia',16))
        label_name1.place(x=280,y=80,height=30)
        self.name1=Entry(self.manage_frame)
        self.name1.place(x=440,y=80,height=30)    
        b1=Button(self.manage_frame,text='Borrow',bg='#FFF5CF',font=('Constantia',12),command=borrow)
        b1.place(x=620,y=80,height=30)

        label_head2=Label(self.manage_frame,text="Reserve Book",bg='#8C5394',fg='#FFFFFF',font=('Constantia',22))
        label_head2.place(x=0,y=130,height=50,width=700)
        label_id2=Label(self.manage_frame,text="Book ID:",bg='#FFF5CF',font=('Constantia',16))
        label_id2.place(x=20,y=210,height=30)
        self.id2=Entry(self.manage_frame)
        self.id2.place(x=120,y=210,height=30)
        label_name2=Label(self.manage_frame,text="Member name:",bg='#FFF5CF',font=('Constantia',16))
        label_name2.place(x=280,y=210,height=30)
        self.name2=Entry(self.manage_frame)
        self.name2.place(x=440,y=210,height=30)    
        b2=Button(self.manage_frame,text='Reserve',bg='#FFF5CF',font=('Constantia',12),command=reserve)
        b2.place(x=620,y=210,height=30)

        label_head3=Label(self.manage_frame,text="Renew Book",bg='#8C5394',fg='#FFFFFF',font=('Constantia',22))
        label_head3.place(x=0,y=260,height=50,width=700)
        label_id3=Label(self.manage_frame,text="Book ID:",bg='#FFF5CF',font=('Constantia',16))
        label_id3.place(x=20,y=340,height=30)
        self.id3=Entry(self.manage_frame)
        self.id3.place(x=120,y=340,height=30)
        label_name3=Label(self.manage_frame,text="Member name:",bg='#FFF5CF',font=('Constantia',16))
        label_name3.place(x=280,y=340,height=30)
        self.name3=Entry(self.manage_frame)
        self.name3.place(x=440,y=340,height=30)    
        b3=Button(self.manage_frame,text='Renew',bg='#FFF5CF',font=('Constantia',12),command=renew)
        b3.place(x=620,y=340,height=30)

        label_head4=Label(self.manage_frame,text="Return Book",bg='#8C5394',fg='#FFFFFF',font=('Constantia',22))
        label_head4.place(x=0,y=390,height=50,width=700)
        label_id4=Label(self.manage_frame,text="Book ID:",bg='#FFF5CF',font=('Constantia',16))
        label_id4.place(x=20,y=460,height=30)
        self.id4=Entry(self.manage_frame)
        self.id4.place(x=120,y=460,height=30)
        label_name4=Label(self.manage_frame,text="Member name:",bg='#FFF5CF',font=('Constantia',16))
        label_name4.place(x=280,y=460,height=30)
        self.name4=Entry(self.manage_frame)
        self.name4.place(x=440,y=460,height=30)    
        b4=Button(self.manage_frame,text='Return',bg='#FFF5CF',font=('Constantia',12),command=returned)
        b4.place(x=620,y=460,height=30)

    def transaction(self):
        self.destroy_frames()
        self.current_frame='transact'

        self.style=ttk.Style()
        self.style.theme_use('default')
        self.style.configure('Treeview',
            background='#E0CCE3',
            foreground='black',
            rowheight=20,
            fieldbackground='D3D3D3'
            )
        self.style.map('Treeview',
            background=[('selected','#8C5394')])

        #Frame for treeview
        self.transact_frame=Frame(self.root)
        self.transact_frame.place(x=450,y=130,height=520,width=700)
        self.transact_frame.config(bg='#C2C2AE')

        #Scrollbar
        self.transact_scroll=Scrollbar(self.transact_frame)
        self.transact_scroll.pack(side=RIGHT,fill=Y)

        #Defining
        self.transact_tree=ttk.Treeview(self.transact_frame,yscrollcommand=self.transact_scroll.set,selectmode='browse')
        self.transact_tree['columns']=('Id','Name','Action','Member','Date','Time')
        self.transact_scroll.config(command=self.transact_tree.yview)

        #Formatting
        self.transact_tree.column('#0',width=0,stretch=NO)
        self.transact_tree.column('Id',anchor=CENTER,width=40)
        self.transact_tree.column('Name',anchor=CENTER,width=140)
        self.transact_tree.column('Action',anchor=CENTER,width=80)
        self.transact_tree.column('Member',anchor=CENTER,width=120)
        self.transact_tree.column('Date',anchor=CENTER,width=150)
        self.transact_tree.column('Time',anchor=CENTER,width=150)

        #Headings
        self.transact_tree.heading('#0',text='',anchor=W)
        self.transact_tree.heading('Id',text='Id',anchor=CENTER)
        self.transact_tree.heading('Name',text='Name',anchor=CENTER)
        self.transact_tree.heading('Action',text='Action',anchor=CENTER)
        self.transact_tree.heading('Member',text='Member',anchor=CENTER)
        self.transact_tree.heading('Date',text='Date',anchor=CENTER)
        self.transact_tree.heading('Time',text='Time',anchor=CENTER)
        self.transact_tree.place(x=0,y=0,height=520,width=683)

        #For Striped Treeview
        self.transact_tree.tag_configure('odd',background='#F5DCD0')
        self.transact_tree.tag_configure('even',background='#F5F5C4')   

        with conn:
            c.execute("SELECT * FROM records")
        items=c.fetchall()
        self.transact_tree.delete(*self.transact_tree.get_children())
        item_id=1
        if len(items)!=0:
            for item in items:
                if item_id%2==0:self.transact_tree.insert(parent='',index='end',iid=item_id,text='',values=(str(item[0]),str(item[1]),str(item[2]),str(item[3]),str(item[4]),str(item[5])),tags=('even',))
                else:self.transact_tree.insert(parent='',index='end',iid=item_id,text='',values=(str(item[0]),str(item[1]),str(item[2]),str(item[3]),str(item[4]),str(item[5])),tags=('odd',)) 
                item_id+=1                   
        else:
            self.transact_tree.insert(parent='',index='end',iid=item_id,text='',values=('No transactions to show!'))

    def log_out(self):
        '''This function destroys the window and logout the admin'''
        self.destroy_frames()
        self.root.destroy()

    def view_books(self):
        '''This function shows customer the items we are selling'''
        self.destroy_frames()
        self.load_product()
        self.current_frame='showbooks'

        # Frame for books
        self.books_frame=Frame(self.root)
        self.books_frame.place(x=450,y=130,width=700,height=520)
        self.books_frame.config(bg='#C2C2AE',highlightbackground='#8C5394',highlightthickness=2)

        #Canvas
        product_canvas=Canvas(self.books_frame)
        product_canvas.pack(side=LEFT,fill="both",expand="yes")

        #Scrollbar
        product_scroll=ttk.Scrollbar(self.books_frame,orient="vertical", command=product_canvas.yview)
        product_scroll.pack(side=RIGHT,fill="y")

        product_canvas.configure(yscrollcommand=product_scroll.set)
        product_canvas.bind('<Configure>',lambda e: product_canvas.configure(scrollregion=product_canvas.bbox('all')))
        
        #CanvasFrame
        canvas_frame=Frame(product_canvas)
        product_canvas.create_window((0,0),window=canvas_frame,anchor="nw")

        x=0
        for i in self.books:
            shoe_frame=Frame(canvas_frame)
            shoe_frame.config(bg='#E0CCE3',height=340,width=700,padx=10,pady=20,highlightbackground='#B08D95',highlightthickness=2)
            shoe_frame.grid(row=x,column=0)
            img = Image.open(self.books[i][3])
            img=img.resize((200,300),Image.ANTIALIAS)
            img=ImageTk.PhotoImage(img)
            label_img=Label(shoe_frame,image=img)
            label_img.photo=img
            label_img.place(x=10,y=0)
            name=Label(shoe_frame,text=str(self.books[i][0]),bg='#E0CCE3',font=('Poppins SemiBold',20))
            name.place(x=240,y=10)
            auth=Label(shoe_frame,text="Author: "+str(self.books[i][1]),bg='#E0CCE3',font=('Poppins Medium',12))
            auth.place(x=240,y=50)
            pub=Label(shoe_frame,text="Published: "+str(self.books[i][2]),bg='#E0CCE3',font=('Poppins Medium',14))
            pub.place(x=490,y=12)
            bid=Label(shoe_frame,text="ID: "+str(i),bg='#E0CCE3',font=('Poppins Medium',14))
            bid.place(x=490,y=74)
            desc_head=Label(shoe_frame,text="Description:",bg='#E0CCE3',font=('Poppins Medium',12))
            desc_head.place(x=240,y=80)
            desc=Message(shoe_frame,text=str(self.books[i][4]),bg='#E0CCE3',font=('Poppins Light',9),width=400)
            desc.place(x=240,y=100,height=120)
            rating=Label(shoe_frame,text=str(self.books[i][7])+'✩',bg='#E0CCE3',font=('Poppins Medium',14))
            rating.place(x=490,y=44)
            x+=1

    def loggedin_admin(self):
        '''This function initiates admin panel creating interface'''
        self.root.destroy() 
        self.current_frame=None
        self.root=Tk()
        self.root.title('Air It')
        self.root.geometry('1200x700')
        # self.root.iconbitmap('CS20098.ico')
        self.root.configure(bg='#F9F0FA')
        self.root.resizable(0,0)
        self.f=Frame(self.root,bg="#c5bec6") 
        self.f.place(x=0,y=0,width=1200,height=80)
        self.k=Frame(self.root,bg="#8C5394") 
        self.k.place(x=310,y=0,width=640,height=80)
        img = Image.open('images/book.png')
        img=img.resize((120,90),Image.ANTIALIAS)
        img=ImageTk.PhotoImage(img)
        label_img=Label(self.f,image=img)
        label_img.photo=img
        label_img.place(x=-2,y=-12)
    
        mem = Image.open('images/mem.png')
        mem = mem.resize((26,26),Image.ANTIALIAS)
        mem=ImageTk.PhotoImage(mem)
        mem_bt=Button(self.f ,image=mem,bg='#8C5394')
        mem_bt.photo=mem
        mem_bt.config(command=self.show_members)
        mem_bt.place(x=1060,y=25)

        add_mem = Image.open('images/add_mem.png')
        add_mem = add_mem.resize((26,26),Image.ANTIALIAS)
        add_mem=ImageTk.PhotoImage(add_mem)
        mem_bt=Button(self.f ,image=add_mem,bg='#8C5394')
        mem_bt.photo=add_mem
        mem_bt.config(command=self.add_members)
        mem_bt.place(x=1020,y=25)


        self.l=Label(self.root,text='Library Management System',font=('Eras Demi ITC',36),bg='#c5bec6',fg='#4e2f25')
        self.l.place(x=300,y=10)
        bkg=Frame(self.root,bg="#8C5394") 
        bkg.place(x=50,y=130,width=300,height=520)
        menu=Label(self.root,text='MENU',font=('Constantia',32),fg='#4e2f25',bg='#E0CCE3')
        menu.place(x=50,y=140,width=300,height=80)
        option1=Button(text='Show books',font=('Constantia',14,'italic'),fg='#4e2f25',bg='#E0CCE3',command=self.view_books)
        option1.place(x=50,y=230,width=300,height=40)
        option10=Button(text='Edit book',font=('Constantia',14,'italic'),fg='#4e2f25',bg='#E0CCE3',command=self.update_book)
        option10.place(x=50,y=290,width=300,height=40)
        option2=Button(text='Add Book',font=('Constantia',14,'italic'),fg='#4e2f25',bg='#E0CCE3',command=self.add_book)
        option2.place(x=50,y=350,width=300,height=40)
        option3=Button(text='Search in Library',font=('Constantia',14,'italic'),fg='#4e2f25',bg='#E0CCE3',command=self.search)
        option3.place(x=50,y=410,width=300,height=40)
        option4=Button(text='Remove Book',font=('Constantia',14,'italic'),fg='#4e2f25',bg='#E0CCE3',command=self.remove_book)
        option4.place(x=50,y=470,width=300,height=40)
        option5=Button(text='Recent Transactions',font=('Constantia',14,'italic'),fg='#4e2f25',bg='#E0CCE3',command=self.transaction)
        option5.place(x=50,y=530,width=300,height=40)
        option7=Button(self.root,text='Manage Books',font=('Constantia',14,'italic'),fg='#4e2f25',bg='#E0CCE3',command=self.manage)
        option7.place(x=50,y=590,width=300,height=40)
        option8=Button(self.root,text='Log Out',font=('Constantia',14,'italic'),fg='#c5bec6',bg='#4e2f25',command=self.log_out)
        option8.place(x=1100,y=25,width=80,height=30)
        self.view_books()
     
class Account(Admin):
    '''This account class inherits from customer and admin class, it instantiate the initial login/signup window'''
    def __init__(self):
        Books.__init__(self)

    def logged_in(self):
        '''This function checks whether to open admin or customer panel and then opens the panel according to given credentials'''
        if (self.entry_user.get() =='admin') and (self.entry_pass.get()=='admin'):
            Admin.loggedin_admin(self) 
        else: messagebox.showinfo("Incorrect Data", "No admin with such id or password exists!")

    def login_window(self):
        '''Allows the customer/admin to login if they have an account, otherwisw allowing to create one'''
        self.root = Tk()
        self.root.title("LMS Admin Panel")
        self.root.geometry('500x350')
        self.root.resizable(0,0)
        self.root.configure(bg='#F9F0FA')
        bg = PhotoImage(file="images/login_bg.png")
        canvas1 = Canvas( self.root, width = 400,height = 400)
        canvas1.pack(fill = "both", expand = True)
        canvas1.create_image( 0, 0, image = bg,anchor = "nw")
        img = Image.open('images/book.png')
        img=img.resize((100,75),Image.ANTIALIAS)
        img=ImageTk.PhotoImage(img)
        label_img=Label(canvas1,image=img)
        label_img.photo=img
        label_img.place(x=-2,y=-12)
        self.l=Label(self.root,text='LMS Admin Panel',font=('Eras Demi ITC',34),bg='#FFFFFF',fg='#4e2f25')
        self.l.place(x=110,y=10)
        label_user=Label(self.root,text="Username:",bg='#FFF5CF',font=('Constantia',16))
        label_user.place(x=120,y=130)
        self.entry_user=Entry(self.root)
        self.entry_user.place(x=250,y=140)
        label_pass=Label(self.root,text="Password:",bg='#FFF5CF',font=('Constantia',16))
        label_pass.place(x=120,y=170)
        self.entry_pass=Entry(self.root)
        self.entry_pass.place(x=250,y=180)
        b_log=Button(self.root,text="Log in",font=('Constantia',16),bg='#523A28',fg='#FFFFFF',command=self.logged_in)
        b_log.place(x=200,y=240)
        self.root.mainloop()

#Initiating the code
m=Account()
m.login_window()

# Coded by
#Muhammad Faizan
#CS-20098