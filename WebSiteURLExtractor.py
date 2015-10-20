# __author__ = vkremez

from bs4 import BeautifulSoup
import requests

m_url = raw_input("Enter a website to extract the URL's from: ")
r_url = requests.get("http://" +url)

data = r.text
soup = BeautifulSoup(data)

for link in soup.find_all('a'):
    print(link.get('href'))
