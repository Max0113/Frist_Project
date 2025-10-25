from tkinter import *
from tkinter import messagebox
import tkinter as tk
import random
 
class super :
    def __init__(self):
        self.root = Tk()
        self.root.geometry("1300x700+30+10")
        self.root.title('Super-Market')
        self.root.resizable(False,False)

        title = Label(self.root,text="Welcome to Super-Market" ,fg="#ffffff",bg="#0B2F3A",font=("tajawal",12))
        title.pack(fill=X)

        # ______ Variables-Part(données d'inscription) ______

        self.NameSubscriber = StringVar()
        self.NumberSubscriber = StringVar()
        self.NumberInvoice = IntVar()
        x = random.randint(1000,9999)
        self.NumberInvoice.set(x)

        # ______ Variables-Part(Price) ______

        self.AccountLegumes = StringVar()
        self.AccountSupplies = StringVar()
        self.AccountElectric = StringVar() 

        # ______ Variables-Part(Legumes[G1 -> G17]) ______

        self.G1 = IntVar()
        self.G2 = IntVar()
        self.G3 = IntVar()
        self.G4 = IntVar()
        self.G5 = IntVar()
        self.G6 = IntVar()
        self.G7 = IntVar()
        self.G8 = IntVar()
        self.G9 = IntVar()
        self.G10 = IntVar()
        self.G11 = IntVar()
        self.G12 = IntVar()
        self.G13 = IntVar()
        self.G14 = IntVar()
        self.G15 = IntVar()
        self.G16 = IntVar()
        self.G17 = IntVar()

        # ______ Variables-Part(Supplies[S1 -> S17]) ______

        self.S1 = IntVar()
        self.S2 = IntVar()
        self.S3 = IntVar()
        self.S4 = IntVar()
        self.S5 = IntVar()
        self.S6 = IntVar()
        self.S7 = IntVar()
        self.S8 = IntVar()
        self.S9 = IntVar()
        self.S10 = IntVar()
        self.S11 = IntVar()
        self.S12 = IntVar()
        self.S13 = IntVar()
        self.S14 = IntVar()
        self.S15 = IntVar()
        self.S16 = IntVar()
        self.S17 = IntVar()
        
        # ______ Variables-Part(Electric[E1 -> E13]) ______

        self.E1 = IntVar()
        self.E2 = IntVar()
        self.E3 = IntVar()
        self.E4 = IntVar()
        self.E5 = IntVar()
        self.E6 = IntVar()
        self.E7 = IntVar()
        self.E8 = IntVar()
        self.E9 = IntVar()
        self.E10 = IntVar()
        self.E11 = IntVar()
        self.E12 = IntVar()
        self.E13 = IntVar()

        # ______ données d'inscription _______

        Frame_Inscription = Frame(self.root, bg="#004D64" )
        Frame_Inscription.place(x=961,y=29,width=338,height=180)

        Title_Frame_IN = Label(Frame_Inscription,text=": بيانات المشتري",bg="#004D64" ,fg="#D4B100",font=("tajawal",12,"bold"))
        Title_Frame_IN.place(x=200,y=10)

        Title_Entry1_IN = Label(Frame_Inscription,text=": اسم المشترك",bg="#004D64" ,fg="#FFFFFF",font=("tajawal",12))
        Title_Entry1_IN.place(x=200+20,y=50)
        Entry1_IN = Entry(Frame_Inscription, justify="center", textvariable=self.NameSubscriber)
        Entry1_IN.place(x=70+25,y=50+5)


        Title_Entry2_IN = Label(Frame_Inscription,text=": رقم المشترك",bg="#004D64" ,fg="#FFFFFF",font=("tajawal",12))
        Title_Entry2_IN.place(x=206+20,y=80)
        Entry2_IN = Entry(Frame_Inscription,justify="center", textvariable=self.NumberSubscriber)
        Entry2_IN.place(x=70+25,y=80+5)

        Title_Entry3_IN = Label(Frame_Inscription,text=": رقم الفاتورة",bg="#004D64" ,fg="#FFFFFF",font=("tajawal",12))
        Title_Entry3_IN.place(x=217+20,y=110)
        Entry3_IN = Entry(Frame_Inscription,justify="center", textvariable=self.NumberInvoice)
        Entry3_IN.place(x=70+25,y=110+5)

        Button_IN = Button(Frame_Inscription,text="بحت",bg="#ffffff",fg="#000000",width=10,height=4, command=self.welcome) 
        Button_IN.place(x=5+5,y=55+5)

        # ____________ BoxText _______________

        Title_TextBox = Label(Frame_Inscription,text="[الفواتير]" ,font=("tajawal",15,"bold") ,bg="#004D64",fg="#d4ff00")
        Title_TextBox.place(x=130,y=145)

        Frame_BoxText = Frame(self.root, bg="#FFFFFF" )
        Frame_BoxText.place(x=961,y=210,width=338,height=330)

        self.BoxText = tk.Text(Frame_BoxText , width=39 , height=20)
        self.BoxText.place(x=21,y=1)

        Scrollbar_BoxText = Scrollbar(Frame_BoxText,orient=VERTICAL, command=self.BoxText.yview)
        Scrollbar_BoxText.place(x=1,y=1,height=327)

        self.BoxText.config(yscrollcommand=Scrollbar_BoxText.set)

        self.BoxText.delete('1.0',END)
        self.BoxText.insert(END , "====================================")
        self.BoxText.insert(END , f"\n Name :")
        self.BoxText.insert(END , f"\n Phone :")
        self.BoxText.insert(END , f"\n num_bill :")
        self.BoxText.insert(END , "\n====================================")
        self.BoxText.insert(END , "\n Fatore : ")
        self.BoxText.insert(END , "\n Peice : ")
        
        # __________ Price ______________

        Frame_Price = Frame(self.root,bg="#004D64")
        Frame_Price.place(x=619,y=543,height=156,width=680)

        Button1_Price = Button(Frame_Price,text="الحساب",bg="#D4B100",fg="#000000",height=1,width=13,font=("tajawal",12),command=self.Price)
        Button1_Price.place(x=470+80,y=30+6)

        Button2_Price = Button(Frame_Price,text="افراغ الحقول",bg="#D4B100",fg="#000000",height=1,width=13,font=("tajawal",12),command=self.delate)
        Button2_Price.place(x=400-50+80,y=30+6)

        Button3_Price = Button(Frame_Price,text="تصدير الفاتورة",bg="#D4B100",fg="#000000",height=1,width=13,font=("tajawal",12))
        Button3_Price.place(x=470+80,y=80+6)

        Button4_Price = Button(Frame_Price,text="اغلاق البرنامج",bg="#D4B100",fg="#000000",height=1,width=13,font=("tajawal",12),command=quit)
        Button4_Price.place(x=400-50+80,y=80+6)
        
        Title1_Price = Label(Frame_Price,text="حساب الكلي للبقوليات",bg="#004D64",fg="#D4B100",font=("tajawal",11,"bold") )
        Title1_Price.place(x=180+40,y=36)

        Title1_Price = Label(Frame_Price,text="حساب اللوازم المنزلية",bg="#004D64",fg="#D4B100",font=("tajawal",11,"bold") )
        Title1_Price.place(x=183+40,y=36+30)

        Title1_Price = Label(Frame_Price,text="حساب ادوات الكهرباء",bg="#004D64",fg="#D4B100",font=("tajawal",11,"bold") )
        Title1_Price.place(x=185+40,y=36+60)

        Entry1_Price = Entry(Frame_Price, justify="center" , textvariable=self.AccountLegumes)
        Entry1_Price.place(x=40,y=40,width=150)

        Entry1_Price = Entry(Frame_Price, justify="center" , textvariable=self.AccountSupplies)
        Entry1_Price.place(x=40,y=73,width=150)

        Entry1_Price = Entry(Frame_Price, justify="center" , textvariable=self.AccountElectric)
        Entry1_Price.place(x=40,y=106,width=150)

        # _________ Legumes ________

        Frame_Legumes = Frame(self.root,bg="#004D64")
        Frame_Legumes.place(x=5,y=29,height=670,width=300)

        Title_Legumes = Label(Frame_Legumes,text="البقوليات",bg="#004D64",fg="#C7D503",font=("tajawal",15,"bold"))
        Title_Legumes.pack()

        Text1_Legumes = Label(Frame_Legumes,text=" : الرز",bg="#004D64",fg="#ffffff",font=("tajawal",12))
        Text1_Legumes.place(x=210+30,y=50)
        Entry1_Legumes = Entry(Frame_Legumes,justify="center",textvariable=self.G1)
        Entry1_Legumes.place(x=40,y=54,width=100)

        Text2_Legumes = Label(Frame_Legumes,text=" : برغل",bg="#004D64",fg="#ffffff",font=("tajawal",12))
        Text2_Legumes.place(x=196+30,y=50+30)
        Entry2_Legumes = Entry(Frame_Legumes,justify="center",textvariable=self.G2)
        Entry2_Legumes.place(x=40,y=54+30,width=100)

        Text3_Legumes = Label(Frame_Legumes,text=" : الفاصولياء",bg="#004D64",fg="#ffffff",font=("tajawal",12))
        Text3_Legumes.place(x=191,y=50+60)
        Entry3_Legumes = Entry(Frame_Legumes,justify="center",textvariable=self.G3)
        Entry3_Legumes.place(x=40,y=54+60,width=100)

        Text4_Legumes = Label(Frame_Legumes,text=" : عدس",bg="#004D64",fg="#ffffff",font=("tajawal",12))
        Text4_Legumes.place(x=220,y=50+90)
        Entry4_Legumes = Entry(Frame_Legumes,justify="center",textvariable=self.G4)
        Entry4_Legumes.place(x=40,y=54+90,width=100)

        Text5_Legumes = Label(Frame_Legumes,text=" : معكرونة",bg="#004D64",fg="#ffffff",font=("tajawal",12))
        Text5_Legumes.place(x=200,y=50+120)
        Entry5_Legumes = Entry(Frame_Legumes,justify="center",textvariable=self.G5)
        Entry5_Legumes.place(x=40,y=54+120,width=100)

        Text6_Legumes = Label(Frame_Legumes,text=" : فريكة",bg="#004D64",fg="#ffffff",font=("tajawal",12))
        Text6_Legumes.place(x=220,y=50+150)
        Entry6_Legumes = Entry(Frame_Legumes,justify="center",textvariable=self.G6)
        Entry6_Legumes.place(x=40,y=54+150,width=100)

        Text7_Legumes = Label(Frame_Legumes,text=" : حمض",bg="#004D64",fg="#ffffff",font=("tajawal",12))
        Text7_Legumes.place(x=215,y=50+180)
        Entry7_Legumes = Entry(Frame_Legumes,justify="center",textvariable=self.G7)
        Entry7_Legumes.place(x=40,y=54+180,width=100)


        Text8_Legumes = Label(Frame_Legumes,text=" : فول",bg="#004D64",fg="#ffffff",font=("tajawal",12))
        Text8_Legumes.place(x=225,y=50+230)
        Entry8_Legumes = Entry(Frame_Legumes,justify="center",textvariable=self.G8)
        Entry8_Legumes.place(x=40,y=54+230,width=100)

        Text9_Legumes = Label(Frame_Legumes,text=" : الملح",bg="#004D64",fg="#ffffff",font=("tajawal",12))
        Text9_Legumes.place(x=217,y=50+260)
        Entry9_Legumes = Entry(Frame_Legumes,justify="center",textvariable=self.G9)
        Entry9_Legumes.place(x=40,y=54+260,width=100)

        Text10_Legumes = Label(Frame_Legumes,text=" : سكر",bg="#004D64",fg="#ffffff",font=("tajawal",12))
        Text10_Legumes.place(x=220,y=50+290)
        Entry10_Legumes = Entry(Frame_Legumes,justify="center",textvariable=self.G10)
        Entry10_Legumes.place(x=40,y=54+290,width=100)

        Text11_Legumes = Label(Frame_Legumes,text=" : فلفل اسود",bg="#004D64",fg="#ffffff",font=("tajawal",12))
        Text11_Legumes.place(x=176,y=50+340)
        Entry11_Legumes = Entry(Frame_Legumes,justify="center",textvariable=self.G11)
        Entry11_Legumes.place(x=40,y=54+340,width=100)

        Text12_Legumes = Label(Frame_Legumes,text=" : فلفل احمر",bg="#004D64",fg="#ffffff",font=("tajawal",12))
        Text12_Legumes.place(x=180,y=50+370)
        Entry12_Legumes = Entry(Frame_Legumes,justify="center",textvariable=self.G12)
        Entry12_Legumes.place(x=40,y=54+370,width=100)

        Text13_Legumes = Label(Frame_Legumes,text=" : اللوبيا",bg="#004D64",fg="#ffffff",font=("tajawal",12))
        Text13_Legumes.place(x=210,y=50+400)
        Entry13_Legumes = Entry(Frame_Legumes,justify="center",textvariable=self.G13)
        Entry13_Legumes.place(x=40,y=54+400,width=100)

        Text14_Legumes = Label(Frame_Legumes,text=" : الادمامي",bg="#004D64",fg="#ffffff",font=("tajawal",12))
        Text14_Legumes.place(x=190,y=50+460)
        Entry14_Legumes = Entry(Frame_Legumes,justify="center",textvariable=self.G14)
        Entry14_Legumes.place(x=40,y=54+460,width=100)

        Text15_Legumes = Label(Frame_Legumes,text=" : القمح",bg="#004D64",fg="#ffffff",font=("tajawal",12))
        Text15_Legumes.place(x=205,y=50+490)
        Entry15_Legumes = Entry(Frame_Legumes,justify="center",textvariable=self.G15)
        Entry15_Legumes.place(x=40,y=54+490,width=100)

        Text16_Legumes = Label(Frame_Legumes,text=" : الشعير",bg="#004D64",fg="#ffffff",font=("tajawal",12))
        Text16_Legumes.place(x=195,y=50+520)
        Entry16_Legumes = Entry(Frame_Legumes,justify="center",textvariable=self.G16)
        Entry16_Legumes.place(x=40,y=54+520,width=100)

        Text17_Legumes = Label(Frame_Legumes,text=" : الشوفان",bg="#004D64",fg="#ffffff",font=("tajawal",12))
        Text17_Legumes.place(x=182,y=50+570)
        Entry17_Legumes = Entry(Frame_Legumes,justify="center",textvariable=self.G17)
        Entry17_Legumes.place(x=40,y=54+570,width=100)

        # _________ Supplies ________

        Frame_Supplies = Frame(self.root,bg="#004D64")
        Frame_Supplies.place(x=312,y=29,height=670,width=300)

        Title_Supplies = Label(Frame_Supplies,text="اللوازم المنزلي",bg="#004D64",fg="#C7D503",font=("tajawal",15,"bold"))
        Title_Supplies.pack()

        Text1_Supplies = Label(Frame_Supplies,text=" : مصفاة",bg="#004D64",fg="#ffffff",font=("tajawal",12))
        Text1_Supplies.place(x=212,y=50)
        Entry1_Supplies = Entry(Frame_Supplies,justify="center",textvariable=self.S1)
        Entry1_Supplies.place(x=40,y=54,width=100)

        Text2_Supplies = Label(Frame_Supplies,text=" : صحن",bg="#004D64",fg="#ffffff",font=("tajawal",12))
        Text2_Supplies.place(x=196+26,y=50+30)
        Entry2_Supplies = Entry(Frame_Supplies,justify="center",textvariable=self.S2)
        Entry2_Supplies.place(x=40,y=54+30,width=100)

        Text3_Supplies = Label(Frame_Supplies,text=" : كآس",bg="#004D64",fg="#ffffff",font=("tajawal",12))
        Text3_Supplies.place(x=196+26,y=50+60)
        Entry3_Supplies = Entry(Frame_Supplies,justify="center",textvariable=self.S3)
        Entry3_Supplies.place(x=40,y=54+60,width=100)

        Text4_Supplies = Label(Frame_Supplies,text=" : ابريق",bg="#004D64",fg="#ffffff",font=("tajawal",12))
        Text4_Supplies.place(x=222,y=50+90)
        Entry4_Supplies = Entry(Frame_Supplies,justify="center",textvariable=self.S4)
        Entry4_Supplies.place(x=40,y=54+90,width=100)

        Text5_Supplies = Label(Frame_Supplies,text=" : سكين",bg="#004D64",fg="#ffffff",font=("tajawal",12))
        Text5_Supplies.place(x=212,y=50+120)
        Entry5_Supplies = Entry(Frame_Supplies,justify="center",textvariable=self.S5)
        Entry5_Supplies.place(x=40,y=54+120,width=100)

        Text6_Supplies = Label(Frame_Supplies,text=" : شوك",bg="#004D64",fg="#ffffff",font=("tajawal",12))
        Text6_Supplies.place(x=215,y=50+150)
        Entry6_Supplies = Entry(Frame_Supplies,justify="center",textvariable=self.S6)
        Entry6_Supplies.place(x=40,y=54+150,width=100)

        Text7_Supplies = Label(Frame_Supplies,text=" : طنجرة",bg="#004D64",fg="#ffffff",font=("tajawal",12))
        Text7_Supplies.place(x=210,y=50+180)
        Entry7_Supplies = Entry(Frame_Supplies,justify="center",textvariable=self.S7)
        Entry7_Supplies.place(x=40,y=54+180,width=100)


        Text8_Supplies = Label(Frame_Supplies,text=" : سلة",bg="#004D64",fg="#ffffff",font=("tajawal",12))
        Text8_Supplies.place(x=225,y=50+230)
        Entry8_Supplies = Entry(Frame_Supplies,justify="center",textvariable=self.S8)
        Entry8_Supplies.place(x=40,y=54+230,width=100)

        Text9_Supplies = Label(Frame_Supplies,text=" : ملاعق",bg="#004D64",fg="#ffffff",font=("tajawal",12))
        Text9_Supplies.place(x=212,y=50+260)
        Entry9_Supplies = Entry(Frame_Supplies,justify="center",textvariable=self.S9)
        Entry9_Supplies.place(x=40,y=54+260,width=100)

        Text10_Supplies = Label(Frame_Supplies,text=" : صينية",bg="#004D64",fg="#ffffff",font=("tajawal",12))
        Text10_Supplies.place(x=214,y=50+290)
        Entry10_Supplies = Entry(Frame_Supplies,justify="center",textvariable=self.S10)
        Entry10_Supplies.place(x=40,y=54+290,width=100)

        Text11_Supplies = Label(Frame_Supplies,text=" : وعاء الخلط",bg="#004D64",fg="#ffffff",font=("tajawal",12))
        Text11_Supplies.place(x=176,y=50+340)
        Entry11_Supplies = Entry(Frame_Supplies,justify="center",textvariable=self.S11)
        Entry11_Supplies.place(x=40,y=54+340,width=100)

        Text12_Supplies = Label(Frame_Supplies,text=" : فتاحة العلب",bg="#004D64",fg="#ffffff",font=("tajawal",12))
        Text12_Supplies.place(x=170,y=50+370)
        Entry12_Supplies = Entry(Frame_Supplies,justify="center",textvariable=self.S12)
        Entry12_Supplies.place(x=40,y=54+370,width=100)

        Text13_Supplies = Label(Frame_Supplies,text=" : مقشرة",bg="#004D64",fg="#ffffff",font=("tajawal",12))
        Text13_Supplies.place(x=200,y=50+400)
        Entry13_Supplies = Entry(Frame_Supplies,justify="center",textvariable=self.S13)
        Entry13_Supplies.place(x=40,y=54+400,width=100)

        Text14_Supplies = Label(Frame_Supplies,text=" : لوح التقطيع",bg="#004D64",fg="#ffffff",font=("tajawal",12))
        Text14_Supplies.place(x=170,y=50+460)
        Entry14_Supplies = Entry(Frame_Supplies,justify="center",textvariable=self.S14)
        Entry14_Supplies.place(x=40,y=54+460,width=100)

        Text15_Supplies = Label(Frame_Supplies,text=" : حفارة",bg="#004D64",fg="#ffffff",font=("tajawal",12))
        Text15_Supplies.place(x=212,y=50+490)
        Entry15_Supplies = Entry(Frame_Supplies,justify="center",textvariable=self.S15)
        Entry15_Supplies.place(x=40,y=54+490,width=100)

        Text16_Supplies = Label(Frame_Supplies,text=" : سلة قمامة",bg="#004D64",fg="#ffffff",font=("tajawal",12))
        Text16_Supplies.place(x=175,y=50+520)
        Entry16_Supplies = Entry(Frame_Supplies,justify="center",textvariable=self.S16)
        Entry16_Supplies.place(x=40,y=54+520,width=100)


        Text17_Supplies = Label(Frame_Supplies,text=" : اكياس",bg="#004D64",fg="#ffffff",font=("tajawal",12))
        Text17_Supplies.place(x=200,y=50+570)
        Entry17_Supplies = Entry(Frame_Supplies,justify="center",textvariable=self.S17)
        Entry17_Supplies.place(x=40,y=54+570,width=100)

        # _________ Electric ________

        Frame_Electric = Frame(self.root,bg="#004D64")
        Frame_Electric.place(x=620,y=29,height=510,width=333)

        Title_Electric = Label(Frame_Electric,text="ادوات كهربائية",bg="#004D64",fg="#C7D503",font=("tajawal",15,"bold"))
        Title_Electric.pack()

        Text1_Electric = Label(Frame_Electric,text=" : مكنسة",bg="#004D64",fg="#ffffff",font=("tajawal",12))
        Text1_Electric.place(x=212+10,y=50)
        Entry1_Electric = Entry(Frame_Electric,justify="center",textvariable=self.E1)
        Entry1_Electric.place(x=40+10,y=54,width=100)

        Text2_Electric = Label(Frame_Electric,text=" : تلفزيون",bg="#004D64",fg="#ffffff",font=("tajawal",12))
        Text2_Electric.place(x=196+26,y=50+30)
        Entry2_Electric = Entry(Frame_Electric,justify="center",textvariable=self.E2)
        Entry2_Electric.place(x=50,y=54+30,width=100)

        Text3_Electric = Label(Frame_Electric,text=" : غسالة",bg="#004D64",fg="#ffffff",font=("tajawal",12))
        Text3_Electric.place(x=196+30,y=50+60)
        Entry3_Electric = Entry(Frame_Electric,justify="center",textvariable=self.E3)
        Entry3_Electric.place(x=50,y=54+60,width=100)

        Text4_Electric = Label(Frame_Electric,text=" : مكرويڤ",bg="#004D64",fg="#ffffff",font=("tajawal",12))
        Text4_Electric.place(x=220,y=50+90)
        Entry4_Electric = Entry(Frame_Electric,justify="center",textvariable=self.E4)
        Entry4_Electric.place(x=50,y=54+90,width=100)

        Text5_Electric = Label(Frame_Electric,text=" : خلاط",bg="#004D64",fg="#ffffff",font=("tajawal",12))
        Text5_Electric.place(x=237,y=50+120)
        Entry5_Electric = Entry(Frame_Electric,justify="center",textvariable=self.E5)
        Entry5_Electric.place(x=50,y=54+120,width=100)

        Text6_Electric = Label(Frame_Electric,text=" : فرن غاز",bg="#004D64",fg="#ffffff",font=("tajawal",12))
        Text6_Electric.place(x=225,y=50+150)
        Entry6_Electric = Entry(Frame_Electric,justify="center",textvariable=self.E6)
        Entry6_Electric.place(x=50,y=54+150,width=100)

        Text7_Electric = Label(Frame_Electric,text=" : مقلاة كهرباء",bg="#004D64",fg="#ffffff",font=("tajawal",12))
        Text7_Electric.place(x=190,y=50+180)
        Entry7_Electric = Entry(Frame_Electric,justify="center",textvariable=self.E7)
        Entry7_Electric.place(x=50,y=54+180,width=100)


        Text8_Electric = Label(Frame_Electric,text=" : مروحة",bg="#004D64",fg="#ffffff",font=("tajawal",12))
        Text8_Electric.place(x=235,y=50+230)
        Entry8_Electric = Entry(Frame_Electric,justify="center",textvariable=self.E8)
        Entry8_Electric.place(x=50,y=54+230,width=100)

        Text9_Electric = Label(Frame_Electric,text=" : هاتف",bg="#004D64",fg="#ffffff",font=("tajawal",12))
        Text9_Electric.place(x=242,y=50+260)
        Entry9_Electric = Entry(Frame_Electric,justify="center",textvariable=self.E9)
        Entry9_Electric.place(x=50,y=54+260,width=100)

        Text10_Electric = Label(Frame_Electric,text=" : تلفيزيون",bg="#004D64",fg="#ffffff",font=("tajawal",12))
        Text10_Electric.place(x=224,y=50+290)
        Entry10_Electric = Entry(Frame_Electric,justify="center",textvariable=self.E10)
        Entry10_Electric.place(x=50,y=54+290,width=100)
        

        Text11_Electric = Label(Frame_Electric,text=" : مكواة",bg="#004D64",fg="#ffffff",font=("tajawal",12))
        Text11_Electric.place(x=240,y=50+340)
        Entry11_Electric = Entry(Frame_Electric,justify="center",textvariable=self.E11)
        Entry11_Electric.place(x=50,y=54+340,width=100)

        Text12_Electric = Label(Frame_Electric,text=" : مبراد",bg="#004D64",fg="#ffffff",font=("tajawal",12))
        Text12_Electric.place(x=247,y=50+370)
        Entry12_Electric = Entry(Frame_Electric,justify="center",textvariable=self.E12)
        Entry12_Electric.place(x=50,y=54+370,width=100)

        Text13_Electric = Label(Frame_Electric,text=" : فلتر الماء",bg="#004D64",fg="#ffffff",font=("tajawal",12))
        Text13_Electric.place(x=218,y=50+400)
        Entry13_Electric = Entry(Frame_Electric,justify="center",textvariable=self.E13)
        Entry13_Electric.place(x=50,y=54+400,width=100)


        self.root.mainloop()

        # _______ Method _______

    def welcome(self) :
        self.BoxText.delete('1.0',END)
        self.BoxText.insert(END , "====================================")
        self.BoxText.insert(END , f"\n Name :{self.NameSubscriber.get()}")
        self.BoxText.insert(END , f"\n Phone :{self.NumberSubscriber.get()}")
        self.BoxText.insert(END , f"\n num_bill :{self.NumberInvoice.get()}")
        self.BoxText.insert(END , "\n====================================")
        self.BoxText.insert(END , "\n Fatore : ")
        self.BoxText.insert(END , f"\n Peice : {self.TOTLE} $")

    def Price(self) :
        Legumes = float(self.S1.get() 
                        + self.G2.get()*2.5 
                        + self.G3.get()*1
                        + self.G4.get()*2
                        + self.G5.get()*1.5
                        + self.G6.get()*1
                        + self.G7.get()*1
                        + self.G8.get()*2.5
                        + self.G9.get()*1.5
                        + self.G10.get()*1.5
                        + self.G11.get()*2.5
                        + self.G12.get()*1.5
                        + self.G13.get()*1
                        + self.G14.get()*1
                        + self.G15.get()*1.5
                        + self.G16.get()*1.5
                        + self.G17.get()*2.5 )
        self.AccountLegumes.set(str(Legumes)+" $")

        Supplies = float(self.S1.get() 
                        + self.S2.get()*2.5 
                        + self.S3.get()*1
                        + self.S4.get()*2
                        + self.S5.get()*1.5
                        + self.S6.get()*1
                        + self.S7.get()*1
                        + self.S8.get()*2.5
                        + self.S9.get()*1.5
                        + self.S10.get()*1.5
                        + self.S11.get()*2.5
                        + self.S12.get()*2
                        + self.S13.get()*1.5
                        + self.S14.get()*1
                        + self.S15.get()*1.5
                        + self.S16.get()*1.5
                        + self.S17.get()*2.5 )
        self.AccountSupplies.set(str(Supplies)+" $")

        Electric = float(self.E1.get() 
                        + self.E2.get()*2.5 
                        + self.E3.get()*1
                        + self.E4.get()*2
                        + self.E5.get()*1.5
                        + self.E6.get()*1
                        + self.E7.get()*1
                        + self.E8.get()*2.5
                        + self.E9.get()*1.5
                        + self.E10.get()*1.5
                        + self.E11.get()*2.5
                        + self.E12.get()*2
                        + self.E13.get()*1.5 )
        self.AccountElectric.set(str(Electric)+" $")

        self.TOTLE = Legumes + Supplies + Electric

    def delate(self) :
        self.AccountLegumes.set("")
        self.AccountSupplies.set("")
        self.AccountElectric.set("")





ob = super()

        
        