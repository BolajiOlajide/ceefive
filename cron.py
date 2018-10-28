import schedule
import time

from tweet import post_tweet


def job():
    print("I'm working...")
    post_tweet()


schedule.every(1).seconds.do(job)
# schedule.every().hour.do(job)
# schedule.every().day.at("10:30").do(job)
# schedule.every().monday.do(job)
# schedule.every().wednesday.at("13:15").do(job)

print('Legggooooo!!!! 💩💩💩💩💩💩')

while True:
    try:
        print('starting work')
        schedule.run_pending()
        time.sleep(60)
    except KeyboardInterrupt:
        print('The user stopped my operation')
        exit()
