from requests import get
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

station_id = '280066'
station_name = 'ΓΑΖΙΑΣ'

url = 'http://telematics.oasa.gr/en/#stationInfo_' + station_id + '_' + station_name

# Download latest chromedriver here: -> http://chromedriver.chromium.org/downloads.
# Then add to path.

# Configuring chrome to start headless
options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')

driver = webdriver.Chrome(chrome_options=options)


print()
print('Chromedriver Started')

driver.get(url)

print('Results Fetched')


soup = BeautifulSoup(driver.page_source, 'html.parser')

bus_arrivals = soup.find_all('ul', class_='list-group tArrivals')

bus_names = []
bus_arrivals = []

for cl in soup.find_all('ul', class_='list-group tArrivals'):
    for but in cl.find_all('button'):
        bus_names.append(but.text)
    for time in cl.find_all('span'):
        bus_arrivals.append(time.text)


for counter, bus in enumerate(bus_names):
    print('%s estimated arrival in: %s' % (bus, bus_arrivals[counter]))

