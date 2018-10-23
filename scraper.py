from bs4 import BeautifulSoup
from requests import get as _get
from selenium import webdriver
from os import getcwd
from random import randint

url = 'https://www.amazon.com/gp/goldbox'
options = webdriver.ChromeOptions()
options.set_headless()


def create_driver():
    return webdriver.Chrome(getcwd() + '/chromedriver', chrome_options=options)


def scrape_product_review():
    random_product = get_random_product()


def get_random_product():
    driver = create_driver()
    driver.get(url)


def parse_post(post):
    link = post.a.get('href') or ''
    image = post.img.get('src')
    title = post.h2.text

    return link, image, title
