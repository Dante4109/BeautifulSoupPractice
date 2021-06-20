from bs4 import BeautifulSoup
from lxml import etree
import cchardet
from dataSet import getDataFromXpathDom


def getAllUrlsBasedOnLicenseType(base_url, license_type, startRng, endRng, requests_session):
    urls = list()

    totalWebPages = range(startRng, endRng)
    """ urls = [ totalWebPages   ] """

    for index in totalWebPages:
        url = base_url + str(index)
        webpage = requests_session.get(base_url + str(index)).text

        soup = BeautifulSoup(webpage, "lxml")
        dom = etree.HTML(str(soup))
        License = getDataFromXpathDom(
            dom, '//*[@id="ctl00_MainContentPlaceHolder_lvResultsLicInfo_ctrl0_lblLicnumInfo"]')
        print(index)
        print(License)
        """ if(License).startswith(license_type): """
        urls.append(url)

    return urls


"""
Relevant info

Name xpath
//*[@id="ctl00_MainContentPlaceHolder_lvResults_ctrl0_lblPhyname"]

License xpath
//*[@id="ctl00_MainContentPlaceHolder_lvResultsLicInfo_ctrl0_lblLicnumInfo"]

"""
