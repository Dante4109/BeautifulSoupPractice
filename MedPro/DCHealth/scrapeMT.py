import requests
import json
import concurrent.futures
import time

requests_session = requests.Session()
responseList = []

start = time.perf_counter()


def getPageData(page_number):
    base_url = (
        "https://doh.force.com/ver/s/sfsites/aura?r=23&other.SearchComponent.searchRemainingRecords=3")

    aura_context = json.dumps({
        "mode": "PROD",
        "fwuid": "AE898lCB2KpCUerBipCwXg",
        "app": "siteforce:communityApp",
        "loaded": {
            "APPLICATION@markup://siteforce:communityApp": "sVZ6cnpPX79_SIZb4Z-5KQ"
        },
        "dn": [],
        "globals": {},
        "uad": "false"
    })

    message = json.dumps({
        "actions": [{
            "id": "258;a",
            "descriptor": "apex://SearchComponentController/ACTION$searchRemainingRecords",
            "callingDescriptor": "markup://c:PageCount",
            "params": {
                "Profession": "0",
                "LicenseType": "PHYSICAL THERAPIST",
                "FirstName": "",
                "LastName": "",
                "LicenseNumber": "",
                "SSN": "",
                "Status": "0",
                "offsetCnt": page_number
            },
            "version": "null"
        }]}
    )

    payload = {
        "aura.context": aura_context,
        "aura.token": "undefined",
        "message": message
    }

    headers = {'Content-type': 'application/json; charset=utf-8'}

    response = requests_session.post(
        base_url, payload, headers)

    """ print(response.status_code)
    print(response.text)
    print("Page Number: " + str(page_number))
    print(response.json()) """
    return response.json()


# context manager
with concurrent.futures.ThreadPoolExecutor() as executor:
    pages = range(0, 201)
    results = executor.map(getPageData, pages)

    for r in results:
        responseList.append(r)

requests_session.close()
finish = time.perf_counter()
print(responseList)
print("Total number of pages obtained: " + str(len(responseList)))
print(f'Finished in {round(finish-start, 2)} second(s)')
