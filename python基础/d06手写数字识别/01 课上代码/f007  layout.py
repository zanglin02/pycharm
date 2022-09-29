import random, sys
from PyQt5 import QtWidgets, QtCore, QtGui

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.button = QtWidgets.QPushButton("Click Me")
        self.text = QtWidgets.QLabel('Hello World')
        font = QtGui.QFont()
        font.setPointSize(50)
        self.text.setFont(font)
        self.text.setAlignment(QtCore.Qt.AlignCenter)
        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)
        self.setLayout(self.layout)

        self.button.clicked.connect(self.changeText)
    def changeText(self):
        texts = ['Hello World', 'Hello Python', 'Hello PYQT5']
        self.text.setText(random.choice(texts))




if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = MyWidget()
    w.resize(800, 600)
    w.show()
    sys.exit(app.exec_())
