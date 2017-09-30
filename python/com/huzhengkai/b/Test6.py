import multiprocessing
import time
import sys

def clock(interval):
    while True:
        print("The time is {0}".format(time.ctime()))
        time.sleep(interval)
if __name__ == '__main__':
    #p = multiprocessing.Process(target=clock, args=(5,))
    #p.start()
    print(sys.path)
    print(sys.argv)
