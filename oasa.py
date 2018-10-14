from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


class Estimator:

    started_time = time.time()
    station_id = None
    station_name = None
    url = None

    def __init__(self, station_id, station_name):
        self.station_id = station_id
        self.station_name = station_name
        self.url = 'http://telematics.oasa.gr/en/#stationInfo_' + station_id + '_' + station_name


    def __str__(self):

        return ('\nEstimator Info\n' +
                ('Bus Station given: %s.\n' % self.station_name) +
                ('Bus Station id   : %s.\n' % self.station_id) +
                ('Station URL      : %s\n' % self.url))


    def run(self):

        # Using selenium because i need javascript to load before grabbing html.
        # Configuring chrome to start headless
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')

        driver = webdriver.Chrome(chrome_options=options)
        driver.get(self.url)

        soup = BeautifulSoup(driver.page_source, 'html.parser')

        '''
        Example of Data am looking for
        
        <ul class="list-group"><li class="list-group-item routeElementToCl" id="troute_863" ml="152">
        <button class="btn btn-info btn-circle" type="button">814</button> SCHISTO KARAVAS - PEIRAIAS </li>
        <li class="list-group-item routeElementToCl" id="troute_888" ml="151">
        <button class="btn btn-info btn-circle" type="button">806</button> KORYDALLOS - ST. METRO AIGALEO </li>
        <li class="list-group-item routeElementToCl" id="troute_861" ml="151">
        <button class="btn btn-info btn-circle" type="button">807</button> ANO KORYDALLOS - ST. METRO AIGALEO </li>
        </ul></div></div></div><div class="col-lg-6"><div class="panel panel-info"><div class="panel-heading">
        <h3 class="panel-title">Bus Arrivals At Stop</h3></div><div class="panel-body">
        <div class="alert alert-danger" id="arrWarning" style="display:none;"></div><ul class="list-group tArrivals">
        <li class="list-group-item arrivalContainer" id="route_1870" style="display:none;"><div class="row">
        <div class="col-lg-2"><button class="btn btn-lg btn-info btn-circle arrivalNumBtn" type="button">814</button>
        </div><div class="col-lg-10"><div>SCHISTO KARAVAS - PEIRAIAS : SCHISTO KARAVAS - PEIRAIAS</div><b>Arrival in
        <span class="arrivalsAr"></span></b></div></div></li>
        <li class="list-group-item arrivalContainer" id="route_1902" style="display: block;"><div class="row">
        <div class="col-lg-2"><button class="btn btn-lg btn-info btn-circle arrivalNumBtn" type="button">806</button></div>
        <div class="col-lg-10"><div>KORYDALLOS - ST. METRO AIGALEO  : KORYDALLOS - ST. METRO AIGALEO </div>
        <b>Arrival in <span class="arrivalsAr">26'</span></b></div></div></li>
        <li class="list-group-item arrivalContainer" id="route_1903" style="display:none;">
        <div class="row"><div class="col-lg-2">
        <button class="btn btn-lg btn-info btn-circle arrivalNumBtn" type="button">807</button></div><div class="col-lg-10">
        <div>ANO KORYDALLOS - ST. METRO AIGALEO : ANO KORYDALLOS - ST. METRO AIGALEO</div><b>Arrival in <span class="arrivalsAr">
        </span></b></div></div></li></ul>
        '''

        bus_names = []
        bus_arrivals = []

        for ul in soup.find_all('ul', class_='list-group tArrivals'):
            for button in ul.find_all('button'):
                bus_names.append(button.text)
            for span in ul.find_all('span'):
                bus_arrivals.append(span.text)

        print('Data Analyzed. Time    : %ds.' % (time.time() - self.started_time))

        for counter, bus in enumerate(bus_names):
            print('%s estimated arrival in: %s' % (bus, bus_arrivals[counter]))


# Example of usage
# You can find id, name by manually browsing http://telematics.oasa.gr/en
# Once you find them, replace them below.

estimator = Estimator(station_id='280066', station_name='ΓΑΖΙΑΣ')
print(estimator)
estimator.run()
