# 图像二值化 我们只关心图像的形状 不关心颜色
# 将图像居中处理 提高正确率
import numpy as np
import struct
def get_images():
    filename = './dataset/train-images.idx3-ubyte'
    binfile = open(filename, 'rb')
    buffers = binfile.read()
    magic_num, pic_num, height, width = struct.unpack_from('>4I', buffers, 0)
    offset = struct.calcsize('>4I')
    pics_size = pic_num * height * width
    data_fmt = f'>{pics_size}B'
    imgs = struct.unpack_from(data_fmt, buffers, offset)
    img_array = np.reshape(imgs, (pic_num, height, width))
    return img_array

if __name__ == '__main__':
    imgs = get_images()
    binary_images = []
    # 遍历所有图片
    for img in imgs:
        image_left = 28
        image_right = 0
        image_top = 28
        image_bottom = 0
        for row in range(28):
            for col in range(28):
                if img[row][col] > 0:
                    img[row][col] = 1
                    image_left = col if col < image_left else image_left
                    image_right = col if col < image_right else image_right
                    image_top = row if row < image_top else image_top
                    image_bottom = row if row < image_bottom else image_bottom
        # 计算有效图像的高度和宽度
        new_height = image_bottom - image_top + 1
        new_width = image_right -image_left + 1
        # 构建一个全为B的二维图像矩阵
        dataMat = np.zeros((28, 28))
        # 计算偏移量
        left = (28 - new_width) // 2
        top = (28 - new_height) //2

        # 居中操作
        for row in range(new_height):
            for col in range(new_width):
                dataMat[row+top][col+left] = img[row+image_top][col+image_left]
        # 将图像降至一维
        dataMat = np.reshape(dataMat, (-1))
        binary_images.append(dataMat)
