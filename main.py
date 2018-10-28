from time import sleep

import schedule

from tweet import post_tweet
# from multiprocessing import Process


# def jobA():
#     for i in range(10):
#         print(i, '<=======>')
#         sleep(4)

def job():
    print("I'm working...")
    post_tweet()


# def jobB():
#     for i in range(5):
#         print(i, '+++++++')
#         sleep(10)


# def runInParallel(*fns):
#     proc = []
#     for fn in fns:
#         p = Process(target=fn)
#         p.start()
#         proc.append(p)
#     for p in proc:
#         p.join()


# runInParallel(jobA, jobB)

schedule.every(3000).seconds.do(job)


def start_job():
    while True:
        try:
            print('starting work')
            schedule.run_pending()
            print('kdkdlsdl')
            sleep(3600)
        except KeyboardInterrupt:
            print('The user stopped my operation')
            exit()


# if __name__ == '__main__':
#     start_job()

def worker_exit(server, worker):
    print('Bye bye! 😣 😣 😣 😣')


def post_worker_init(server):
    start_job()
