import multiprocessing
import time
# 学习任务
def study():
    for i in range(5):
        print('正在学习...')
        time.sleep(0.5)

# 工作任务
def work():
    for i in range(5):
        print('正在工作...')
        time.sleep(0.5)

if __name__ == '__main__':
    # group : 进程组
    # target : 执行的任务名（函数名）
    # name : 进程名称 默认情况 Process-1
    study_process = multiprocessing.Process(group=None, target=study, name='study-process')
    work_process = multiprocessing.Process(target=work)
    # 启动进程执行对应任务
    study_process.start()
    work_process.start()