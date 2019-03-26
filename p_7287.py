import requests
from bs4 import BeautifulSoup as bs

my_baekjoon = requests.get("https://www.acmicpc.net/user/handy113")
my_baekjoon_html = my_baekjoon.text

soup = bs(my_baekjoon_html, "html.parser")

#print(soup)
my_id = soup.select('body > div.wrapper > div.container.content > div.row > div:nth-of-type(1) > div > h1')
my_solved_p = soup.select('#statics > tbody > tr:nth-of-type(2) > td')
print(my_id[0].text)
print(my_solved_p[0].text)
