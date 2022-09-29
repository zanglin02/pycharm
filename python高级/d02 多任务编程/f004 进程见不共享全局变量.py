import multiprocessing
import time

g_list = list()
# 添加数据任务
def add_task():
    for i in range(5):
        print('正在添加数据...')
        g_list.append(i)
        time.sleep(0.2)
# 读取数据任务
def read_task():
    print(f'read_data:{g_list}')
if __name__ == '__main__':
    add_process = multiprocessing.Process(target=add_task)
    read_process = multiprocessing.Process(target=read_task)
    add_process.start()
    # join 会让主进程等待子进程执行结束后再继续向下执行
    add_process.join()
    read_process.start()
# 注意：不共享全局变量的意思是每个进程操作的实际上是自己内存空间下的同名对象
