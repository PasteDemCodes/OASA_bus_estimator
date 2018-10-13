from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


started_time = time.time()

# Change these to your liking.
station_id = '280066'
station_name = 'ΓΑΖΙΑΣ'

url = 'http://telematics.oasa.gr/en/#stationInfo_' + station_id + '_' + station_name

# Configuring chrome to start headless
options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')

driver = webdriver.Chrome(chrome_options=options)

print()
print('Bus Station given : %s.' % station_name)
print('Bus Station id    : %s.' % station_id)
print()
print('Searching Initiated')

driver.get(url)

print('Results Fetched')


soup = BeautifulSoup(driver.page_source, 'html.parser')

bus_names = []
bus_arrivals = []

print('Analyzing Data')

for ul in soup.find_all('ul', class_='list-group tArrivals'):
    for button in ul.find_all('button'):
        bus_names.append(button.text)
    for span in ul.find_all('span'):
        bus_arrivals.append(span.text)


finish_time = time.time()
print('Data Analyzed. Time: %ds.' % (finish_time - started_time))


for counter, bus in enumerate(bus_names):
    print('%s estimated arrival in: %s' % (bus, bus_arrivals[counter]))

