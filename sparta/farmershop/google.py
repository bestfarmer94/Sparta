from selenium import webdriver
import time
import datetime
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import math

from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.8vasl6v.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta

options = webdriver.ChromeOptions()
options.add_argument("headless")

id = "sjasjaruddus@naver.com"
pwd = "1q2w3e4r!"

driver = webdriver.Chrome()
driver.get("https://lostark.game.onstove.com/Market")

time.sleep(2)
elem = driver.find_element(By.XPATH, '//*[@id="user_id"]')
elem.send_keys(id)
elem = driver.find_element(By.XPATH, '//*[@id="user_pwd"]')
elem.send_keys(pwd)
elem.send_keys(Keys.RETURN)
time.sleep(2)
elem = driver.find_element(By.XPATH, '//*[@id="lostark-wrapper"]/div/main/div/div[2]/a[2]').click()
time.sleep(2)
elem = driver.find_element(By.XPATH, '// *[ @ id = "itemList"] / thead / tr / th[1] / a').click()
time.sleep(2)

price_list = []
for i in range(1, 10):
	a = str(i)
	xpath = '//*[@id="tbodyItemList"]/tr[' + a + ']/td[4]/div/em'
	print(xpath)
	price_list.append(round(float(driver.find_element(By.XPATH, xpath).text)))

print(price_list)
print('success')
# print(elem)
# assert "Python" in driver.title
# elem = driver.find_element(By.NAME, "q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source

driver.close()