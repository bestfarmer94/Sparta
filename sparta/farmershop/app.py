from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.8vasl6v.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta

from selenium import webdriver
import time
import datetime
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import math

from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/crawling", methods=["GET"])
def load_crawling():
    print("실행")
    all_price = list(db.lostark.find({},{'_id':False}))
    price = all_price[len(all_price)-1]
    print(price)
    print(datetime.datetime.now().strftime('%Y/%m/%d') == price['date'])

    if datetime.datetime.now().strftime('%Y/%m/%d') == price['date']:
        return jsonify({'price': price})
    else:
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
        green_relic = math.ceil(
            float(driver.find_element(By.XPATH, '//*[@id="tbodyItemList"]/tr[3]/td[2]/div/em').text))
        blue_fish = math.ceil(float(driver.find_element(By.XPATH, '//*[@id="tbodyItemList"]/tr[4]/td[2]/div/em').text))
        blue_meat = math.ceil(float(driver.find_element(By.XPATH, '//*[@id="tbodyItemList"]/tr[5]/td[2]/div/em').text))
        blue_relic = math.ceil(float(driver.find_element(By.XPATH, '//*[@id="tbodyItemList"]/tr[6]/td[2]/div/em').text))
        white_fish = math.ceil(float(driver.find_element(By.XPATH, '//*[@id="tbodyItemList"]/tr[7]/td[2]/div/em').text))
        white_meat = math.ceil(float(driver.find_element(By.XPATH, '//*[@id="tbodyItemList"]/tr[8]/td[2]/div/em').text))
        white_relic = math.ceil(
            float(driver.find_element(By.XPATH, '//*[@id="tbodyItemList"]/tr[9]/td[2]/div/em').text))

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

        all_price = list(db.lostark.find({}, {'_id': False}))
        price = all_price[len(all_price) - 1]

        return jsonify({'price': price})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)