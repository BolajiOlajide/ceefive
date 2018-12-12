from os import getenv, path, chdir
from random import choice
import string

from dotenv import load_dotenv
from requests import get as _get
from tweepy import OAuthHandler, API, TweepError

from scraper import scrape_product_review


dotenv_path = path.join(path.dirname(__file__), '.env')
load_dotenv(dotenv_path)

# twitter credentials
CONSUMER_KEY = getenv('CONSUMER_KEY', '')
CONSUMER_SECRET = getenv('CONSUMER_SECRET', '')
ACCESS_TOKEN = getenv('ACCESS_TOKEN', '')
ACCESS_SECRET = getenv('ACCESS_SECRET', '')

auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
twitter = API(auth)


def post_tweet():
    try:
        print('starting to scrape data \n\n')
        product_data = scrape_product_review()
        if not product_data:
            print('Error scraping data! \n\n')
            return None

        product_title = product_data.get('product_title')
        product_link = product_data.get('product_link')
        random_review_text = product_data.get('random_review_text')
        product_image_url = product_data.get('product_image_url')

        # tweet the product title and image
        print('tweeting title \n\n')
        formatted_title = 'TITLE: \n{}'.format(product_title)
        response = tweet_product_title_image(
            formatted_title, product_image_url)
        title_response_status_id = response._json.get('id')

        # tweet the review
        print('tweeting review \n\n')
        formatted_review_text = 'REVIEW: \n{}'.format(random_review_text)
        print(formatted_review_text)
        review_response_id = tweet_product_review(
            formatted_review_text, title_response_status_id)

        # tweet the product link
        print('tweeting link \n\n')
        formatted_product_link = 'LINK: \n{}'.format(product_link)
        twitter.update_status(
            formatted_product_link, in_reply_to_status_id=review_response_id)

        print('Done tweeting this product! \n\n')
        return False
    except TweepError as error:
        print(error.reason)
        return None


def tweet_product_title_image(product_title, product_image_url):
    chdir('images')
    product_image = grab_image(product_image_url)
    tweet_response = twitter.update_with_media(
        product_image,
        status=product_title
    )
    chdir('..')
    return tweet_response


def generate_random_string():
    chars = string.ascii_uppercase + string.digits
    return ''.join(choice(chars) for _ in range(11))


def grab_image(product_image_url):
    response = _get(product_image_url)
    filename = '{}.jpg'.format(generate_random_string())
    if response.status_code == 200:
        with open(filename, 'wb') as file:
            file.write(response.content)
            file.close()
        return filename
    else:
        return None


def split_text(s, count):
    return [''.join(x) for x in zip(*[list(s[z::count]) for z in range(count)])]  # noqa: E501


def tweet_product_review(review_text, title_status_id):
    try:
        splitted_review = split_text(review_text, 279)
        recurring_status_id = title_status_id
        # import pdb; pdb.set_trace()
        for review_slice in splitted_review:
            response = twitter.update_status(
                review_slice,
                in_reply_to_status_id=recurring_status_id
            )
            # import pdb; pdb.set_trace()
            recurring_status_id = response._json.get('id')
        return recurring_status_id
    except:  # noqa: E722
        print('error tweeting product review')
