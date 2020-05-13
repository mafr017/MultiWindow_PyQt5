import sys
import time
from PyQt5.QtGui     import *
from PyQt5.QtCore    import *
from PyQt5.QtWidgets import *
from PyQt5.uic import *
from PyQt5 import *

import gui.test1 as tst1
import gui.test2 as tst2
import gui.test3 as tst3

class formMain(QMainWindow):

    def __init__(self):
        global nilai2
        QMainWindow.__init__(self)
        self.tst1s = tst1.Ui_MainWindow()
        self.tst1s.setupUi(self)

        #inisialisasi widgets
        self.valluee = 2323
        nilai2 = self.valluee
        self.tst1s.label_2.setText(str(nilai2))
        self.tst1s.pushButton.clicked.connect(self.pencet)
        self.show()
    
    #fungsi pencet untuk widget pushButton
    def pencet(self):
        global nilai
        nilai = int(self.tst1s.lineEdit.displayText())
        self.bukaform = formMain2(nilai, nilai2) #panggil class formMain2
        self.close()
    
class formMain2(QMainWindow):

    def __init__(self, aaa, bbb):
        QMainWindow.__init__(self)
        self.tst2s = tst2.Ui_MainWindow()
        self.tst2s.setupUi(self)
        self.tst2s.label_2.setText(str(f"{nilai} {nilai2}"))

        self.tst2s.pushButton.clicked.connect(self.pencet1)
        self.tst2s.pushButton_2.clicked.connect(self.pencet3)
        self.show()
    
    def pencet1(self):
        self.bukaform = formMain()
        self.close()
    
    def pencet3(self):
        self.bukaform = formMain3(nilai2)
        self.close()

class formMain3(QDialog):

    def __init__(self, ccc):
        QMainWindow.__init__(self)
        self.tst3s = tst3.Ui_Dialog()
        self.tst3s.setupUi(self)
        self.tst3s.label_2.setText(str(f"{nilai2}"))

        self.tst3s.pushButton.clicked.connect(self.pencet)
        self.show()
    
    def pencet(self):
        self.bukaform = formMain2(nilai, nilai2)
        self.close()

if __name__=="__main__":
    app = QApplication(sys.argv)
    w = formMain()
    sys.exit(app.exec_())