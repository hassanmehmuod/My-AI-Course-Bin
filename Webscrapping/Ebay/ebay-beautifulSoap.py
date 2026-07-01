#Python program to scrape website 

import requests
from bs4 import BeautifulSoup
import csv

with open("D:\\Work\\Github\\My-AI-Course-Bin\\Webscrapping\\Ebay\\ebay.html", 'r', encoding='utf-8') as file:
    soup = BeautifulSoup(file, 'html5lib')

smartphone = []

table = soup.find('section', attrs = {'class':'brw-river'})

for row in table.find_all('li',
                          attrs = {'class':'brwrvr__item-card'}):
    smartphones = {}
    smartphones['url'] = row.a['href']
    smartphones['img'] = row.img['src']
    smartphones['discription'] = row.img['alt']
    smartphone.append(smartphones)

filename = 'D:\\Work\\Github\\My-AI-Course-Bin\\Webscrapping\\Ebay\\smart-phonesData-BeautifulSoup.csv'
with open(filename, 'w', newline='', encoding='utf-8') as f:
    w = csv.DictWriter(f,['url', 'img', 'discription'])
    w.writeheader()
    for smartphones in smartphone:
        w.writerow(smartphones)