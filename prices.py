from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from time import sleep
import re
import random

username = 'your_name@email.com'  # Your username here
password = 'your_password'  # Your password here

# Initialise browser and specify login details
browser = webdriver.Firefox()

# Open Trading212 and login
browser.get('https://live.trading212.com/')
username_field = browser.find_element_by_name("login[username]")
username_field.send_keys(username)
username_field = browser.find_element_by_name("login[password]")
username_field.send_keys(password)
login_button = browser.find_element_by_class_name("button-login")
login_button.click()

# Define explicit wait. We use explicit wait for when the "item-xxxxxxx" (stock holdings) have loaded as they load
# after the rest of the page. If we used implicit wait, we would get the page source WITHOUT the positions table HTML.
# Use starts-with Xpath function because the stock positions all have id's that start with "item-" (see page source).
element_present = EC.presence_of_element_located((By.XPATH, '//*[starts-with(@id,"item-")]'))
WebDriverWait(browser, 20).until(element_present)

# Get page HTML source
source = browser.page_source

# Find regex, for any stock
stock_regex = re.compile(r'class="name">.+</td><td data-column-id="created"')
'<div class="instrument-name" data-dojo-attach-point="instrumentNameNode">Sonos, Inc.</div>'
holdings = stock_regex.findall(source)

# Extract name of stock from html
stocks = []
for holding in holdings:
    stock = holding.replace('class="name">', '').replace('</td><td data-column-id="created"', '')
    # Correct leveraged stocks, e.g. 2x Apple
    if stock.startswith(('2x', '3x')):
        stock = stock[3:]
    elif stock.startswith(('-1x', '-2x')):
        stock = stock[4:]
    print(stock)
    stocks.append(stock)

# Google search each stock
for stock in reversed(stocks):
    browser.execute_script(f"window.open('https://www.google.com/search?q={stock + ' stock price'}','_blank')")
    secs = random.uniform(1, 2.5)
    sleep(secs)