from urlListFast import main
from dataSetFast import getDataSetFromUrl
from exportCSV import writeExampleCSV, exportDicAsCSV
import time
import requests

base_url = (
    "http://www.armedicalboard.org/Public/verify/results.aspx?strPHIDNO=ASMB")

license_type = "PA"
dataSetList = list()
requests_session = requests.Session()

tic = time.perf_counter()
urls = main(
    base_url, license_type, 18409, 18500, requests_session)
toc = time.perf_counter()
print(f"Grabbed {len(urls)} urls in {toc - tic:0.4f} seconds")
print(license_type + " Count: " + str(len(urls)))

for url in urls:
    currentUrl = url
    currentDataSet = getDataSetFromUrl(currentUrl, requests_session)
    dataSetList.append(currentDataSet.__dict__)

exportDicAsCSV(dataSetList, "ARMedBoard.csv")

""" writeExampleCSV() """
