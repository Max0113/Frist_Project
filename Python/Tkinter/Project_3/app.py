from tkinter import *
from tkinter import messagebox
import os
import webbrowser
import sys

# ----- window --------
win = Tk()
win.geometry('800x450')
win.resizable(False,False)
win.title("SUPERMARKET")
win.iconbitmap("C:\\Users\\Gk\\Desktop\\younes\\Codhub\\My_Frist_Project\\Tkinter\\Project_3\\shops.ico")
# win.iconbitmap("C:\\Users\\amzil\\Desktop\\Codhub\\My_Frist_Project\\Tkinter\\Project_3\\shops.ico")

# ------- Variables ------

Name = StringVar()
Passowrd = StringVar()

# ------ methode -------

u1 = 'https://www.facebook.com/'
u2 = 'https://web.telegram.org/'
u3 = 'https://www.youtube.com/'
def open1() :
    webbrowser.open_new(u1)
def open2() :
    webbrowser.open_new(u2)
def open3() :
    webbrowser.open_new(u3)

def information_developer() :
    messagebox.showinfo("information de developrer","Younes Amzil j'ai 14 ans")

def information_Project() :
    messagebox.showinfo("information de Project","c'est la deuxeme project pour moi")
    
def log() :
    user = Enter1.get()
    passw = Enter2.get()
    if user == 'younes' and passw == '123456' :
        messagebox.showinfo("programme","login he is succese")
        import super
    else :
        messagebox.showinfo("programme","login he is Error")

# -------- nevbar --------

nevbar = Label(win,text="Super Market System",bg="#000000",fg="#f2ff00",font=("tajawal",15,'bold'))
nevbar.pack(fill=X)

# -------- Farm1 ---------

farm1 = Frame(win,bg="#002C5F")
farm1.place(x=571,y=35,width=230,height=450)

Title1 = Label(farm1,text="مشروع سوبرماركت",bg="#002C5F",font=("tajawal",11,'bold'),fg="#ffffff")
Title1.pack(pady=8)

Title2 = Label(farm1,text="المطور يونس",bg="#002C5F",font=("tajawal",11,'bold'),fg="#ffffff")
Title2.pack(pady=8)

Title3 = Label(farm1,text= "وسايل تواصل بنا",bg="#002C5F",font=("tajawal",11,'bold'),fg="#ffffff")
Title3.pack(pady=8)

button1 = Button(farm1,text= "حسابنا علي فايسبوك",bg="#d2a500",font=("tajawal",10,'bold'), width=30, command=open1)
button1.pack(pady=7)

button2 = Button(farm1,text= "حسابنا علي تيليعرام",bg="#d2a500",font=("tajawal",10,'bold'), width=30 , command=open2)
button2.pack(pady=7)

button3 = Button(farm1,text= "حسابنا علي يوتيوب",bg="#d2a500",font=("tajawal",10,'bold'), width=30, command=open3)
button3.pack(pady=7)

button4 = Button(farm1,text= "لمحة عن المطور",bg="#d2a500",font=("tajawal",10,'bold'), width=30,command=information_developer)
button4.pack(pady=7)

button5 = Button(farm1,text= "لمحة عن المشرع",bg="#d2a500",font=("tajawal",10,'bold'), width=30,command=information_Project)
button5.pack(pady=7)

button6 = Button(farm1,text= "اغلاق البرنامج",bg="#d2a500" ,font=("tajawal",10), width=30, command=quit)
button6.pack(pady=7)

Image1 = PhotoImage(file="C:\\Users\\Gk\\Desktop\\younes\\Codhub\\My_Frist_Project\\Tkinter\\Project_3\\store.png")
# Image1 = PhotoImage(file="C:\\Users\\amzil\\Desktop\\Codhub\\My_Frist_Project\\Tkinter\\Project_3\\store.png")
size = Image1.subsample(2,2)
imo = Label(win,image=size)
imo.place(x=150,y=43) 

farm2 = Frame(win,bg="#002C5F")
farm2.place(x=0,y=310,width=575,height=160)

Image2 = PhotoImage(file="C:\\Users\\Gk\\Desktop\\younes\\Codhub\\My_Frist_Project\\Tkinter\\Project_3\\person.png")
# Image2 = PhotoImage(file="C:\\Users\\amzil\\Desktop\\Codhub\\My_Frist_Project\\Tkinter\\Project_3\\person.png")
size2 = Image2.subsample(4,4)
imo2 = Label(farm2,image=size2 ,background="#d2a500")
imo2.place(x=430,y=5)

Title1 = Label(farm2,text=" :  اسم المستخدم", bg="#002C5F", font=("tajawal",15,'bold'), fg="#000000")
Title1.place(x=260,y=30)
Enter1 = Entry(farm2,textvariable=Name)
Enter1.place(x=130,y=40)

Title2 = Label(farm2,text=" :  كـــــــــــــــــــلمة المرور", bg="#002C5F", font=("tajawal",15,'bold'), fg="#000000")
Title2.place(x=260,y=70)
Enter2 = Entry(farm2,textvariable=Passowrd)
Enter2.place(x=130,y=80)

button_Entry = Button(farm2,text="تسجيل الدخول",bg="#d2a500",width=15,height=4 , command=log)
button_Entry.place(x=9,y=35)

win.mainloop() 