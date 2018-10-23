import schedule
import time

def job():
    print("I'm working...")

schedule.every(1).minutes.do(job)
# schedule.every().hour.do(job)
# schedule.every().day.at("10:30").do(job)
# schedule.every().monday.do(job)
# schedule.every().wednesday.at("13:15").do(job)

while True:
    try:
        print('starting work')
        schedule.run_pending()
        time.sleep(100)
    except KeyboardInterrupt:
        print('The user stopped my operation')
        exit()
