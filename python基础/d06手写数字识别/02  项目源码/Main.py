import sys

import PyQt5.QtCore.QUrl

from DatasetLoader import DatasetLoader
from KnnAlgorithm import KnnAlgorithm
from PaintPad import PaintPad

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.__train_ldr = DatasetLoader('./dataset/train-images.idx3-ubyte', './dataset/train-labels.idx1-ubyte')
        self.init_ui()

    def init_ui(self):
        # 绘制界面 绑定信号与槽函数
        # 手写板
        self.paintBox = QGroupBox('Hand Write Area')
        self.paintPad = PaintPad()

        # 二进制
        self.binViewBox = QGroupBox('Binary Image')
        self.binViewLabel = QLabel()
        self.binViewLabel.setAlignment(Qt.AlignCenter)

        # 结果展示
        self.resultBox = QGroupBox('Result Display')
        self.resultDisplay = QLabel("hello")
        font = QFont()
        font.pointSize(100)
        self.resultDisplay.setFont(font)
        self.resultDisplay.setAlignment(Qt.AlignCenter)


