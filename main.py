from os import getenv, path
import time

from dotenv import load_dotenv
from tweepy import (
    OAuthHandler, API
)


dotenv_path = path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)

# twitter credentials
CONSUMER_KEY = getenv('CONSUMER_KEY')
CONSUMER_SECRET = getenv('CONSUMER_SECRET')
ACCESS_TOKEN = getenv('ACCESS_TOKEN')
ACCESS_SECRET = getenv('ACCESS_SECRET')

auth = OAuthHandler(
    CONSUMER_KEY, CONSUMER_SECRET
)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
twitter = API(auth)

time.sleep(3000)
