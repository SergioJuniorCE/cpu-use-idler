import time
import sys
from itertools import repeat
from multiprocessing import Pool, cpu_count


def f(x, runtime, sleeptime, busycycles):
    cnt = 0
    while True:
        if sleeptime and cnt % busycycles == 0:
            time.sleep(sleeptime)
        x*x
        cnt += 1


if __name__ == '__main__':
    runtime = 1
    sleeptime = 0.01
    busycycles = 2000000
    processes = 2
    print(
        f'Running for eternity with sleep time of {sleeptime}s per {busycycles} cycles utilizing {processes} cores')
    pool = Pool(processes)
    pool.starmap(f, zip(range(processes), repeat(runtime),
                 repeat(sleeptime), repeat(busycycles)))
