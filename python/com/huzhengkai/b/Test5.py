import multiprocessing
import time

def worker(procnum, return_dict):
    print(str(procnum) + ' represent!')
    time.sleep(2)  #这个函数是并行执行的
    return_dict[procnum] = procnum


if __name__ == '__main__':
    manager = multiprocessing.Manager()
    return_dict = manager.dict()
    jobs = []
    for i in range(5):
        p = multiprocessing.Process(target=worker, args=(i,return_dict))
        jobs.append(p)
        p.start()

    for proc in jobs:
        proc.join()
    print(return_dict.values())
