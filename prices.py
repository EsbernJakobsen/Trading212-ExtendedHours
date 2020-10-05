from selenium import webdriver
from time import sleep
import re
import random

username = 'your_username'  # Your username here
password = 'your_password'  # Your username here

# Initialise browser and specify login details
browser = webdriver.Firefox()
browser.implicitly_wait(10)

# Open Trading212 and login
browser.get('https://live.trading212.com/')
username_field = browser.find_element_by_name("login[username]")
username_field.send_keys(username)
username_field = browser.find_element_by_name("login[password]")
username_field.send_keys(password)
login_button = browser.find_element_by_class_name("button-login")
login_button.click()
sleep(13)  # wait for page to load html

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
    print(stock)
    stocks.append(stock)

# Google search each stock
for stock in stocks:
    browser.execute_script(f"window.open('https://www.google.com/search?q={stock + ' stock price'}','_blank')")
    secs = random.uniform(1, 2.5)
    sleep(secs)