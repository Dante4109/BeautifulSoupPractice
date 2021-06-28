from bs4 import BeautifulSoup
from lxml import etree
import requests
import csv

url = "https://en.wikipedia.org/wiki/List_of_Marvel_Cinematic_Universe_films"

webpage = requests.get(url)

soup = BeautifulSoup(webpage.content, "html.parser")

dom = etree.HTML(str(soup))

elements = (
    dom.xpath('//*[@id="mw-content-text"]/div[1]/table[2]/tbody/tr[*]/th/i/a'))


'''ironman:'''
'//*[@id = "mw-content-text"]/div[1]/table[2]/tbody/tr[4]/th/i/a'

print(elements[0].text)

for element in elements:
    print(element.text)
    print("---------------------")

base_url = "https: // en.wikipedia.org"

links = [base_url + element.attrib['href'] for element in elements]

for link in links:
    print(link)
    print("---------------------")
