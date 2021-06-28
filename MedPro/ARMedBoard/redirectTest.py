import requests

url = 'http://www.armedicalboard.org/Public/verify/lookup.aspx?LicNum=PA-2000'

response = requests.get(url)
if response.history:
    print("Request was redirected")
    for resp in response.history:
        print(resp.status_code, resp.url)
    print("Final destination:")
    print(response.status_code, response.url)
else:
    print("Request was not redirected")
