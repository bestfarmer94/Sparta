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

driver = webdriver.Chrome('./chromedriver.exe', options=options)
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
green_fish = math.ceil(float(driver.find_element(By.XPATH, '//*[@id="tbodyItemList"]/tr[1]/td[2]/div/em').text))
green_meat = math.ceil(float(driver.find_element(By.XPATH, '//*[@id="tbodyItemList"]/tr[2]/td[2]/div/em').text))
green_relic = math.ceil(float(driver.find_element(By.XPATH, '//*[@id="tbodyItemList"]/tr[3]/td[2]/div/em').text))
blue_fish = math.ceil(float(driver.find_element(By.XPATH, '//*[@id="tbodyItemList"]/tr[4]/td[2]/div/em').text))
blue_meat = math.ceil(float(driver.find_element(By.XPATH, '//*[@id="tbodyItemList"]/tr[5]/td[2]/div/em').text))
blue_relic = math.ceil(float(driver.find_element(By.XPATH, '//*[@id="tbodyItemList"]/tr[6]/td[2]/div/em').text))
white_fish = math.ceil(float(driver.find_element(By.XPATH, '//*[@id="tbodyItemList"]/tr[7]/td[2]/div/em').text))
white_meat = math.ceil(float(driver.find_element(By.XPATH, '//*[@id="tbodyItemList"]/tr[8]/td[2]/div/em').text))
white_relic = math.ceil(float(driver.find_element(By.XPATH, '//*[@id="tbodyItemList"]/tr[9]/td[2]/div/em').text))

datetime.datetime.now().strftime('%Y/%m/%d')
print(datetime.datetime.now().strftime('%Y/%m/%d'))
doc = {
	'date': datetime.datetime.now().strftime('%Y/%m/%d'),
	'green_fish': green_fish,
	'green_meat': green_meat,
	'green_relic': green_relic,
	'blue_fish': blue_fish,
	'blue_meat': blue_meat,
	'blue_relic': blue_relic,
	'white_fish': white_fish,
	'white_meat': white_meat,
	'white_relic': white_relic
}
db.lostark.insert_one(doc)
print('success')
# print(elem)
# assert "Python" in driver.title
# elem = driver.find_element(By.NAME, "q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source

driver.close()