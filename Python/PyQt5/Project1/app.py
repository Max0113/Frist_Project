from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QFrame , QLabel , QLineEdit , QPushButton , QCheckBox
import PyQt5.QtWidgets as QW
import sys

print(sys.argv)

app = QtWidgets.QApplication(sys.argv)

win = QtWidgets.QWidget()
win = QtWidgets.QMainWindow()
win.resize(500, 500)
win.move(200, 200)
win.setWindowTitle("APP-YounesAmzil")
win.setStyleSheet("background-color:#ffffff")

# Icon (تأكد أن الملف .ico)
win.setWindowIcon(QtGui.QIcon("C:\\Users\\Gk\\Desktop\\younes\\Codhub\\My_Frist_Project\\PyQt5\\Project1\\imge\\favpng_22eeecf99b8d92726b4f3735be5473c0.png"))

# ____ Main _____

menubre = win.menuBar()

l1 = menubre.addMenu("File")
e1 = QtWidgets.QAction("New File")
e2 = QtWidgets.QAction("New Folder")
e3 = QtWidgets.QAction("Save As")
e4 = QtWidgets.QAction("Exit")
l1.addAction(e1)
l1.addAction(e2)
l1.addAction(e3)
l1.addAction(e4)
e1.setShortcut('Ctrl + N')
e2.setShortcut('Ctrl + F')
e3.setShortcut('Ctrl + S')
e4.setShortcut('Ctrl + E')
def ex () :
    win.destroy()
    quit()
e4.triggered.connect(ex)


l2 = menubre.addMenu("Edit")
l3 = menubre.addMenu("Selection")
l4 = menubre.addMenu("View")
l5 = menubre.addMenu("Help")

# ____ Method ____

def Error() :
    Q1 = QW.QMessageBox.warning(win,"hello","error of inscription !!")

# إنشاء QFrame
frame = QFrame(win)
frame.setGeometry(100, 90, 300, 320)  # position x, y, width, height

# تحديد style
frame.setFrameShape(QFrame.Box)        # شكل الإطار (Box, Panel, HLine, VLine…)
frame.setFrameShadow(QFrame.Raised)    # الظل (Raised, Sunken, Plain)
frame.setLineWidth(0)                            # سماكة الخط
frame.setStyleSheet("""
background-color: #000000;
color: #ffffff;
font-family : tajawal;
border-radius: 10px; 
""")

# إضافة عنصر داخل الـ frame (مثلا label)
label1 = QLabel("Email : ", frame)
label1.move(20, 20+60)
Entr1 = QLineEdit(frame)
Entr1.move(20, 50+60)
Entr1.resize(200,30)
Entr1.setStyleSheet("""
   background-color: #ffffff;
   border-radius: 5px;
   color : black;
                    """)

label2 = QLabel("Passowrd : ", frame)
label2.move(20, 90+60)
Entr2 = QLineEdit(frame)
Entr2.move(20, 120+60)
Entr2.resize(200,30)
Entr2.setStyleSheet("""
   background-color: #ffffff;
   border-radius: 5px;
   color : black;
""")

check1 = QCheckBox("accept",frame)
check1.move(20,170+60)

button1 = QPushButton("Login",frame)
button1.move(20,200+60)
button1.resize(100,30)
button1.setStyleSheet("""
   background-color: #ffffff;
   color: black;
   border-radius: 5px; 
""")
button1.clicked.connect(Error)

button2 = QPushButton("Inscription",frame)
button2.move(140,200+60)
button2.resize(100,30)
button2.setStyleSheet("""
   background-color: #ffffff;
   color: black;
   border-radius: 5px; 
""")

# Image 
Lable = QLabel(frame)
photo = QPixmap("C:\\Users\\Gk\\Desktop\\\\younes\\Codhub\\My_Frist_Project\\PyQt5\\Project1\\imge\\user.png")
Lable.setPixmap(photo)
Lable.move(120,20)
Lable.setStyleSheet("")

win.show()
app.exec_()   # إذا كنت PyQt5
# app.exec()  # إذا كنت PyQt6


