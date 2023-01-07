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

# driver = webdriver.Chrome('./chromedriver.exe', chrome_options=options)
driver = webdriver.Chrome()
driver.get("https://lostark.game.onstove.com/Market")

elem = driver.find_element(By.XPATH, '//*[@id="user_id"]')
elem.send_keys(id)
elem = driver.find_element(By.XPATH, '//*[@id="user_pwd"]')
elem.send_keys(pwd)
elem.send_keys(Keys.RETURN)
time.sleep(0.5)
elem = driver.find_element(By.XPATH, '//*[@id="lostark-wrapper"]/div/main/div/div[2]/a[2]').click()
time.sleep(0.5)
elem = driver.find_element(By.XPATH, '// *[ @ id = "itemList"] / thead / tr / th[1] / a').click()
time.sleep(0.5)

itemDB = []
for i in range(1, 10):
    a = str(i)
    xpath = '//*[@id="tbodyItemList"]/tr[' + a + ']/td[1]/div/span[1]/img'
    xpath2 = '//*[@id="tbodyItemList"]/tr[' + a + ']/td[2]/div/em'
    elem1 = driver.find_element(By.XPATH, xpath)
    elem2 = driver.find_element(By.XPATH, xpath2)
    itemDB.append({
        'name': elem1.get_attribute('alt'),
        'price': elem2.text,
        'image': elem1.get_attribute('src')
    })

print(itemDB)
# elem = driver.find_element(By.XPATH,
#                            '//*[@id="lostark-wrapper"]/div/main/div/div[1]/div[1]/div[2]/button').click()
# time.sleep(0.5)
# elem = driver.find_element(By.XPATH, '//*[@id="expand-character-list"]/ul[1]/li[3]/span/button').click()
# time.sleep(0.5)
# elem = driver.find_element(By.XPATH, '//*[@id="modal-info"]/div/div/div[2]/button').click()
# time.sleep(0.5)
# elem = driver.find_element(By.XPATH, '//*[@id="itemList"]/thead/tr/th[1]/a').click()
# time.sleep(0.5)
#
# for i in range(1, 5):
#     a = str(i)
#     xpath = '//*[@id="tbodyItemList"]/tr[' + a + ']/td[2]/div/em'
#     price_list[num] = round(float(driver.find_element(By.XPATH, xpath).text))

# elem = driver.find_element(By.XPATH, '//*[@id="tbodyItemList"]/tr[1]/td[1]/div/span[1]/img').get_attribute('src')
# elem2 = driver.find_element(By.XPATH, '//*[@id="tbodyItemList"]/tr[1]/td[1]/div/span[1]/img').get_attribute('alt')
# elem3 = driver.find_element(By.XPATH, '//*[@id="tbodyItemList"]/tr[1]/td[4]/div/em').text
# itemDB = []
# itemDB.append({
#     'name': elem2,
#     'price': elem3,
#     'image': elem
# })
# print(itemDB)
# price_list = []
# for i in range(1, 10):
# 	a = str(i)
# 	xpath = '//*[@id="tbodyItemList"]/tr[' + a + ']/td[4]/div/em'
# 	print(xpath)
# 	price_list.append(round(float(driver.find_element(By.XPATH, xpath).text)))

print('success')
# print(elem)
# assert "Python" in driver.title
# elem = driver.find_element(By.NAME, "q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source

driver.close()
