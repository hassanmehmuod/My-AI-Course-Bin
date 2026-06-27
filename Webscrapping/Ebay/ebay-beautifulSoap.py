

import requests
from bs4 import BeautifulSoup
import csv

URL = "https://www.ebay.com/b/Cell-Phones-Smartphones/9355/bn_320094"
r = requests.get(URL)

soap = BeautifulSoup(r.content, 'html5lib')

smartphones = []

table = soap.find('div', attrs = {})