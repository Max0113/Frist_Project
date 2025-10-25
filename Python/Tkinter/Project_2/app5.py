from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pymysql

class student :
    def __init__(self,win):
        self.win = win
        self.win.geometry("1350x700")
        self.win.config(bg="#e6e6e6")
        self.win.title("student app")
        self.win.resizable(False,False)
        title = Label(self.win , text="نظام تسجيل الطلاب" ,bg="#0096b8" ,fg="#ffffff")
        title.pack(fill=X)
        # ----------- varaible ----------

        self.ID_var = StringVar()
        self.Name_var = StringVar()
        self.Email_var = StringVar()
        self.Phone_var = StringVar()
        self.Qualifications_var = StringVar()
        self.Sex_var = StringVar()
        self.Addresse_var = StringVar()
        self.Delete_var = StringVar()

        self.Search_var = StringVar()
        self.choase_var = StringVar()

        # ----------- أدوات تحكم بالبرنامج --------------

        fram = Frame(self.win , bg="#ffffff")
        fram.place(x=1096,y=25,width=250,height=420)
        
        lbl_ID = Label(fram, text="الرقم التسلسلي" ,bg="#ffffff")
        lbl_ID.pack()
        ID_Entry = Entry(fram,textvariable=self.ID_var , bd=2 , justify="center")
        ID_Entry.pack()

        lbl_Name = Label(fram, text="اسم الطالب" ,bg="#ffffff")
        lbl_Name.pack()
        Name_Entry = Entry(fram, bd=2 ,textvariable=self.Name_var , justify="center")
        Name_Entry.pack()

        lbl_Email = Label(fram , text="ايميل الطالب" ,bg="#ffffff")
        lbl_Email.pack()
        Email_Entry = Entry(fram,textvariable=self.Email_var, bd=2 , justify="center")
        Email_Entry.pack()

        lbl_Phone = Label(fram , text="هاتف الطالب" ,bg="#ffffff")
        lbl_Phone.pack()
        Phone_Entry = Entry(fram, textvariable=self.Phone_var ,bd=2 , justify="center")
        Phone_Entry.pack()

        lbl_qualifications = Label(fram, text="مؤهلات الطالب" ,bg="#ffffff")
        lbl_qualifications.pack()
        qualifications_Entry = Entry(fram, textvariable=self.Qualifications_var , bd=2 , justify="center")
        qualifications_Entry.pack()

        lbl_Sex = Label(fram, text="جنس الطالب" ,bg="#ffffff")
        lbl_Sex.pack()
        array = ("male","famille")
        choasie = ttk.Combobox(fram,values=(array),textvariable=self.Sex_var)
        choasie.pack()

        lbl_Addresse = Label(fram, text="عنوان الطالب" ,bg="#ffffff")
        lbl_Addresse.pack()
        Addresse_Entry = Entry(fram, textvariable=self.Addresse_var , bd=2 , justify="center")
        Addresse_Entry.pack()

        lbl_delete = Label(fram, text="حدف الطالب" ,bg="#ffffff" , fg="red")
        lbl_delete.pack()
        delete_Entry = Entry(fram, textvariable=self.Delete_var , bd=2 , justify="center")
        delete_Entry.pack()

        # -------- Button ---------

        fram1 = Frame(self.win, bg="#ffffff")
        fram1.place(x=1096,y=450,width=250,height=243)

        title1 = Label(fram1,text="لوحة التحكم",bg="#2877ff" ,fg="#ffffff",font=("29LT Azer",15))
        title1.pack(fill=X)
        
        lbl_Button1 = Button(fram1,text="اضافة الطالب",width=20,bg="#949191" ,fg="#ffffff",command=self.add_student)
        lbl_Button1.pack(pady=5)

        lbl_Button2 = Button(fram1,text="حدف الطالب",width=20,bg="#949191",fg="#ffffff",command=self.delete)
        lbl_Button2.pack(pady=5)

        lbl_Button3 = Button(fram1,text="تعديل بيانات الطالب",width=20,bg="#949191",fg="#ffffff",command=self.updata)
        lbl_Button3.pack(pady=5)

        lbl_Button4 = Button(fram1,text="افراغ الحقول",width=20,bg="#949191",fg="#ffffff",command=self.clear)
        lbl_Button4.pack(pady=5)

        lbl_Button5 = Button(fram1,text="من نحن",width=20,bg="#949191",fg="#ffffff", command=self.developement_all)
        lbl_Button5.pack(pady=5)

        lbl_Button6 = Button(fram1,text="اغلاق البرنامج",width=20,bg="#949191",fg="#ffffff",command=quit)
        lbl_Button6.pack(pady=5)


        # ---------- search bar -------------

        search_farm = Label(self.win,bg="#ffffff")
        search_farm.place(x=4,y=25,width=1087,height=52)

        text = Label(search_farm,text="البحث عن طالب",bg="#ffffff")
        text.place(x=980,y=12)
 
        array1 = ("id","name","email","phone")
        choasie = ttk.Combobox(search_farm, textvariable=self.choase_var ,values=(array1))
        choasie.place(x=820,y=12)

        Search_Entry = Entry(search_farm, textvariable=self.Search_var , bd=2 , justify="left")
        Search_Entry.place(x=670,y=13)

        Search_Button = Button(search_farm, text="البحث",width=15,bg="#6bbaff",command=self.search_all)
        Search_Button.place(x=530,y=10)

        # -------- databise ----------

        fram_databise = Frame(self.win, bg="#D7D7D7")
        fram_databise.place(x=4,y=81,width=1087,height=612)

        # -------- scroll ----------

        scroll_x = Scrollbar(fram_databise,orient=HORIZONTAL)
        scroll_y = Scrollbar(fram_databise,orient=VERTICAL)

        # -------- Table -----------

        self.student_table = ttk.Treeview(fram_databise,
        columns=("id","name","email","phone","certi","gender","address"),
        xscrollcommand=scroll_x.set,
        yscrollcommand=scroll_y.set)

        self.student_table.place(x=17,y=1,width=1120,height=593)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=LEFT,fill=Y)

        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table["show"] = "headings"
        self.student_table.heading('id', text="ID")
        self.student_table.heading('name', text="اسم الطالب")
        self.student_table.heading('email', text="ايميل الطالب")
        self.student_table.heading('phone', text="هاتف الطالب")
        self.student_table.heading('certi', text="مؤهلات الطالب")
        self.student_table.heading('gender', text="جنس الطالب")
        self.student_table.heading('address', text="عنوان الطالب")

        self.student_table.column('id', width=50)
        self.student_table.column('name', width=100)
        self.student_table.column('email', width=150)
        self.student_table.column('phone', width=100)
        self.student_table.column('certi', width=120)
        self.student_table.column('gender', width=80)
        self.student_table.column('address', width=150)
        self.student_table.bind("<ButtonRelease-1>",self.get_cursor)

        self.fetch_all()
        

    # -------- connect -----------
    
    def add_student(self) :
        con = pymysql.connect(host = 'localhost',
            user = 'root',
            password = '',
            database = 'stud')
        cur = con.cursor()
        cur.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s)",(
            self.ID_var.get(),
            self.Name_var.get(),
            self.Email_var.get(),
            self.Phone_var.get(),
            self.Qualifications_var.get(),
            self.Sex_var.get(),
            self.Addresse_var.get(),
        ))
        con.commit()
        self.fetch_all()
        con.close()
        messagebox.showinfo("root","Added successfully.")
        

    def fetch_all(self) :
        con = pymysql.connect(host = 'localhost',
            user = 'root',
            password = '',
            database = 'stud')
        cur = con.cursor()
        cur.execute("select * from student")
        rows = cur.fetchall()
        if len(rows) != 0 :
            self.student_table.delete(*self.student_table.get_children())
            for row in rows :
                self.student_table.insert("",END,values=row)
            con.commit()
        con.close()
    
    def delete(self) :
        con = pymysql.connect(host = 'localhost',
            user = 'root',
            password = '',
            database = 'stud')
        cur = con.cursor()
        cur.execute('delete from student where ID=%s', (self.Delete_var.get(),))
        con.commit()
        self.fetch_all()
        con.close()
        messagebox.showinfo("root","Deleted successfully.")
    
    def clear(self) :
        self.Name_var.set("")
        self.ID_var.set("")
        self.Addresse_var.set("")
        self.Sex_var.set("")
        self.Email_var.set("")
        self.Delete_var.set("")
        self.Qualifications_var.set("")
        self.Phone_var.set("")

    def get_cursor(self,ev) :
        cursor_row = self.student_table.focus()
        cursor = self.student_table.item(cursor_row)
        row = cursor["values"]
        self.ID_var.set(row[0])
        self.Name_var.set(row[1])
        self.Email_var.set(row[2])
        self.Phone_var.set(row[3])
        self.Qualifications_var.set(row[4])
        self.Sex_var.set(row[5])
        self.Addresse_var.set(row[6])

    def updata(self):
        con = pymysql.connect(host='localhost',
                            user='root',
                            password='',
                            database='stud')
        cur = con.cursor()
        cur.execute("""
                update student set
                name=%s,
                email=%s,
                phone=%s,
                sex=%s,
                moahle=%s,
                address=%s
            where id=%s
        """, (
            self.Name_var.get(),
            self.Email_var.get(),
            self.Phone_var.get(),
            self.Qualifications_var.get(),
            self.Sex_var.get(),
            self.Addresse_var.get(),
            self.ID_var.get()
        ))
        con.commit()
        self.fetch_all()  # تحديث الجدول فـ Tkinter
        self.clear()      # مسح الحقول
        con.close()
        messagebox.showinfo("root","The change was successful.")

    def search_all(self) :
        con = pymysql.connect(host='localhost',
                            user='root',
                            password='',
                            database='stud')
        cur = con.cursor()
        search_by = str(self.choase_var.get())
        search_for = str(self.Search_var.get())
        if search_by != '' and search_for !='' :
            quer = "SELECT * FROM student WHERE " + search_by + " LIKE %s"
            cur.execute(quer, ("%" + search_for + "%",))
        else :
            cur.execute("SELECT * FROM student")
        rows = cur.fetchall()
        if len(rows) != 0 :
            self.student_table.delete(*self.student_table.get_children())
            for row in rows :
                self.student_table.insert("",END,values=row)
            con.commit()
        con.close()

    def developement_all(self) :
        messagebox.showinfo("devloper youness amzil","welcome to my first project")
        




win = Tk()
student1 = student(win)
win.mainloop()
        