import bs4
import requests
import pandas as pd

url = "https://quotes.toscrape.com/"

data = requests.get(url).content
html_data = bs4.BeautifulSoup(data, 'lxml')

# print(html_data)

quotes_data = html_data.findAll("span", class_="text")
author_data = html_data.findAll("small", class_="author")
tags_data = html_data.findAll("div", class_="tags")

# print(quotes_data)
# print(author_data)
# print(tags_data)

for i in range(len(quotes_data)):
    print(author_data[i].text)
    print(quotes_data[i].text)
    print(tags_data[i].text.strip())
    print()

# for j in author_data:
#
# for k in tags_data:
