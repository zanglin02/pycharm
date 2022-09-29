'''
使用knn算法 对电影进行分类
'''
import numpy as np

# 创建数据集
def createDataSet():
    features = np.array([
        [3, 104],
        [8, 95],
        [1, 81],
        [111, 15],
        [99, 2],
        [88, 10]
    ])
    labels = ['Romance', 'Romance', 'Romance', 'Action', 'Action', 'Action']
    return features, labels

# Knn电影分类算法
def knnClassify(trainFeatures, labels, testFeature, k):
    '''
    :param trainFeatures: 训练数据集
    :param labels:        训练集对应的标签
    :param testFeature:   测试数据
    :param k:             KNN的k值 参数
    :return:              预测结果
    '''
    distances = []
    for index in range(len(trainFeatures)):
        diff = trainFeatures[index] - testFeature
        # print(diff)
        # print(diff**2)
        # print(sum(diff**2))
        # print(sum(diff**2)**0.5)
        distance = sum(diff**2)**0.5
        distances.append((distance, labels[index]))
    # print(distances)
    distances = sorted(distances, key=lambda x: x[0])
    print(distances)

    classCount = {}
    for index in range(k):
        classCount[distances[index][1]] = classCount.get(distances[index][1], 0) + 1
    # print(classCount)
    # print('=============================')
    # print(classCount.keys())
    # print(classCount.values())
    # print(classCount.items())
    sortedClassCount = sorted(classCount.items(), key=lambda x: x[1], reverse=True)
    # print(sortedClassCount)
    return sortedClassCount[0][0]
if __name__ == '__main__':
    dataSet = createDataSet()
    testFeature = np.array([10, 87])
    label = knnClassify(dataSet[0], dataSet[1], testFeature, 4)
    print(label)