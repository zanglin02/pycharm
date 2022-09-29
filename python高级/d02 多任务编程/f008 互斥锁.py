import threading
import time

num = 0
# 在主线程内创建全局互斥锁
lock = threading.Lock()
def sum1():
    lock.acquire()  # 上锁
    for i in range(1000000):
        global num
        num += 1
    print(f'sum1:{num}')
    lock.release()  # 释放锁

def sum2():
    lock.acquire()  # 上锁
    for i in range(1000000):
        global num
        num += 1
    print(f'sum2:{num}')
    lock.release()  # 释放锁

if __name__ == '__main__':
    first = threading.Thread(target=sum1)
    second = threading.Thread(target=sum2)
    first.start()
    second.start()
    time.sleep(1)
    print(num)
