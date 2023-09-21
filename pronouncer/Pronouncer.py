import sys
import pyttsx3 as pu
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QLineEdit, QPushButton, QHBoxLayout, QApplication
from functools import partial
class Main :
    def __init__(self):
        self.a=QApplication(sys.argv)
        self.w=QWidget()
        self.w.setWindowTitle('Pronouncer')
        self.w.setFixedSize(500,250)
        self.line_edit()
        self.button()
        self.e=pu.init()
        self.e.setProperty('rate',110)

        self.bt.clicked.connect(self.readd)
    def line_edit(self):
        self.font=QFont('Century',35)
        self.le=QLineEdit(self.w)
        print(self.le.text())
        self.le.setPlaceholderText('Enterword:')
        self.le.setFont(self.font)
        self.le.move(5,10)
    def button(self):
        self.font2=QFont('Century',60)
        self.bt=QPushButton('Start',self.w)
        self.bt.setFont(self.font2)
        self.bt.move(150,130)
    def readd(self):
        x=self.le.text()
        self.e.say(x)
        self.e.runAndWait()




if __name__ == '__main__':
    m=Main()
    m.w.show()
    sys.exit(m.a.exec_())



