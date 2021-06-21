from seleniumOR import getLicenseDataFromOR

dataSetList = getLicenseDataFromOR()
print("We are in Main again")
print(dataSetList)
for data in dataSetList:
    print(data)
    print("-------------")
