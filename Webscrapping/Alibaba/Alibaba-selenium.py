from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import csv

url = "https://www.alibaba.com/trade/search?SearchText=Auto+Accessories"

cService = webdriver.ChromeService(executable_path='D:\\Work\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe')
driver = webdriver.Chrome(service=cService)

try:
    driver.get(url)

    productList=[]
    productDiv = driver.find_elements(By.XPATH, "//div[contains(@class, 'fy26-product-card-wrapper')]" )
    for p in range(len(productDiv)):   
        product = {}
        innerImg = productDiv[p].find_element(By.TAG_NAME, "img")
        innera = productDiv[p].find_element(By.TAG_NAME, "a")
        innerTitle = productDiv[p].find_element(By.XPATH, ".//*[contains(@class, 'searchx-product-e-title')]")
        innerPrice = productDiv[p].find_element(By.XPATH, ".//*[contains(@class, 'searchx-product-price-price-main')]")
        product['img'] = innerImg.get_attribute('src')
        product['discription'] = innerTitle.text
        product['url'] = innera.get_attribute('href')
        product['price'] = innerPrice.text
        productList.append(product)

    filename = 'D:\\Work\\Github\\My-AI-Course-Bin\\Webscrapping\\Alibaba\\productsData-Selenium.csv'
    with open(filename, 'w', newline='',encoding='utf-8') as f:
        w = csv.DictWriter(f,['img','url', 'discription', 'price'])
        w.writeheader()
        for product in productList:
            w.writerow(product)

finally:
    driver.quit()