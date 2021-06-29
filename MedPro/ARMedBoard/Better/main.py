from urlList_MTBatch import getAllUrlsBasedOnLicenseType
from dataSet import getDataSetFromUrl
from exportCSV import exportDicAsCSV
import time
import requests


tic = time.perf_counter()

license_type = "PA"
dataSetList = list()
requests_session = requests.Session()
# Get list of usable urls
urls = getAllUrlsBasedOnLicenseType()
toc = time.perf_counter()

print(f"Grabbed {len(urls)} urls in {toc - tic:0.4f} seconds")
print("License Count: " + str(len(urls)))

# Scrape data from usable urls
for url in urls:
    currentUrl = url['URL']
    currentDataSet = getDataSetFromUrl(currentUrl, requests_session)
    dataSetList.append(currentDataSet.__dict__)

exportDicAsCSV(dataSetList, "ARMedBoard.csv")
