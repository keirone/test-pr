
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QVBoxLayout,
                            QMessageBox, QPlainTextEdit, QHBoxLayout,
                            QLineEdit, QComboBox)
from PyQt5.QtGui import QIcon
from PyQt5 import QtCore

class View(QWidget) :
    # 화면 정의 및 처리, 초기화를 담당하는 파일
    def __init__(self) :
        super().__init__()
        self.initUI()
    
    def initUI(self) :
        self.btn1 = QPushButton("Calc", self)
        self.btn2 = QPushButton("Reset", self)
        
        self.te1 = QPlainTextEdit()
        self.te1.setReadOnly(True)

        self.le1 = QLineEdit("0",self)
        self.le1.setAlignment(QtCore.Qt.AlignRight) # 문자열 배치 설정
        self.le1.setFocus(True) # 포커스 설정
        self.le1.selectAll()    # 텍스트 전체 선택

        self.le2 = QLineEdit("0",self)
        self.le2.setAlignment(QtCore.Qt.AlignRight)

        self.cb = QComboBox(self)
        self.cb.addItems(["+","-","*","/"]) # 콤보박스의 연산자

        hbox = QHBoxLayout()    # 수평 박스 레이아웃 추가
        hbox.addStretch(1)      # 공백을 추가한다
        hbox.addWidget(self.btn1)
        hbox.addWidget(self.btn2)

        hbox_formular = QHBoxLayout()
        hbox_formular.addWidget(self.le1)
        hbox_formular.addWidget(self.cb)
        hbox_formular.addWidget(self.le2)

        vbox = QVBoxLayout()
        vbox.addWidget(self.te1)
        vbox.addLayout(hbox_formular)
        vbox.addLayout(hbox)    # btn1 대신 hbox를 위치시킴
        vbox.addStretch(1)
        
        self.setLayout(vbox)

        self.setWindowTitle("Calculator")
        self.setWindowIcon(QIcon("Icon.png"))
        self.resize(256,256)
        self.show()
        
    def setDisplay(self,text) :     # Handler 함수
        #QMessageBox.information(self,"information","Button Clicked")
        self.te1.appendPlainText(text)
    def clearMessage(self) :
        self.te1.clear()