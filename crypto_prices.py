
import time
import requests
import schedule
from lxml import html
import datetime
import os
def job():
    url = 'https://www.bitprime.co.nz/all-coins/'
    response = ''
    try:
        response = requests.get(url)
    except:
        print 'request failed'
    if response:
        tree = html.fromstring(response.content)
        a = tree.xpath('//*/text()')
        table = []
        for x in range(419,1126):
            if a[x] not in ['Login to Sell','Login to purchase']:
                table.append(a[x])
        dic1 = {}
        row = []
        for x in range(len(table)):
            row.append(table[x])
            if table[x] == '\r\n        ':
                name = row.pop(0)
                row.pop(0)
                row.pop(0)
                row.pop(len(row)-1)
                dic1[name] = row
                row = []
        os.system('cls')
        print "CURRENT PRICE AT "+ datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print ""
        print 'Stellar (XLM)',dic1['Stellar (XLM)']
        print 'Ethereum (ETH)',dic1['Ethereum (ETH)']
        print 'XRP (XRP)',dic1['XRP (XRP)']
        print 'Bitcoin (BTC)',dic1['Bitcoin (BTC)']

schedule.every(5).seconds.do(job)
while True:
    schedule.run_pending()
    time.sleep(1)