import threading
num = 0
def sum_num1():
    for i in range(1000000):
        global num
        num += 1
    print(f'sum1:{num}')


def sum_num2():
    for i in range(1000000):
        global num
        num += 1
    print(f'sum2:{num}')

if __name__ == '__main__':
    first = threading.Thread(target=sum_num1)
    second = threading.Thread(target=sum_num2)
    first.start()
    second.start()
