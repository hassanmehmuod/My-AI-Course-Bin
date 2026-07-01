#Python program to scrape website 

import requests
from bs4 import BeautifulSoup
import csv

with open("D:\\Work\\Github\\My-AI-Course-Bin\\Webscrapping\\Alibaba\\Alibaba.html", 'r', encoding='utf-8') as file:
    soup = BeautifulSoup(file, 'html5lib')

productList = []

table = soup.find_all('div', attrs = {'class':'fy26-product-card-wrapper'})

for row in table:
    product = {}
    product['url'] = row.find('a', attrs = {'class':'searchx-product-e-slider__link'})['href']
    product['img'] = row.img['src']
    product['discription'] = row.find(attrs = {'class':'searchx-product-e-title'}).text
    product['price'] = row.find(attrs = {'class':'searchx-product-price-price-main'}).text
    productList.append(product)

filename = 'D:\\Work\\Github\\My-AI-Course-Bin\\Webscrapping\\Alibaba\\alibaba-productsData-BeautifulSoup.csv'
with open(filename, 'w', newline='', encoding='utf-8') as f:
    w = csv.DictWriter(f,['url', 'img', 'discription', 'price'])
    w.writeheader()
    for product in productList:
        w.writerow(product)