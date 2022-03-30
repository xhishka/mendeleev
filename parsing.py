from bs4 import BeautifulSoup
import requests
import re

url = 'https://news.mail.ru/coronavirus/stat/region/72/'
resp = requests.get(url)
soup = BeautifulSoup(resp.text, 'lxml')
script = str(soup.find('body').find('div', {"class": "layout"}).find_all('script')[8])
region = str(re.findall(r'"region"(.+)', script))
t1 = re.findall(r'"delta_confirmed":"([^"]+)', region)
print(t1[0])
