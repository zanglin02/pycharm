import threading
import time
def task():
    for i in range(5):
        print(f'任务执行中')
        time.sleep(1)

if __name__ == '__main__':
    sub_thread = threading.Thread(target=task, daemon=True)
    sub_thread.start()
    time.sleep(2.5)
    print('over')
    exit()
