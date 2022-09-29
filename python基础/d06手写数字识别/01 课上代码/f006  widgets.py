"""
pyqt5  窗口程序
"""
import sys  # 系统配置库
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton
"""
QApplication: 应用类 一个QT程序必须构造一个应用类实例
QWidget:      窗口类(面板) 可以摆放控件
QLabel:       标签控件 可以显示文字 也可以显示图片/gif  
QPushButton:  按钮控件 可以接受用户点击      
"""

class BasicQt(QWidget):
    def __init__(self):
        # 调用父类的构造函数 做初始化
        super().__init__()
        self.init_ui()

    def setText(self):
        """
        自定义槽函数 修改Qlabel文字
        setText()
        """
        self.lbl.setText('Hello PYQT5~~~~~')

    def init_ui(self):
        # 初始化ui
        # 设置窗口
        self.resize(600, 400)
        self.lbl = QLabel('图形化界面程序', self)

        """
        坐标系:
        窗口的左上角(0.0)
        水平方向向右为x轴正方向 0-599
        垂直方向向下为y轴正方向 0-399
        move函数的参数为移动后的控件位置 不是相对当前位置的偏移量
        """

        self.lbl.move(0, 200)
        self.lbl.move(300, 0)

        # 构造一个按钮
        self.btn = QPushButton('退出程序', self)
        self.btn.move(480, 360)

        """
        信号与槽函数机制
        功能：点击按钮的时候 退出程序
        将按钮的clicked点击信号 绑定到退出程序函数上
        """

        self.btn.clicked.connect(exit)
        self.setLblTextBtn = QPushButton('修改文字', self)
        self.setLblTextBtn.move(200, 350)
        self.setLblTextBtn.clicked.connect(self.setText)





if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = BasicQt()
    w.show()
    sys.exit(app.exec_())
