import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import numpy as np

class PaintPad(QWidget):
    def __init__(self):
        super().__init__()
        '''
        根据鼠标的轨迹曲线，我们需要一个列表来保存所有移动过的点
        '''
        self.pos_xy = []

        # 定义调色板
        pal = QPalette()
        pal.setColor(QPalette.window, Qt.white)
        self.setAutoFillBackground(True)
        self.setPalette(pal)

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        pen = QPen(Qt.black, 50, Qt.solidLine)
        painter.setPen(pen)
        if len(self.pos_xy) > 1:
            point_start = self.pos_xy[0]
            for point_end in self.pos_xy:
                if point_start == (-1, -1) or point_end == (-1, -1):
                    point_start = point_end
                    continue
                painter.drawLine(point_start[0], point_start[1], point_end[0], point_end[1])
                point_start = point_end
        painter.end()
    def mouseMoveEvent(self, event):
        """
        (按住)鼠标移动：将鼠标当前，添加入pos_xy列表
        self.update()相当于调用了paintEvent()
        注意调用update()之前画的痕迹会清空
        """
        pos_tmp = (event.pos().x(), event.pos().y())
        self.pos_xy.append(pos_tmp)
        self.update()

    def mouseReleaseEvent(self, event):
        """
        鼠标松开时
        我们向pos_xy内添加一个断点（-1，-1）
        画的时候需要判断一下
        如果遇到断点则跳过
        """
        pos_tmp = (-1, -1)
        self.pos_xy.append(pos_tmp)
        self.update()

    def clear(self):
        """
        清空画板
        """
        self.pos_xy.clear()
        self.update()

    def getPaintData(self):
        '''
        将控件内容转化为图片，再转换为数组格式
        '''
        fileName = './test.png'
        fileName1 = './test1.png'
        fileName2 = './test2.png'
        fileName3 = './test3.png'

        pixmap = QPixmap(self.size())
        self.render(pixmap)
        img = pixmap.toImage()
        img.save(fileName1)
        img_height = img.size().height()
        img_width = img.size().width()
        print(img_width)
        print(img_height)

        # 获取有效图像
        xPoint_left = img_width - 1
        xPoint_right = 0
        yPoint_top = img_height - 1
        yPoint_bottom = 0

        for row in range(img_height):
            for col in range(img_width):
                if(qGray(img.pixel(row, col))) == 0:  # 黑色为0
                    xPoint_left = col if col < xPoint_left else xPoint_left
                    xPoint_right = col if col > xPoint_right else xPoint_right
                    yPoint_top = row if row < yPoint_top else yPoint_top
                    yPoint_bottom = row if row > yPoint_bottom else yPoint_bottom
        height = yPoint_bottom - yPoint_top
        width = xPoint_right - xPoint_left
        # 裁剪图片
        img_cut = img.copy(xPoint_left, yPoint_top, width, height)
        img_cut.save(fileName2)

        # 创建正方形图片 边长为imfcut宽和高更大的值
        sqLen = max(width, height)
        img_white = QPixmap(sqLen, sqLen)
        img_white.fill(Qt, white)
        img_white_p = img_white.toImage()

        # 将剪裁图片（img_cut）放入正方形图片（img_white_p）中
        if height > width:
            offset = (height - width) // 2
            for i in range(height):
                for j in range(width):
                    img_white_p.setPixelColor(j+offset, i, img_cut.pixelColor(j, i))
        else:
            offset = (width - height) // 2
            for i in range(height):
                for j in range(width):
                    img_white_p.setPixelColor(j, i+offset, img_cut.pixelColor(j, i))
        img_white_p.save(fileName3)
        # 缩放为20*20的图片后 放到28*28的空白图片里面
        img_20_20_p = img_white_p.scaled(20, 20, Qt.IgnoreAspectRatio)
        img_28_28 = QPixmap(28, 28)
        img_28_28.fill(Qt.white)
        img_28_28_p = img_28_28.toImage()
        # 将图片2020的图片居中放置到2828的图片中去
        for i in range(20):
            for j in range(28):
                img_28_28_p.setPixelColor(j+4, i+4, img_20_20_p.pixelColor(j, i))
                img_20_20_p.save(fileName)

        imgMat = []
        for i in range(28):
            img_row = []
            for j in range(28):
                color = qGray(img_28_28_p.pixel(j, i))
                if color == 0:
                    img_row.append(1)
                else:
                    img_row.append(0)
            imgMat.append(img_row)
        return np.array(imgMat)





if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = PaintPad()
    w.show()
    sys.exit(app.exec_())
