from pymongo import MongoClient

client = MongoClient('mongodb+srv://test:sparta@cluster0.8vasl6v.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta

from selenium import webdriver
import time
import schedule
import datetime
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

id = "sjasjaruddus@naver.com"
pwd = "1q2w3e4r!"

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

price_list = [0] * 13
for i in range(1, 10):
    a = str(i)
    xpath = '//*[@id="tbodyItemList"]/tr[' + a + ']/td[4]/div/em'
    # num = transform(i - 1)
    price_list[i] = round(float(driver.find_element(By.XPATH, xpath).text))

elem = driver.find_element(By.XPATH, '//*[@id="lostark-wrapper"]/div/main/div/div[1]/div[1]/div[2]/button').click()
time.sleep(0.5)
elem = driver.find_element(By.XPATH, '//*[@id="expand-character-list"]/ul[1]/li[3]/span/button').click()
time.sleep(0.5)
elem = driver.find_element(By.XPATH, '//*[@id="modal-info"]/div/div/div[2]/button').click()
time.sleep(0.5)
elem = driver.find_element(By.XPATH, '//*[@id="itemList"]/thead/tr/th[1]/a').click()
time.sleep(0.5)

for i in range(10, 13):
    a = str(i-9)
    xpath = '//*[@id="tbodyItemList"]/tr[' + a + ']/td[2]/div/em'
    price_list[i] = round(float(driver.find_element(By.XPATH, xpath).text))

doc = {'date': datetime.datetime.now().strftime('%Y/%m/%d')}
for i in range(0, 13):
    a = str(i)
    doc[a] = price_list[i]

daily_price = list(db.daily_price.find({}, {'_id': False}))

db.daily_price.delete_many({})
db.daily_price.insert_one(doc)

def transform(num):
    if num == 0:
        return 0
    if num == 1:
        return 3
    if num == 2:
        return 6
    if num == 3:
        return 7
    if num == 4:
        return 4
    if num == 5:
        return 1
    if num == 6:
        return 2
    if num == 7:
        return 5
    if num == 8:
        return 8