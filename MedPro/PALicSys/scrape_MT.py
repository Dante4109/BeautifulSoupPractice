import requests
import json
import concurrent.futures
import time

requests_session = requests.Session()
responseList = []

start = time.perf_counter()


def getPageData(page_number):
    base_url = (
        "https://www.pals.pa.gov/api/Search/SearchForPersonOrFacilty")

    data = {"OptPersonFacility": "Person", "ProfessionID": 8, "LicenseTypeId": 383, "LicenseNumber": "",
            "State": "", "Country": "ALL", "IsFacility": 0, "PageNo": page_number}

    response = requests_session.post(
        base_url, data)
    """ print(response.status_code)
    print(response.json()) """
    print("Page Number: " + str(page_number))
    return response.json()


# context manager

# Note this api is much slower than DCHealth
# Reponse time is 1.3s per request
with concurrent.futures.ThreadPoolExecutor(max_workers=200) as executor:
    pages = range(0, 200)
    results = executor.map(getPageData, pages)

    for r in results:
        responseList.append(r)

requests_session.close()
finish = time.perf_counter()
print(responseList)
print("Total number of pages obtained: " + str(len(responseList)))
print(f'Finished in {round(finish-start, 2)} second(s)')

# Total results returned 9942

""" maxworkers=30
Total number of pages obtained: 50
Finished in 16.74 second(s) """

""" maxworkers=50
Total number of pages obtained: 50
Finished in 16.17 second(s) """

""" maxworkers=100
Total number of pages obtained: 50
Finished in 10.55 second(s) """

""" maxworkers=100
Total number of pages obtained: 100
Finished in 22.55 second(s) """

""" maxworkers=200
Total number of pages obtained: 200
Finished in 51.53 second(s) """
