from bs4 import BeautifulSoup
import requests
import json


base_url = (
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
