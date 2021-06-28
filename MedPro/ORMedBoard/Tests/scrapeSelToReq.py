from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import requests
import json


webdriver_path = 'F:/Programs/Python/BeautifulSoupPractice/chromedriver_win32/chromedriver.exe'
driver = webdriver.Chrome(webdriver_path)
web_url = 'https://techmedweb.omb.state.or.us/search'

post_url = 'https://techmedweb.omb.state.or.us/api/licensee-search'
data = {"distance": "5", "nameMatch": "Exact", "address": "All", "pagenumber": 1, "token": "03AGdBq24aFbrydUeiHxp8pPq4ZRz0rSf070XVmLL_yDfdLVZqhkbVjk4QLzV3hnPDuayhxYGkXsvxqNHrynWbOYEmnQtciW6VFkp6UMvhtER8YwPVEUxvzpAqBWA9M9Dk_CiTU150SrG7yYhqz-CViQp7NrQXmfDz4V7behUfdQSmckioO1aL0WTOrAuru1cCu60RsYzW_QEl64__xi144zyagyz1NwjZsk6H54Y0WgASyEr-l7KjxXbcICEyr502TQAxLcjev-6obfb--mJmDr-4_xZw0f2jLkOJwOl1415DlF08BPJbgzDgdw0k5CiMDT5uLDv0OUyYBxvnNBwgbwsbc4gBY4tAtGVkh-0DnoZ_Ajd2x6jxNWa6Ngo7B57jpMkn-kryDSuYhp9OjyYgSD7Vs23SWNY7rsvZIMPInSxFDJdj0Clib5b1zhYhVzw06D6N7LyhBue2Z8L85lHn-3Pw9AOcxmV4q11PjAFaLfSwTx9OGjCfxThPapHbXrfwJLcGGuCEo4W2OOFMTQ8Rq2XwmPbCn5zx5w", "license": "Podiatrist"}
driver.get(web_url)
cookies = driver.get_cookies()
print(cookies)
agent = driver.execute_script("return navigator.userAgent")
origin = driver.execute_script("return navigator.origin")
print(agent)
print(origin)


""" base_url = (
    "https://techmedweb.omb.state.or.us/api/licensee-search")
page_number = 199
data = {
    "distance": "5",
    "nameMatch": "Exact",
    "address": "All",
    "license": "Podiatrist",
    "pagenumber": 1,
    "token": "03AGdBq249qX-XUhA3VJckI6uXQ8edz3JH_N8Q5WyHZllmvDOIMQEuyyBnRA8OAftCPkyEVSNYpblC6-knyCMzN1tU989qSb732CuxEk2dDQf_iNlsSP-Z_nIn5GNQdQy-umMIaNSwuXk2KCKDjiM1QRf4Mj92X3trWyxC0iSUwjC4_4zkEHIMIEnZMGrAt6SJCQOQPWgCzzVxFQiQZwL3Wxf35cR372YHGqrDPZYOMVRJImkviShBKPWQwQ4IWksVh3xpuNcp2pI5HJuOhisgS9Tk66g2j_6X3-NmhW779nnFMXcGZrOyfI-f99-HMKySpKxkQtQ1MJxOmoo_OQKODDZmU7otLmWJFSlAWS63AUVtj2kEmhIeVBAEXwdPlBIncOZlAv_m60XjWQYY4UPDCWkK3A6SJkOcFKaRwX94_X2A45aSWrGSJku1ULHAkutjI1gkWHOXmcnf_U2sqJ2cXz_nZkujQzeBpmTt5U7fywOSFrpWYRvlfOKj_Bn7-w_3Zlq2biGF8VZJG1Zer90BdkkA6s8HHCxdBR2U3gpiysTzQa2BpfEYfAA"
}
url_List = list()
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36"
}
requests_session = requests.Session()
response = requests_session.post(
    base_url, data, headers)
print(response.headers)
print(response.status_code)
print(response.json())
 """
