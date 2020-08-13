
from bs4 import BeautifulSoup
from urllib.request import urlopen
import re

html = urlopen("https://morvanzhou.github.io/static/scraping/table.html").read().decode('utf-8')

soup = BeautifulSoup(html, features='html.parser')

img_links = soup.find_all("img", {"src":re.compile('.*?\.jpg')})

