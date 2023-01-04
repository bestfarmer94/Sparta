import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://loa.icepeng.com/refining', headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.8vasl6v.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta

# print(soup)
#craftTable > div.v-data-table__wrapper > table > tbody > tr:nth-child(1) > td:nth-child(3) > span
#tbodyItemList > tr:nth-child(5) > td:nth-child(1) > div > span.name
#tbodyItemList > tr:nth-child(5) > td:nth-child(2) > div > em
#tbodyItemList > tr:nth-child(4) > td:nth-child(2) > div > em
#mat-input-4
#mat-input-3
#chartdiv > div > div:nth-child(1) > div > canvas:nth-child(2)
items = soup.select('#mat-input')
print(items)
for item in items:
    rank = item.select_one('td.item-transaction.text-right').text
    print(rank)
    title = item.select_one('td.info > a.title.ellipsis').text
    if len(title) > 100:    #19금 마크 없애기
        title = title[5:len(title)]
    title = title.strip()

