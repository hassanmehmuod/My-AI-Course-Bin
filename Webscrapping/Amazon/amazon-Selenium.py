from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import csv
import time

url = "https://www.amazon.com/b?_encoding=UTF8&node=21217035011&ref_=cct_cg_SHnav2_2a1&pf_rd_p=12b44fc7-b592-4f55-b8d7-32c20b211ef1&pf_rd_r=CZEXWGP16MP0B5YJHP3T"

cService = webdriver.ChromeService(executable_path='D:\\Work\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe')
driver = webdriver.Chrome(service=cService)

driver.get(url)
time.sleep(5)
devicelist = []
deviceDiv = driver.find_elements(By.XPATH,"//div[contains(@class, 'puis-card-container')]")
for p in range(len(deviceDiv)):
    device = {}
    innerImg = deviceDiv[p].find_element(By.TAG_NAME, "img")
    innera = deviceDiv[p].find_element(By.TAG_NAME, "a")
    device['img'] = innerImg.get_attribute('src')
    device['discription'] = innerImg.get_attribute('alt')
    device['url'] = innera.get_attribute('href')
    devicelist.append(device)

filename = 'D:\\Work\\Github\\My-AI-Course-Bin\\Webscrapping\\Amazon\\Devices-Data-Selenium.csv'
with open(filename, 'w', newline='',encoding='utf-8') as f:
    w = csv.DictWriter(f,['img','url', 'discription'])
    w.writeheader()
    for device in devicelist:
        w.writerow(device)

driver.close()
