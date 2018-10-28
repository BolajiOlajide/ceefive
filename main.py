from time import sleep
from multiprocessing import Process


def jobA():
    for i in range(10):
        print(i, '<=======>')
        sleep(4)


def jobB():
    for i in range(5):
        print(i, '+++++++')
        sleep(10)


def runInParallel(*fns):
    proc = []
    for fn in fns:
        p = Process(target=fn)
        p.start()
        proc.append(p)
    for p in proc:
        p.join()


# runInParallel(jobA, jobB)