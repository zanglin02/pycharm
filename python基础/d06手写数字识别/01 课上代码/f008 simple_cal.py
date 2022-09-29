import sys
from PyQt5.QtWidgets import *

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('我的计算器')
        self.initUI()

    def initUI(self):
        self.resize(600, 400)
        self.num1Edit = QLineEdit(self)
        self.num2Edit = QLineEdit(self)
        self.op = QComboBox(self)
        self.op.addItems(['+', '-', '*', '/'])
        self.calBtn = QPushButton(self)
        self.calBtn.setText('=')
        self.resultbl = QLabel(self)
        self.resultbl.setText('500000')

        hbox = QHBoxLayout()

        hbox.addWidget(self.num1Edit)
        hbox.addWidget(self.op)
        hbox.addWidget(self.num2Edit)
        hbox.addWidget(self.calBtn)
        hbox.addWidget(self.resultbl)
        self.setLayout(hbox)

        self.calBtn.clicked.connect(self.calSlot)
    def calSlot(self):
        num1 = float(self.num1Edit.text()) if self.num1Edit.text().isdigit() else 0
        num2 = float(self.num2Edit.text()) if self.num2Edit.text().isdigit() else 0
        oper = self.op.currentText()
        if oper == '+':
            res = num1 + num2
        elif oper == '-':
            res = num1 - num2
        elif oper == '*':
            res = num1 * num2
        elif oper == '/' and num2 != 0:
            res = num1 / num2
        else:
            res = 'num2此处不能为0'

        self.resultbl.setText(str(res))






if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyWidget()
    w.show()
    sys.exit(app.exec_())
