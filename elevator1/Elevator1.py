
import sys
import time
from PyQt5.QtCore import Qt 
from PyQt5.QtGui import QFont, QIcon  
from PyQt5.QtWidgets import QApplication, QCheckBox, QGridLayout,QRadioButton, QLabel,QPushButton, QSlider, QVBoxLayout, QWidget
from functools import partial

class  Elevator:
    def __init__(self):
        self.a=QApplication(sys.argv)
        self.w=QWidget()
        self.a.setStyleSheet("background-color: red;")
        self.hbox=QVBoxLayout()
        self.w.setFixedSize(500,500)
        self.w.setWindowTitle('   ...Elevator...')
        self.w.setLayout(self.hbox)
        self.n=0
        
        self.sliders()
        self.buttonf()
        self.button.stateChanged.connect(partial(self.elevator_move,self.button,0,1))
        self.button1.stateChanged.connect(partial(self.elevator_move,self.button1,2,1))
        self.button2.stateChanged.connect(partial(self.elevator_move,self.button2,4,1))
        self.button3.stateChanged.connect(partial(self.elevator_move,self.button3,6,1))
        self.button4.stateChanged.connect(partial(self.elevator_move,self.button4,8,1))
        self.button5.stateChanged.connect(partial(self.elevator_move,self.button5,10,1))
    def buttonf(self):
        self.font=QFont('arary',13)
        self.button=QCheckBox('0')
        self.button.setFont(self.font)
        self.hbox.addWidget(self.button)
        self.button1=QCheckBox('1')
        self.button1.setFont(self.font)
        self.hbox.addWidget(self.button1)
        self.button2=QCheckBox('2')
        self.button2.setFont(self.font)
        self.hbox.addWidget(self.button2)
        self.button3=QCheckBox('3')
        self.button3.setFont(self.font)
        self.hbox.addWidget(self.button3)
        self.button4=QCheckBox('4')
        self.button4.setFont(self.font)
        self.hbox.addWidget(self.button4)
        self.button5=QCheckBox('5')
        self.button5.setFont(self.font)
        self.hbox.addWidget(self.button5)
    def sliders(self):
        self.slider=QSlider()
        self.slider.setOrientation(Qt.Orientation.Vertical)
        self.slider.setMinimum(0)
        self.slider.setMaximum(10)
        self.slider.setTickPosition(QSlider.TickPosition.TicksBothSides)
        self.slider.setTickInterval(2)
        self.hbox.addWidget(self.slider)
    def elevator_move(self,b,n,nn):
        self.b=b
        self.slider.setValue(n)




        
        


if __name__ == '__main__':
    e=Elevator()
    e.w.show()
    sys.exit(e.a.exec())