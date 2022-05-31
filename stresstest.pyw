'''
Examples:

Run for 15 seconds maxing out all processors:
  stress.py 15

Run for 15 seconds with each subprocess sleeping for 0.01s every 100,000 cycles across all processors (on my machine it's about a 50% duty cycle):
  stress.py 15 0.01 100000

Run for 15 seconds, sleep 0.01s every 100,000 cycles, but only use a max of 8 processors:
  stress.py 15 0.01 100000 8
'''

import time
import sys
from itertools import repeat
from multiprocessing import Pool, cpu_count


def f(x, runtime=1, sleeptime=0, busycycles=100000):
    cnt = 0
    while True:
        if sleeptime and cnt % busycycles == 0:
            time.sleep(sleeptime)
        x*x
        cnt += 1


if __name__ == '__main__':
    runtime = 1
    sleeptime = 0.01
    busycycles = 100000 if len(sys.argv) <= 2 else int(sys.argv[1])
    processes = cpu_count() if len(sys.argv) <= 2 else int(
        sys.argv[2]) if 0 < int(sys.argv[2]) <= cpu_count() else cpu_count()
    print(
        f'Running for eternity with sleep time of {sleeptime}s per {busycycles} cycles utilizing {processes} cores')
    pool = Pool(processes)
    pool.starmap(f, zip(range(processes), repeat(runtime),
                 repeat(sleeptime), repeat(busycycles)))
