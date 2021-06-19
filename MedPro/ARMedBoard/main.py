from urlList import getAllUrlsBasedOnLicenseType
from dataSet import getDataSetFromUrl
from exportCSV import writeExampleCSV, exportDicAsCSV


base_url = (
    "http://www.armedicalboard.org/Public/verify/results.aspx?strPHIDNO=ASMB")

license_type = "PA"
dataSetList = list()

urls = getAllUrlsBasedOnLicenseType(base_url, license_type, 18409, 18412)
print(license_type + " Count: " + str(len(urls)))

for url in urls:
    currentUrl = url
    currentDataSet = getDataSetFromUrl(currentUrl)
    dataSetList.append(currentDataSet.__dict__)

exportDicAsCSV(dataSetList, "ARMedBoard.csv")

""" writeExampleCSV() """
