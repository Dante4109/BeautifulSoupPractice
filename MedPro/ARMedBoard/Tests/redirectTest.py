import requests

base_url = 'http://www.armedicalboard.org/Public/verify/lookup.aspx?LicNum=PA-340'

no_match_url = 'http://www.armedicalboard.org/Public/verify/results.aspx?strPHIDNO=No%20Match'


response = requests.get(base_url)
if response.history:
    print("Request was redirected")
    for resp in response.history:
        print(resp.status_code, resp.url)
    print("Final destination:")
    print(response.status_code, response.url)
else:
    print("Request was not redirected")
