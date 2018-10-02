from bs4 import BeautifulSoup
from requests import get as _get

url = 'https://www.morebranches.com/'

def scrape_data():
    _html = _get(url)
    soup = BeautifulSoup(_html.text, 'html.parser')
    blog_posts = soup.find('ul', class_='blog-widget-list').findAll('li')
    return blog_posts


def parse_post(post):
    link = post.a.get('href') or ''
    image = post.img.get('src')
    title = post.h2.text

    return link, image, title
