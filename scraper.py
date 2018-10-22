from bs4 import BeautifulSoup
from requests import get as _get
from selenium import webdriver
from os import getcwd

url = 'https://www.amazon.com/gp/goldbox'
options = webdriver.ChromeOptions()
options.set_headless()


def scrape_data():
    # _html = _get(url)
    # soup = BeautifulSoup(_html.text, 'html.parser')
    # blog_posts = soup.find('ul', class_='blog-widget-list').findAll('li')
    # return blog_posts
    driver = webdriver.Chrome(getcwd() + '/chromedriver', chrome_options=options)
    driver.get(url)


def parse_post(post):
    link = post.a.get('href') or ''
    image = post.img.get('src')
    title = post.h2.text

    return link, image, title
