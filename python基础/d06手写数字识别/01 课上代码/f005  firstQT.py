from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = QWidget()
    label = QLabel('Hello Python', w)
    btn = QPushButton('按钮', w)
    btn.setGeometry(100, 100, 100, 50)
    w.show()
    sys.exit(app.exec_())
