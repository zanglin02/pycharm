class MyQueue:
    def __init__(self, data: iter, limit):
        self.limit = limit
        self.length = len(data)
        if self.limit < self.length:
            raise Exception('数据长度大于限定长度')
        else:
            self.data = [i for i in data]

    # 出队、入队、判断为空、清空、查看、重置队列长度
    def get(self):
        if self.is_empty():
            print('当前队列为空，无法出队')
        else:
            self.length -= 1
            return self.data.pop(0)
    def put(self, item):
        if self.limit == self.length:
            print('当前队列已满，无法入队')
        else:
            self.data.append(item)
            self.length += 1


    def is_empty(self):
        if self.length == 0:
            return True
        else:
            return False

    def clear(self):
        self.data.clear()
        self.length = 0

    def __str__(self):
        return str(self.data)

    def resize(self, new_limit):
        if self.length > new_limit:
            print('新的长度限制小于当前队列长度，拒绝修改')
        else:
            self.limit = new_limit

a = MyQueue([1, 4, 56, 67], 70)
print(a)

