from requests import get
from bs4 import BeautifulSoup
from selenium import webdriver


station_id = '280066'
station_name = 'ΓΑΖΙΑΣ'

url = 'http://telematics.oasa.gr/en/#stationInfo_' + station_id + '_' + station_name

# Download latest chromedriver here: -> http://chromedriver.chromium.org/downloads.
# Then add to path.
driver = webdriver.Chrome()
driver.get(url)

session = get(url)

soup = BeautifulSoup(driver.page_source, 'html.parser')

bus_arrivals = soup.find_all('ul', class_ = 'list-group tArrivals')

for bus in bus_arrivals:
    print(bus)