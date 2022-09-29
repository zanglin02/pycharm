import multiprocessing
import time
import os
# 带参数的任务（函数）
def task(count):
    pid = os.getpid()
    for i in range(count):
        print(f'[{pid}]任务正在执行...')
        time.sleep(0.2)

if __name__ == '__main__':
    # 通过位置参数方式给任务传参，args=(args1, args2)元组
    sub_process = multiprocessing.Process(target=task, args=(3,))
    sub_process.start()

    # 通过关键字传参,kwargs={'key':walue, 'key':value)
    sub_process_2 = multiprocessing.Process(target=task, kwargs={"count": 3})
    sub_process_2.start()