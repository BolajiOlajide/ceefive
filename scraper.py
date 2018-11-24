from os import getcwd, path, getenv
from random import randint

from bs4 import BeautifulSoup
from selenium import webdriver
from dotenv import load_dotenv


url = 'https://www.amazon.com/gp/goldbox'
options = webdriver.ChromeOptions()
options.set_headless()

dotenv_path = path.join(path.dirname(__file__), '.env')
load_dotenv(dotenv_path)

CHROMEDRIVER = getenv('CHROMEDRIVER_FILE_NAME', 'chromedriver')
# THis is an alias for Chrome Driver Path (CDP)
CDP = '/{}'.format(CHROMEDRIVER)


def create_driver():
    return webdriver.Chrome(getcwd() + CDP, chrome_options=options)


def scrape_product_review():
    """
    scrape for product review
    """
    driver = create_driver()
    random_product_link = get_random_product_link(driver)
    return get_product_details(driver, random_product_link)


def pick_random_item(items):
    """
    return random item from a list of items
    """
    number_of_items = len(items)
    if number_of_items > 0:
        random_item_index = randint(0, (number_of_items - 1))
        return items[random_item_index]
    return None


def get_random_product_link(driver):
    """
    the method returns the link of a random product from today's
    deals on Amazon
    """
    try:
        driver.get(url)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        widget_content = soup.find("div", {"id": "widgetContent"})
        products = widget_content.find_all('div', class_='tallCellView')
        random_product = pick_random_item(products)
        if not random_product:
            return None
        return random_product.find('a', id="dealTitle")['href'] or None
    except:  # noqa: E722
        return None


def get_product_details(driver, product_link):
    try:
        driver.get(product_link)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        product_title = soup.find('span', {'id': 'productTitle'}).text.replace('\n', '').strip() or ''
        product_image_url = soup.find('img', {'id': 'landingImage'})['src']
        product_reviews = soup.select('span.a-size-base.review-text')
        random_product_review = pick_random_item(product_reviews)
        random_review_text = random_product_review.find('div', class_="a-expander-content").text or ''
        return {
            'product_title': product_title,
            'product_image_url': product_image_url,
            'random_review_text': random_review_text,
            'product_link': product_link
        }
    except:  # noqa: #722
        return None
