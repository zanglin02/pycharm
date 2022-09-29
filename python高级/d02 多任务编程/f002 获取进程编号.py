import multiprocessing
import time
import os
def study():
    print('study_pid:', os.getpid())
    print('study:', multiprocessing.current_process)
    for i in range(5):
        print('正在学习...')
        time.sleep(0.5)
def work():
    print('work_pid:', os.getpid())
    print('work:', multiprocessing.current_process)
    for i in range(5):
        print('正在工作...')
        time.sleep(0.5)

if __name__ == '__main__':
    print('main_pid:', os.getpid())
    print('main:', multiprocessing.current_process)
    study_process = multiprocessing.Process(target=study)
    work_process = multiprocessing.Process(target=work)
    study_process.start()
    work_process.start()