# 加载数据集
import numpy as np
import struct
"""
⼿写数字识别数据格式
TRAINING SET IMAGE FILE (train-images-idx3-ubyte):
[offset] [type]             [value]             [description]
0000     32 bit integer     0x00000803(2051)    magic number
0004     32 bit integer     60000               number of images
0008     32 bit integer     28                  number of rows
0012     32 bit integer     28                  number of columns
0016     unsigned byte      ??                  pixel
0017     unsigned byte      ??                  pixel
........
xxxx unsigned byte ?? pixel
"""
filename = './dataset/train-images.idx3-ubyte'
# 二进制b 读r 方式打开文件
binfile = open(filename, 'rb')
# 读入内存
buffers = binfile.read()
print(len(buffers))
"""
tup = struct.unpack_from('>IIII', buffers, 0)
print(tup)

# 字节序不同结果不同
data = [1, 2, 3]
sdata  = struct.pack('<LHB', *data)
print(sdata)
sdata = struct.pack('>LHB', *data)
print(sdata)
"""
magic_num, pic_num, height, width = struct.unpack_from('>4I', buffers, 0)
# 计算偏移量
offset = struct.calcsize('>4I')
# 计算剩余数据总大小（图片）
pics_size = pic_num * height * width
# 剩余数据格式计算
data_fmt = f'>{pics_size}B'
# 解析图片数据
imgs = struct.unpack_from(data_fmt, buffers, offset)

print(len(imgs))
# 将imgs一维数据转化为数量*高*宽的3维数据
img_array = np.reshape(imgs, (pic_num, height, width))
print(f'img_array.shape:{img_array.shape}')
print(img_array[0])

from PIL import Image
image = Image.fromarray(img_array[0])
image.show()
print(np.uint8(img_array[0]))
image = Image.fromarray(np.uint8(img_array[0]))
image.save('test.png')