from PyQt5 import QtWidgets , QtGui , QtCore
from PyQt5.QtWidgets import *
import sys

app = QApplication(sys.argv)

win = QWidget()
win.setWindowTitle("app younes")
win.resize(600,500)
win.move(100,100)
win.setWindowIcon(QtGui.QIcon("C:\\Users\\Gk\\Desktop\\younes\\Codhub\\My_Frist_Project\\PyQt5\\Project1\\imge\\favpng_22eeecf99b8d92726b4f3735be5473c0.png"))

tab = QTabWidget(win)
tab.resize(600,500)
# ____ Tab un ____
t1 = QWidget()
t1.resize(600,500)
tab.addTab(t1,"Tab 1")
Text = QLabel("""
« Texte » est issu du mot latin « textum », dérivé du verbe « texere » 
qui signifie « tisser ». Le mot s'applique à l'entrelacement des fibres utilisées 
dans le tissage, voir par exemple Ovide : « Quo super iniecit textum rude sedula Baucis
= (un siège) sur lequel Baucis empressée avait jeté un tissu grossier »[2] ou au tressage 
(exemple chez Martial « Vimineum textum = panier d'osier tressé »). Le verbe a aussi le 
sens large de construire comme dans « basilicam texere = construire une basilique » 
chez Cicéron[3].

Le sens figuré d'éléments de langage organisés et enchaînés apparaît avant l'Empire 
romain : il désigne un agencement particulier du discours. Exemple : « epistolas 
texere = composer des épîtres » - Cicéron (Ier siècle av. J.-C.)[4] ou plus nettement 
chez Quintilien (Ier siècle apr. J.-C.) : « verba in textu jungantur = l'agencement des 
mots dans la phrase »[5].

Les formes anciennes du Moyen Âge désignent au XIIe siècle le volume qui contient le 
texte sacré des Évangiles, puis au XIIIe siècle, le texte original d'un livre saint 
ou des propos de quelqu'un. Au XVIIe siècle le mot s’applique au passage d'un ouvrage 
pris comme référence et au début du XIXe siècle le mot texte a son sens général d'« écrit »
[6]
""" , t1)

Text.setStyleSheet("""

""")

# ____ Tab deux ____
t2 = QWidget()
t2.resize(500,500)
tab.addTab(t2,"Tab 2")

text_edit = QTextEdit(t2)
text_edit.setPlaceholderText("Écris ton texte ici...")
text_edit.resize(600,500)


# ____ Tab Trew ____
t3 = QWidget()
t3.resize(500,500)
tab.addTab(t3,"Tab 3")





win.show()
app.exec_()