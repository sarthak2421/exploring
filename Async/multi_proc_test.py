import multiprocessing
import os

def test(num):
    for n in num:
        print(f'PID for {n} is {os.getpid()}')

nums=[1,2,3,4]
p1 = multiprocessing.Process(target=test,args=(nums,))
p1.start()
p1.join()




