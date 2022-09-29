import struct
import numpy as np

class DatasetLoader:
    def __init__(self, image_filepath, label_filepath):
        self.__image_filepath = image_filepath
        self.__label_filepath = label_filepath

    def __load_image_data(self):
        # 二进制打开文件
        binfile = open(self.__image_filepath, 'rb')
        # 读入内存
        buffers = binfile.read()
        binfile.close()
        # 解析数据
        magic_num, pic_num, height, width = struct.unpack_from('>4I', buffers, 0)
        # 计算偏移量
        offset = struct.calcsize('>4I')
        # 剩余数据大小
        pics_size = pic_num * height * width
        imgs = struct.unpack_from(f'>{pics_size}B', buffers, offset)
        # 将图片转化为三维数组
        img_array = np.reshape(imgs, (pic_num, height, width))
        return img_array

    def __binary_data(self, imgs):
        # 定义一个列表，存放图片数据
        binary_images = []
        for img in imgs:
            # 定义有效图片数据范围：
            image_left = 28
            image_right = 0
            image_top = 28
            image_bottom = 0
            for row in range(28):
                for col in range(28):
                    if img[row][col] > 0:
                        img[row][col] = 1
                        image_left = col if col < image_left else image_left
                        image_right = col if col > image_right else image_right
                        image_top = row if row < image_top else image_top
                        image_bottom = row if row > image_bottom else image_bottom
            # 图像的有效区域高和宽
            new_height = image_bottom - image_top + 1
            new_width = image_right - image_left +1
            # 图像居中
            Data_Mat = np.zeros((28, 28))
            new_left = (28 - new_width) // 2
            new_top = (28 - new_height) // 2

            for row in range(new_height):
                for col in range(new_width):
                    Data_Mat[row + new_top][col + new_left] = img[row + image_top][col + image_left]

            binary_images.append(Data_Mat.tolist())
        # 将整体转化成数组
        binary_images = np.array(binary_images)
        new_images = []
        for image in binary_images:
            new_image = np.reshape(image, (-1,))  # 将图片降至一维
            new_images.append(new_image)
        return np.array(new_images)

    def get_features(self):
        # 返回二值化后的特征
        # 缓存：
        import os
        cache_filepath = os.path.basename(self.__image_filepath) + '_cache.txt'
        if os.path.exists(cache_filepath):
            return np.loadtxt(cache_filepath)
        data = self.__binary_data(self.__load_image_data())
        np.savetxt(cache_filepath, data, fmt="%d", delimiter=' ')
        return data

    def get_lables(self):
        binfile = open(self.__label_filepath, 'rb')
        buffers = binfile.read()
        binfile.close()
        # 解析数据
        magic_num, label_num = struct.unpack_from('>II', buffers, 0)
        offset = struct.calcsize('>II')
        data = struct.unpack_from(f'>{label_num}B', buffers, offset)
        return data

if __name__ == '__main__':
    ldr = DatasetLoader('./dataset/train-images.idx3-ubyte', './dataset/train-labels.idx1-ubyte')
    ldr.get_features()
    ldr.get_lables()



