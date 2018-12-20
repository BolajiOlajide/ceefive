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

schedule.every(20000).seconds.do(job)


def start_job():
    while True:
        try:
            print('starting work')
            schedule.run_pending()
            print('kdkdlsdl')
            sleep(20000)
        except KeyboardInterrupt:
            print('The user stopped my operation')
            exit()


if __name__ == '__main__':
    # https://stackoverflow.com/questions/31092538/heroku-node-js-error-r10-boot-timeout-web-process-failed-to-bind-to-port-w/31094668#31094668  # noqa: E501
    # this helped with knowing I can just use heroku as a worker instead of setting the app as a web service # noqa: E501
    start_job()
