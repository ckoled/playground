url = "https://www.hotels.com/search.do?"

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import os
import time

opts = Options()
opts.binary_location = "/usr/bin/google-chrome"

chrome_driver = "/usr/bin/chromedriver"

driver = webdriver.Chrome(options=opts)
driver.implicitly_wait(10)

# def get_page(output_file):
driver.get(url)

time.sleep(10)

soup = BeautifulSoup(driver.page_source, "lxml")
incidents = soup.find_all("div", class_="incident-item")
# print(incidents)

incident_list = []
for incident in incidents:
    id = incident.get("id")
    title = incident.find("span", id="incident-type").text.strip()
    address = incident.find("span", id="incident-address").text.strip()
    description = incident.find("span", id="incident-description").text.strip()
    date = incident.find("span", id="incident-date").text.strip()
    time = incident.find("span", id="incident-time").text.strip()
    inc = {
    'id': id,
    'title': title,
    'address': address,
    'description': description,
    'date': date,
    'time': time
    }
    incident_list.append(inc)
    print(inc)

driver.quit()

from csv import DictWriter
headers = ['id','title','address','description','date','time']

with open('incidents.csv', 'a', newline='\n') as f_object:
    obj = DictWriter(f_object, fieldnames=headers)
    for i in incident_list:
        obj.writerow(i)
    f_object.close()
