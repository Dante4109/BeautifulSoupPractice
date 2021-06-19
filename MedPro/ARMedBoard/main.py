from urlListFast import getAllUrlsBasedOnLicenseType
from dataSetFast import getDataSetFromUrl
from exportCSV import writeExampleCSV, exportDicAsCSV
import requests

base_url = (
    "http://www.armedicalboard.org/Public/verify/results.aspx?strPHIDNO=ASMB")

license_type = "PA"
dataSetList = list()
requests_session = requests.Session()

urls = getAllUrlsBasedOnLicenseType(
    base_url, license_type, 18409, 18450, requests_session)
print(license_type + " Count: " + str(len(urls)))

for url in urls:
    currentUrl = url
    currentDataSet = getDataSetFromUrl(currentUrl, requests_session)
    dataSetList.append(currentDataSet.__dict__)

exportDicAsCSV(dataSetList, "ARMedBoard.csv")

""" writeExampleCSV() """
