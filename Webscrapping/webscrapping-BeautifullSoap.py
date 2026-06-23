#Python program to scrape website 

import requests
from bs4 import BeautifulSoup
import csv

URL = "http://www.daraz.pk/catalog/?spm=a2a0e.tm80331704.cate_5.5.77cc5aa7fPImi7&q=Smart%20Phones&from=hp_categories&src=all_channel"
r = requests.get(URL)

soup = BeautifulSoup(r.content, "html5lib")

smartphone = []

table = soup.find('div', attrs = {'data-qa-locator': 'general-products'})

for row in table.find_all('div',
                          attrs = {'class':'Bm3ON'}):
    smartphones = {}
    smartphones['url'] = row.a['href']
    smartphones['img'] = row.img['src']
    smartphones['discription'] = row.img['alt']
    smartphone.append(smartphones)

filename = 'MY-AI-COURSE-BIN/Webscrapping/smart-phonesData-BeautifulSoap.csv'
with open(filename, 'w', newline='') as f:
    w = csv.DictWriter(f,['url', 'img', 'discription'])
    w.writeheader()
    for smartphones in smartphone:
        w.writerow(smartphones)

