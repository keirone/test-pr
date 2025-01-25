import sys
from PyQt5.QtWidgets import (QApplication,QWidget, QPushButton, QVBoxLayout,QMessageBox, QPlainTextEdit, QHBoxLayout)
from PyQt5.QtGui import QIcon

class Calculator(QWidget) :
    def __init__(self) :
        super().__init__()
        self.initUI()
    
    def initUI(self) :
        self.btn1 = QPushButton("Message", self)
        self.btn1.clicked.connect(self.activateMessage)
        
        self.btn2 = QPushButton("Reset", self)
        self.btn2.clicked.connect(self.clearMessage)
        
        self.te1 = QPlainTextEdit()
        self.te1.setReadOnly(True)

        hbox = QHBoxLayout()    # 수평 박스 레이아웃 추가
        hbox.addStretch(1)      # 공백을 추가한다
        hbox.addWidget(self.btn1)
        hbox.addWidget(self.btn2)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addWidget(self.te1)
        vbox.addLayout(hbox)    # btn1 대신 hbox를 위치시킴
        vbox.addStretch(1)
        
        self.setLayout(vbox)

        self.setWindowTitle("Calculator")
        self.setWindowIcon(QIcon("Icon.png"))
        self.resize(256,256)
        self.show()

    def activateMessage(self) :     # Handler 함수
        #QMessageBox.information(self,"information","Button Clicked")
        self.te1.appendPlainText("button Clicked")
    def clearMessage(self) :
        self.te1.clear()

        
if __name__ == "__main__" :
    app = QApplication(sys.argv)
    view = Calculator()
    sys.exit(app.exec_())