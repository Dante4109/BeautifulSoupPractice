from urlList import getAllUrlsBasedOnLicenseType
from dataSet import getDataSetFromUrl
from exportCSV import exportDicAsCSV
import requests

# Set parameters for request
base_url = (
    "http://www.armedicalboard.org/Public/verify/results.aspx?strPHIDNO=ASMB")

license_type = "PA"
dataSetList = list()
requests_session = requests.Session()

# Warning data is obtained sequentially. Range no greate than 100 is recommended.
urls = getAllUrlsBasedOnLicenseType(
    base_url, license_type, 18409, 18415, requests_session)
print(license_type + " Count: " + str(len(urls)))

# Convert matched urls to dataSet class
for url in urls:
    currentUrl = url
    currentDataSet = getDataSetFromUrl(currentUrl, requests_session)
    dataSetList.append(currentDataSet.__dict__)

# Export to CSV File
exportDicAsCSV(dataSetList, "ARMedBoard.csv")
