
import sys
import time
from PyQt6.QtGui import QIcon ,   QFont
from PyQt6.QtWidgets import QLabel, QWidget, QPushButton, QApplication, QSlider, QVBoxLayout, QGridLayout
from PyQt6.QtCore import Qt
from functools import partial
class  Elevator:
    def __init__(self):
        self.a=QApplication(sys.argv)
        self.w=QWidget()
        self.hbox=QVBoxLayout()
        self.w.setFixedSize(500,500)
        self.w.setWindowTitle('   ...Elevator...')
        self.w.setLayout(self.hbox)
        self.sliders()
        self.button()
        self.button.clicked.connect(partial(self.elevator_move,self.button,0))
        self.button1.clicked.connect(partial(self.elevator_move,self.button1,2))
        self.button2.clicked.connect(partial(self.elevator_move,self.button2,4))
        self.button3.clicked.connect(partial(self.elevator_move,self.button3,6))
        self.button4.clicked.connect(partial(self.elevator_move,self.button4,8))
        self.button5.clicked.connect(partial(self.elevator_move,self.button5,10))
    def button(self):
        self.font=QFont('arary',13)
        self.button=QPushButton('...  p   ...',self.w)
        self.button.setFont(self.font)
        self.button.move(400,300)
        self.button1=QPushButton('...   1   ...',self.w)
        self.button1.setFont(self.font)
        self.button1.move(400,250)
        self.button2=QPushButton('...   2   ...',self.w)
        self.button2.setFont(self.font)
        self.button2.move(400,200)
        self.button3=QPushButton('...   3   ...',self.w)
        self.button3.setFont(self.font)
        self.button3.move(400,150)
        self.button4=QPushButton('...   4   ...',self.w)
        self.button4.setFont(self.font)
        self.button4.move(400,100)
        self.button5=QPushButton('...    5   ...',self.w)
        self.button5.setFont(self.font)
        self.button5.move(400,50)
    def sliders(self):
        self.slider=QSlider()
        self.slider.setOrientation(Qt.Orientation.Vertical)
        self.slider.setMinimum(0)
        self.slider.setMaximum(10)
        self.slider.setTickPosition(QSlider.TickPosition.TicksBothSides)
        self.slider.setTickInterval(2)
        self.hbox.addWidget(self.slider)
    def elevator_move(self,b,n):
        self.b=b
        self.slider.setValue(n)

if __name__ == '__main__':
    e=Elevator()
    e.w.show()
    sys.exit(e.a.exec())











# import sys
# import time

# from PyQt5.QtCore import Qt 
# from PyQt5.QtGui import QFont, QIcon  
# from PyQt5.QtWidgets import QApplication, QCheckBox, QGridLayout,QRadioButton, QLabel,QPushButton, QSlider, QVBoxLayout, QWidget


# class  Elevator:
#     def __init__(self):
#         self.a=QApplication(sys.argv)
#         self.w=QWidget()
#         self.a.setStyleSheet("background-color: red;")
#         self.hbox=QVBoxLayout()
#         self.w.setFixedSize(500,500)
#         self.w.setWindowTitle('   ...Elevator...')
#         self.w.setLayout(self.hbox)

        
#         self.sliders()
#         self.buttonf()
#         self.button.stateChanged.connect(self.elevator_move)
#         self.button1.stateChanged.connect(self.elevator_move_1)
#         self.button2.stateChanged.connect(self.elevator_move_2)
#         self.button3.stateChanged.connect(self.elevator_move_3)
#         self.button4.stateChanged.connect(self.elevator_move_4)
#         self.button5.stateChanged.connect(self.elevator_move_5)
#     def buttonf(self):
#         self.font=QFont('arary',13)
#         self.button=QCheckBox('0')
#         self.button.setFont(self.font)
#         self.hbox.addWidget(self.button)
#         self.button1=QCheckBox('1')
#         self.button1.setFont(self.font)
#         self.hbox.addWidget(self.button1)
#         self.button2=QCheckBox('2')
#         self.button2.setFont(self.font)
#         self.hbox.addWidget(self.button2)
#         self.button3=QCheckBox('3')
#         self.button3.setFont(self.font)
#         self.hbox.addWidget(self.button3)
#         self.button4=QCheckBox('4')
#         self.button4.setFont(self.font)
#         self.hbox.addWidget(self.button4)
#         self.button5=QCheckBox('5')
#         self.button5.setFont(self.font)
#         self.hbox.addWidget(self.button5)
#     def sliders(self):
#         self.slider=QSlider()
#         self.slider.setOrientation(Qt.Orientation.Vertical)
#         self.slider.setMinimum(0)
#         self.slider.setMaximum(10)
#         self.slider.setTickPosition(QSlider.TickPosition.TicksBothSides)
#         self.slider.setTickInterval(2)
#         self.hbox.addWidget(self.slider)
#     def elevator_move(self):
#         print(self.button.text())
#         self.slider.setValue(0)
#     def elevator_move_1(self):
#         print(self.button1.text())
#         self.slider.setValue(2)
#     def elevator_move_2(self):
#         print(self.button2.text())
#         self.slider.setValue(4)
#     def elevator_move_3(self):
#         print(self.button3.text())
#         self.slider.setValue(6)
#     def elevator_move_4(self):
#         print(self.button4.text())
#         self.slider.setValue(8)
#         time.sleep(0.01)
#     def elevator_move_5(self):
#         print(self.button5.text())
#         self.slider.setValue(10)

# if __name__ == '__main__':
#     e=Elevator()
#     e.w.show()
#     sys.exit(e.a.exec())