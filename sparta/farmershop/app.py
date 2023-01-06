from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.8vasl6v.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import datetime

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/today_price')
def today_price():
    daily_price = list(db.daily_price.find({}, {'_id': False}))
    print(datetime.datetime.now().strftime('%Y/%m/%d'))
    print(daily_price)
    if len(daily_price) != 0 and daily_price[0]['date'] == datetime.datetime.now().strftime('%Y/%m/%d'):
        return jsonify({'daily_price': daily_price})
    else:
        options = webdriver.ChromeOptions()
        options.add_argument("headless")

        id = "sjasjaruddus@naver.com"
        pwd = "1q2w3e4r!"

        driver = webdriver.Chrome('./chromedriver.exe', chrome_options=options)
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
            xpath = '//*[@id="tbodyItemList"]/tr[' + a + ']/td[2]/div/em'
            num = transform(i - 1)
            price_list[num] = round(float(driver.find_element(By.XPATH, xpath).text))

        elem = driver.find_element(By.XPATH,
                                   '//*[@id="lostark-wrapper"]/div/main/div/div[1]/div[1]/div[2]/button').click()
        time.sleep(0.5)
        elem = driver.find_element(By.XPATH, '//*[@id="expand-character-list"]/ul[1]/li[3]/span/button').click()
        time.sleep(0.5)
        elem = driver.find_element(By.XPATH, '//*[@id="modal-info"]/div/div/div[2]/button').click()
        time.sleep(0.5)
        elem = driver.find_element(By.XPATH, '//*[@id="itemList"]/thead/tr/th[1]/a').click()
        time.sleep(0.5)

        for i in range(1, 5):
            a = str(i)
            xpath = '//*[@id="tbodyItemList"]/tr[' + a + ']/td[2]/div/em'
            num = transform(i + 8)
            price_list[num] = round(float(driver.find_element(By.XPATH, xpath).text))

        elem = driver.find_element(By.XPATH,
                                   '//*[@id="lostark-wrapper"]/div/main/div/div[1]/div[1]/div[2]/button').click()
        time.sleep(0.5)
        elem = driver.find_element(By.XPATH, '//*[@id="expand-character-list"]/ul[1]/li[1]/span/button').click()
        driver.close()

        doc = {}
        for i in range(0, 13):
            a = str(i)
            doc[a] = price_list[i]

        doc['date'] = datetime.datetime.now().strftime('%Y/%m/%d')

        db.daily_price.insert_one(doc)
        daily_price = list(db.daily_price.find({}, {'_id': False}))

        return jsonify({'daily_price' : daily_price})

@app.route("/save_user", methods=["POST"])
def save_user():
    data_receive = request.form.getlist('data_give[]')
    user = db.user_data.find_one({'0': data_receive[0]})
    msg = '영지 정보 저장 완료'

    if user is not None:
        db.user_data.delete_one({'0': data_receive[0]})
        msg = '영지 정보 수정 완료'

    doc = {
        '0': data_receive[0],
        '1': data_receive[1],
        '2': data_receive[2],
        '3': data_receive[3],
        '4': data_receive[4]
    }

    db.user_data.insert_one(doc)
    return jsonify({'msg': msg})


@app.route("/load_user", methods=["POST"])
def load_user():
    data_receive = request.form['data_give']
    user_data = list(db.user_data.find({'0': data_receive}, {'_id': False}))
    print(user_data)
    if len(user_data) == 1:
        return jsonify({'user_data': user_data})
    else:
        return jsonify({'user_data': '해당 닉네임으로 저장된 영지 정보가 없습니다.'})


@app.route("/crawling", methods=["GET"])
def crawling():
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

    price_list = [0] * 9
    for i in range(1, 10):
        a = str(i)
        xpath = '//*[@id="tbodyItemList"]/tr[' + a + ']/td[4]/div/em'
        print(xpath)
        num = transform(i - 1)
        price_list[num] = round(float(driver.find_element(By.XPATH, xpath).text))

    return jsonify({'price_list': price_list})
    # if datetime.datetime.now().strftime('%Y/%m/%d') == price['date']:
    #     return jsonify({'price': price})
    # else:
    #     options = webdriver.ChromeOptions()
    #     options.add_argument("headless")
    #
    #     id = "sjasjaruddus@naver.com"
    #     pwd = "1q2w3e4r!"
    #
    #     driver = webdriver.Chrome('./chromedriver.exe', options=options)
    #     driver.get("https://lostark.game.onstove.com/Market")
    #
    #     time.sleep(2)
    #     elem = driver.find_element(By.XPATH, '//*[@id="user_id"]')
    #     elem.send_keys(id)
    #     elem = driver.find_element(By.XPATH, '//*[@id="user_pwd"]')
    #     elem.send_keys(pwd)
    #     elem.send_keys(Keys.RETURN)
    #     time.sleep(2)
    #     elem = driver.find_element(By.XPATH, '//*[@id="lostark-wrapper"]/div/main/div/div[2]/a[2]').click()
    #     time.sleep(2)
    #     elem = driver.find_element(By.XPATH, '// *[ @ id = "itemList"] / thead / tr / th[1] / a').click()
    #     time.sleep(2)
    #
    #     price_list = []
    #     for i in range(0, 8) :
    #         xpath = '//*[@id="tbodyItemList"]/tr[' + i + ']/td[4]/div/em'
    #         price_list[i] = round(float(driver.find_element(By.XPATH, xpath).text))
    #
    #     return jsonify({'price_list': price_list})
    # white_relic = round(float(driver.find_element(By.XPATH, '//*[@id="tbodyItemList"]/tr[1]/td[2]/div/em').text))
    # white_fish = round(float(driver.find_element(By.XPATH, '//*[@id="tbodyItemList"]/tr[2]/td[2]/div/em').text))
    # white_meat = round(
    #     float(driver.find_element(By.XPATH, '//*[@id="tbodyItemList"]/tr[3]/td[2]/div/em').text))
    # green_meat = round(float(driver.find_element(By.XPATH, '//*[@id="tbodyItemList"]/tr[4]/td[2]/div/em').text))
    # green_fish = round(float(driver.find_element(By.XPATH, '//*[@id="tbodyItemList"]/tr[5]/td[2]/div/em').text))
    # green_relic = round(float(driver.find_element(By.XPATH, '//*[@id="tbodyItemList"]/tr[6]/td[2]/div/em').text))
    # blue_relic = round(float(driver.find_element(By.XPATH, '//*[@id="tbodyItemList"]/tr[7]/td[2]/div/em').text))
    # blue_fish = round(float(driver.find_element(By.XPATH, '//*[@id="tbodyItemList"]/tr[8]/td[2]/div/em').text))
    # blue_meat = round(
    #     float(driver.find_element(By.XPATH, '//*[@id="tbodyItemList"]/tr[9]/td[2]/div/em').text))

    # print(datetime.datetime.now().strftime('%Y/%m/%d'))
    # doc = {
    #     'date': datetime.datetime.now().strftime('%Y/%m/%d'),
    #     'white_relic': white_relic,
    #     'white_fish': white_fish,
    #     'white_meat': white_meat,
    #     'green_meat': green_meat,
    #     'green_fish': green_fish,
    #     'green_relic': green_relic,
    #     'blue_relic': blue_relic,
    #     'blue_fish': blue_fish,
    #     'blue_meat': blue_meat
    # }
    # db.lostark.insert_one(doc)
    #
    # all_price = list(db.lostark.find({}, {'_id': False}))
    # price = all_price[len(all_price) - 1]
    #
    # return jsonify({'price': price})
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
    if num == 9:
        return 11
    if num == 10:
        return 12
    if num == 11:
        return 10
    if num == 12:
        return 9

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)

def daily_crawling():
    options = webdriver.ChromeOptions()
    options.add_argument("headless")

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
        xpath = '//*[@id="tbodyItemList"]/tr[' + a + ']/td[2]/div/em'
        num = transform(i - 1)
        price_list[num] = round(float(driver.find_element(By.XPATH, xpath).text))

    elem = driver.find_element(By.XPATH,
                               '//*[@id="lostark-wrapper"]/div/main/div/div[1]/div[1]/div[2]/button').click()
    time.sleep(0.5)
    elem = driver.find_element(By.XPATH, '//*[@id="expand-character-list"]/ul[1]/li[3]/span/button').click()
    time.sleep(0.5)
    elem = driver.find_element(By.XPATH, '//*[@id="modal-info"]/div/div/div[2]/button').click()
    time.sleep(0.5)
    elem = driver.find_element(By.XPATH, '//*[@id="itemList"]/thead/tr/th[1]/a').click()
    time.sleep(0.5)

    for i in range(1, 5):
        a = str(i)
        xpath = '//*[@id="tbodyItemList"]/tr[' + a + ']/td[2]/div/em'
        num = transform(i + 8)
        price_list[num] = round(float(driver.find_element(By.XPATH, xpath).text))

    elem = driver.find_element(By.XPATH,
                               '//*[@id="lostark-wrapper"]/div/main/div/div[1]/div[1]/div[2]/button').click()
    time.sleep(0.5)
    elem = driver.find_element(By.XPATH, '//*[@id="expand-character-list"]/ul[1]/li[1]/span/button').click()
    driver.close()

    doc = {}
    for i in range(0, 13):
        a = str(i)
        doc[a] = price_list[i]

    doc['date'] = datetime.datetime.now().strftime('%Y/%m/%d')

    db.daily_price.delete_many({})
    db.daily_price.insert_one(doc)