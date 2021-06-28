from seleniumOR import getLicenseDataFromOR
import time

start = time.perf_counter()
dataSetList = getLicenseDataFromOR()
print("We are in Main again")
print(dataSetList)
for data in dataSetList:
    print(data)
    print("-------------")

finish = time.perf_counter()
print(f'Finished in {round(finish-start, 2)}'
