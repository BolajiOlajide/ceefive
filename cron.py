# import time

from flask import Flask
# import schedule

# from tweet import post_tweet
# from main import runInParallel


# def job():
#     print("I'm working...")
#     post_tweet()


# def start_job():
#     while True:
#         try:
#             print('starting work')
#             schedule.run_pending()
#             time.sleep(60)
#         except KeyboardInterrupt:
#             print('The user stopped my operation')
#             exit()


app = Flask(__name__)


# schedule.every(1).seconds.do(job)
# schedule.every().hour.do(job)
# schedule.every().day.at("10:30").do(job)
# schedule.every().monday.do(job)
# schedule.every().wednesday.at("13:15").do(job)


@app.route('/')
def index():
    return 'Ceefive! 😆 😆 😆 😆 😆 😆'


if __name__ == '__main__':
    print('Legggooooo!!!! 💩💩💩💩💩💩')
    app.run()
    # runInParallel(app.run, start_job)
