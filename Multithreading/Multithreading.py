# Multiprocessing
import multiprocessing 
import time

COUNT = 50000000

def countdown(n):
    while n>0:
        n -= 1

if __name__ == '__main__':
    start = time.time()
    countdown(COUNT)
    end = time.time()
    print(f'Time with single thread: {end-start} s')

    # creating processes 
    p1 = multiprocessing.Process(target=countdown, args=(COUNT//2, )) 
    p2 = multiprocessing.Process(target=countdown, args=(COUNT//2, )) 

    start = time.time()
    p1.start() # starting process 1 
    p2.start()

    p1.join() # wait until process is finished 
    p2.join() 
    end = time.time()

    print(f'Time with multiple (two here) threads in parallel: {end-start} s')