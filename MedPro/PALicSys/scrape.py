import requests
import json


base_url = (
    "https://www.pals.pa.gov/api/Search/SearchForPersonOrFacilty")
page_number = 199
data = {"OptPersonFacility": "Person", "ProfessionID": 8, "LicenseTypeId": 383, "LicenseNumber": "",
        "State": "", "Country": "ALL", "IsFacility": 0, "PageNo": page_number}
url_List = list()
requests_session = requests.Session()
response = requests_session.post(
    base_url, data)
print(response.status_code)
print(response.json())
