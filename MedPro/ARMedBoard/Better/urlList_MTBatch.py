from bs4 import BeautifulSoup
from lxml import etree
from dataSet import getDataFromXpathDom
import concurrent.futures
from concurrent.futures import ThreadPoolExecutor, as_completed
import time
import requests

urlList = []
base_url = "http://www.armedicalboard.org/Public/verify/lookup.aspx?LicNum="
no_match_url = 'http://www.armedicalboard.org/Public/verify/results.aspx?strPHIDNO=No%20Match'
requests_session = requests.Session()
license_type = "PA"
startRng = 300
endRng = 400
totalNumSearchs = []
start = time.perf_counter()
ids = [*range(startRng, endRng, 1)]

number_of_chunks = 20
chunk_size = 5


def getAllUrlsBasedOnLicenseType():
    # context manager
    with concurrent.futures.ThreadPoolExecutor(max_workers=number_of_chunks) as executor:
        tasks = []
        for i in range(number_of_chunks):
            chunk = ids[i*chunk_size:(i+1)*chunk_size]
            tasks.append(executor.submit(getUrlFromRedirect, chunk))

    requests_session.close()
    finish = time.perf_counter()
    sortedUrlList = (sorted(urlList, key=lambda i: i['LicenseID']))
    for r in sortedUrlList:
        print("----------")
        print(r['LicenseID'])
    print("Total number of searches: " + str(len(totalNumSearchs)))
    print("Total number of matches: " + str(len(urlList)))
    print(f'Finished in {round(finish-start, 2)} second(s)')
    return sortedUrlList


def checkUrlForLicenseType(ids):
    for i in ids:
        url = base_url + str(id)
        webpage = requests_session.get(base_url + str(id)).text
        soup = BeautifulSoup(webpage, "lxml")
        dom = etree.HTML(str(soup))
        License = getDataFromXpathDom(
            dom, '//*[@id="ctl00_MainContentPlaceHolder_lvResultsLicInfo_ctrl0_lblLicnumInfo"]')
        soup.decompose()
        if(License).startswith(license_type):
            return True
        else:
            return False
    print(f'Searched {len(ids)} users!')


def getUrlFromRedirect(ids):
    for id in ids:
        totalNumSearchs.append(id)
        try:
            response = requests_session.get(
                base_url + license_type + "-" + str(id))
            if response.history:
                for resp in response.history:
                    """ print(resp.status_code, resp.url) """
                """ print("Final destination:") """
                """ print(response.status_code, response.url) """
                if(response.url != no_match_url):
                    print('Found License user: ' +
                          license_type + "-" + str(id))
                    licensedUser = {"LicenseID": (
                        license_type + "-" + str(id)), 'URL': response.url}
                    urlList.append(licensedUser)
            else:
                print("Request was not redirected")
        except Exception as e:
            print(e)
        else:
            print('Not Found License user: ' + license_type + str(id))
    print(f'Searched {len(ids)} users!')


"""

results = executor.map(checkUrlForLicenseType, ids)

        for r in results:
            print(r)

Relevant info

Name xpath
//*[@id="ctl00_MainContentPlaceHolder_lvResults_ctrl0_lblPhyname"]

License xpath
//*[@id="ctl00_MainContentPlaceHolder_lvResultsLicInfo_ctrl0_lblLicnumInfo"]

"""
