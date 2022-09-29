import threading
import time
def study():
    for i in range(3):
        print(f'[{i}]正在学习...')
        time.sleep(0.5)
def work():
    for i in range(3):
        print(f'[{i}]正在工作...')
        time.sleep(0.5)

if __name__ == '__main__':
    study_thread = threading.Thread(target=study)
    work_thread = threading.Thread(target=work)
    study_thread.start()
    work_thread.start()