from tkinter import *
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
img = PhotoImage(file='C:\\Users\\Gk\\Desktop\\younes\\Codhub\\My_Frist_Project\\Tkinter\\man.png')
size = img.subsample(5,5)
plant = Label(Farm, image=size)
plant.place(x=100,y=10)
#----- label ------
text11 = Label(Farm,text="USERNAME :",font=('Century',15))
text11.place(x=10,y=150)
text22 = Label(Farm,text="PASSWORD :",font=('Century',15))
text22.place(x=10,y=190)
#----- INPUT ------
input1 = Entry(Farm)
input1.place(x=150,y=155)
input2 = Entry(Farm)
input2.place(x=150,y=195)
#----- checkbutton ---
check = Checkbutton(Farm,text="Forget password !!",font=('Century',15))
check.place(x=40,y=220)
#----- Button ----
button1 = Button(Farm,text="Login",width=10,font=('Century',15))
button1.place(x=10,y=260)
button1 = Button(Farm,text="Sigin",width=10,font=('Century',15))
button1.place(x=150,y=260)
win.mainloop()