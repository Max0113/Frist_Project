from tkinter import *
from tkinter import ttk
import tkinter as tk
# import Gema

win1 = Tk()


win1.geometry('500x500')
win1.resizable(width=False,height=False)
win1.title('set_web')

    

Far = Frame(win1 ,width=500, height=50,bg='black')
Far.pack(fill=Y)

Logo = Label(Far, text="younes" ,bg="#000000" ,fg="#ffffff")
Logo.place(x=15,y=15)

  
Text1 = Label(Far , text="Home" ,bg="#000000" ,fg="#ffffff")
Text1.place(x=230,y=15)
Text2 = Label(Far , text="Home" ,bg="#000000" ,fg="#ffffff")
Text2.place(x=300,y=15)
Text3 = Label(Far , text="Home" ,bg="#000000" ,fg="#ffffff")
Text3.place(x=365,y=15)
Text4 = Label(Far , text="Home" ,bg="#000000" ,fg="#ffffff")
Text4.place(x=430,y=15)

Far2 = Frame(win1,width=500,height=500,bg="#ff0000")
Far2.pack()


def new_window() :
    win = Tk()
    win.title('LOGIN SYSTEM')
    win.geometry('500x500')
    win.resizable(width=False,height=False)
    win.config(bg='#368ABF')
    #------ Text -------
    title = Label(win,text="LOGIN WINDOWE" , bg='black' ,fg='white',font=('Freestyle Script',15))
    title.pack(fill=X)
    #------ Farme ------
    Farm = Frame(win, width='300', height='350')
    Farm.pack(padx=30,pady=55)
    #------ imge -------
    # img = PhotoImage(file='C:\\Users\\Gk\\Desktop\\younes\\Codhub\\My_Frist_Project\\Tkinter\\man.png')
    # size = img.subsample(5,5)
    # plant = Label(Farm, image=img)
    # plant.place(x=100,y=10)
    #----- label ------
    text11 = Label(Farm,text="USERNAME :",font=('Century',15))
    text11.place(x=10,y=150)
    text22 = Label(Farm,text="PASSWORD :",font=('Century',15))
    text22.place(x=10,y=190)
    #----- INPUT ------
    input11 = Entry(Farm)
    input11.place(x=150,y=155)
    input22 = Entry(Farm)
    input22.place(x=150,y=195)
    #----- checkbutton ---
    check = Checkbutton(Farm,text="Forget password !!",font=('Century',15))
    check.place(x=40,y=220)
    #----- Button ----
    button1 = Button(Farm,text="Login",width=10,font=('Century',15))
    button1.place(x=10,y=260)
    button1 = Button(Farm,text="Sigin",width=10,font=('Century',15))
    button1.place(x=150,y=260)
    win.mainloop()

button = Button(Far2,text='Sigin up',command=new_window,bg="red")
button.place(x=230,y=200)

text5 = Label(Far2,text="helle to mon sitweb !!",font=('Century',15) ,bg="#ff0000",fg="#ffffff")
text5.place(x=150,y=150)



win1.mainloop()



