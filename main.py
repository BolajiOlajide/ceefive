from os import getenv, path
import time

from dotenv import load_dotenv
from tweepy import (
    OAuthHandler, API
)

from scraper import scrape_data, parse_post


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


# implement actual tweeting and sleeping if main == name lol
if __name__ == "__main__":
    try:
        while True:
            new_posts = scrape_data()
            for post in new_posts:
                link, image, title = parse_post(post)
                status = """
                {0}

                {1}
                """.format(title, link)
                twitter.update_with_media(image, status)
                time.sleep(120)
            time.sleep(43000)
    except:
        pass
