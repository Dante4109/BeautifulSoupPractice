from seleniumrequests import Firefox
import requests

webdriver_path = 'F:/Programs/Python/BeautifulSoupPractice/geckodriver/geckodriver.exe'
webdriver = Firefox(webdriver_path)

url = 'https://www.pals.pa.gov/api/Search/SearchForPersonOrFacilty'
data = {"OptPersonFacility": "Person", "ProfessionID": 8, "LicenseTypeId": 383,
        "LicenseNumber": "", "State": "", "Country": "ALL", "IsFacility": 0, "PageNo": 199}
response = webdriver.request('POST', url, data)
print(response)
print(response.text)

""" cookies = driver.get_cookies()
print(cookies) """
