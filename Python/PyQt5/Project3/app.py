from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUiType
from os import path
import sys


From_Class, _ = loadUiType(path.join(path.dirname(__file__), "untitled.ui"))


class mainloop(QWidget, From_Class):
    def __init__(self, parent=None):
        super(mainloop, self).__init__(parent)
        self.setupUi(self) 

def main():
    app = QApplication(sys.argv)
    app.setAttribute(Qt.AA_EnableHighDpiScaling)  
    app.setStyle("Fusion")                         
    w = mainloop()  
    w.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

