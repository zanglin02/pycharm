import numpy as np

class KnnAlgorithm:
    @staticmethod
    def predict(inputs, features, labels, k):
        dataSstSize = features.shape[0]
        testFeatureArray = np.tile(inputs, (dataSstSize, 1))
        diffMat = testFeatureArray - features
        sqDiffMat = diffMat ** 2
        sqDistance = sqDiffMat.sum(axis=1)
        distances = sqDistance ** 0.5
        sortedDistances = distances.argsort()
        classCount = {}
        for i in range(k):
            label = labels[sortedDistances[i]]
            classCount[label] = classCount.get(label, 0) + 1

        sortedClassCount = sorted(classCount.items(), key=lambda x:x[1], reverse=True)
        return sortedClassCount[0][0]

if __name__ == '__main__':
    from DatasetLoader import DatasetLoader
    ldr = DatasetLoader('./dataset/train-images.idx3-ubyte', './dataset/train-labels.idx1-ubyte')
    features, labels = ldr.get_features(), ldr.get_lables()

    test_ldr = DatasetLoader('./dataset/t10k-images.idx3-ubyte', './dataset/t10k-labels.idx1-ubyte')
    test_features, test_labels = test_ldr.get_features(), test_ldr.get_lables()

    correct = 0
    test_num = len(test_labels)
    print('predict begin')
    for i in range(test_num):
        result = KnnAlgorithm.predict(test_features[i], features, labels, 3)
        if result == test_labels[i]:
            correct += 1
        print('predict end!!!')
        print(f'rate:{correct/test_num}')
