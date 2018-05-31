"""parsing with BeautifulSoup"""

import requests
from selenium import webdriver
from bs4 import BeautifulSoup
import re
import time

expedia = 'https://www.expedia.co.uk/Flights-Search?flight-type=on&starDate=24%2F08%2F2018&_xpid=11905%7C1&mode=search&trip=oneway&leg1=from%3ALondon%2C+England%2C+UK+%28LON-All+Airports%29%2Cto%3ABucharest%2C+Romania%2Cdeparture%3A24%2F09%2F2018TANYT&passengers=children%3A0%2Cadults%3A1%2Cseniors%3A0%2Cinfantinlap%3AY'
page = requests.get(expedia)
soup = BeautifulSoup(page.content, "html.parser")

def price():
   
    symbol = []
    prices = soup.find_all(class_= "full-bold no-wrap")
    for price in prices:
        price=price.get_text()
        price = re.sub(price[0], '', price)
        
        if int(price)<100: 
            price = str(price)
            price = '£'+price
            symbol.append(price)
        
    symbol = sorted(set(symbol))
    symbol = str(symbol)[1:-1]
    symbol = re.sub("['']", '', symbol)
    return print("For the specific period of time, available tickets are at {0}.".format(symbol))

price()