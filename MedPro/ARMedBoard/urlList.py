from bs4 import BeautifulSoup
from lxml import etree
import requests


def getAllUrlsBasedOnLicenseType(base_url, license_type, startRng, endRng):
    urls = list()

    totalWebPages = range(startRng, endRng)

    for index in totalWebPages:
        url = base_url + str(index)
        webpage = requests.get(base_url + str(index))
        soup = BeautifulSoup(webpage.content, "html.parser")
        dom = etree.HTML(str(soup))
        License = (
            dom.xpath('//*[@id="ctl00_MainContentPlaceHolder_lvResultsLicInfo_ctrl0_lblLicnumInfo"]'))
        print(index)
        if(License[0]).text.startswith(license_type):
            urls.append(url)

    return urls


"""
Relevant info 

Name xpath
//*[@id="ctl00_MainContentPlaceHolder_lvResults_ctrl0_lblPhyname"]

License xpath
//*[@id="ctl00_MainContentPlaceHolder_lvResultsLicInfo_ctrl0_lblLicnumInfo"]

"""
