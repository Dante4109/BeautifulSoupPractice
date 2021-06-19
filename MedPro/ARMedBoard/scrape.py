from bs4 import BeautifulSoup
import requests

""" print(soup.prettify()) """

base_url = (
    "http://www.armedicalboard.org/Public/verify/results.aspx?strPHIDNO=ASMB")


def getAllUrls(base_url):

    url_List = list()

    webpage = requests.get(base_url + "1")
    webpage_text = requests.get(base_url + "1").text

    soup = BeautifulSoup(webpage_text, 'lxml')


url_List = list()

if webpage.status_code == 200:
    print(soup.prettify())


""" source = requests.get(
    'http://www.armedicalboard.org/Public/verify/results.aspx?strPHIDNO=ASMB18409').text

 """
