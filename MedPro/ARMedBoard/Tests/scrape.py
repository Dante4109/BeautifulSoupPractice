from bs4 import BeautifulSoup
import requests

base_url = (
    "http://www.armedicalboard.org/Public/verify/results.aspx?strPHIDNO=ASMB")


def getWebPageFromUrl(base_url):
    webpage = requests.get(base_url + "18409")
    webpage_text = requests.get(base_url + "18409").text
    soup = BeautifulSoup(webpage_text, 'lxml')

    if webpage.status_code == 200:
        print(soup.prettify())


getWebPageFromUrl(base_url)


""" source = requests.get(
    'http://www.armedicalboard.org/Public/verify/results.aspx?strPHIDNO=ASMB18409').text

 """
