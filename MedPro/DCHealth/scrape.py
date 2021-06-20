import requests
import json


base_url = (
    "https://doh.force.com/ver/s/sfsites/aura?r=23&other.SearchComponent.searchRemainingRecords=3")

page_number = 1000

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
url_List = list()
requests_session = requests.Session()
response = requests_session.post(
    base_url, payload, headers)
print(response.status_code)
print(response.text)
print(response.json())
