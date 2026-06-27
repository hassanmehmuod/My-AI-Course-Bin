#Python program to scrape website 
#and save quotes from website
import requests
from bs4 import BeautifulSoup
import csv

with open('D:\\Work\\Github\\My-AI-Course-Bin\\Webscrapping\\Amazon\\AmazonData.html', encoding='utf-8') as file:
    soap = BeautifulSoup(file, 'html5lib')

devices = []

table = soap.find('div', attrs = {'data-normaliseheight': 'false'})

for row in table.find_all('div', class_='puis-card-container'):
    device = {}
    device['url'] = row.a['href']
    device['img'] = row.img['src']
    device['discription'] = row.img['alt']
    devices.append(device)

filename = 'D:\\Work\\Github\\My-AI-Course-Bin\\Webscrapping\\Amazon\\amazon-deivceData-BeautifulSoap.csv'
with open(filename, 'w', newline='', encoding='utf-8') as f:
    w = csv.DictWriter(f,['url','img','discription'])
    w.writeheader()
    for device in devices:
        w.writerow(device)

