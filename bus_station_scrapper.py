from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import requests

started_time = time.time()

url = 'http://telematics.oasa.gr/en/'

# Configuring chrome to start headless
options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')

driver = webdriver.Chrome(chrome_options=options)

print()
print('Searching Initiated')

driver.get(url)

print('Results Fetched')

soup = BeautifulSoup(driver.page_source, 'html.parser')

form_options = []

print('Analyzing Data')

for select in soup.find_all('div', class_='form-group'):
    for option in select.find_all('option'):
        try:
            form_options.append(option['value'])
        finally:
            print('Finished Grabbing Form Options. Time: %d.' % (time.time() - started_time))



print(form_options)