"""
TRAINING SET IMAGE FILE (train-images-idx1-ubyte):
[offset] [type]             [value]             [description]
0000     32 bit integer     0x00000803(2051)    magic number
0004     32 bit integer     60000               number of labels
0009     unsigned byte      ??                  label
0010     unsigned byte      ??                  label
........
"""
import numpy as np
import struct

filename = './dataset/train-labels.idx1-ubyte'
binfile = open(filename, 'rb')
buffers = binfile.read()

magic_num, labels_num = struct.unpack_from('>2I', buffers, 0)
data_fmt = f'>{labels_num}B'
offset = struct.calcsize('>2I')
labels = struct.unpack_from(data_fmt, buffers, offset)
labels_array = np.array(labels)
