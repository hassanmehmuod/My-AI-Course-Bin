from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import csv


url = "https://www.daraz.pk/catalog/?spm=a2a0e.tm80331704.cate_5.5.77cc5aa7fPImi7&q=Smart%20Phones&from=hp_categories&src=all_channel"

cService = webdriver.ChromeService(executable_path='D:\\Work\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe')
driver = webdriver.Chrome(service=cService)

driver.get(url)

smartphoneList=[]
smartphoneDiv= driver.find_elements(By.XPATH, "//div[contains(@class, 'Bm3ON')]" )
for p in range(len(smartphoneDiv)):   
    smartphone = {}
    innerImg = smartphoneDiv[p].find_element(By.TAG_NAME, "img")
    innera = smartphoneDiv[p].find_element(By.TAG_NAME, "a")
    smartphone['img'] = innerImg.get_attribute('src')
    smartphone['discription'] = innerImg.get_attribute('alt')
    smartphone['url'] = innera.get_attribute('href')
    smartphoneList.append(smartphone)

filename = 'D:\\Work\\Github\\My-AI-Course-Bin\\Webscrapping\\Daraz\\smart-phonesData-Selenium.csv'
with open(filename, 'w', newline='',encoding='utf-8') as f:
    w = csv.DictWriter(f,['img','url', 'discription'])
    w.writeheader()
    for smartphone in smartphoneList:
        w.writerow(smartphone)

driver.close()