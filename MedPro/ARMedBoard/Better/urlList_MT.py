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
endRng = 1000

start = time.perf_counter()


def main():
    # context manager
    with concurrent.futures.ThreadPoolExecutor(max_workers=60) as executor:
        ids = range(startRng, endRng+1)
        futures = {executor.submit(
            getUrlFromRedirect, id): id for id in ids}
        for result in as_completed(futures):
            link = futures.get(result)
            try:
                data = result.result()
                if(data):
                    urlList.append(data)
            except Exception as e:
                print(e)
            else:
                print("Link: {}, data: {}".format(link, data))
        end = time.time()
        print("Time Taken: {:.6f}s".format(end-start))

    requests_session.close()
    finish = time.perf_counter()
    sortedUrlList = (sorted(urlList, key=lambda i: i['LicenseID']))
    print(sortedUrlList)
    print("Total number of matches: " + str(len(urlList)))
    print(f'Finished in {round(finish-start, 2)} second(s)')
    return urlList


def checkUrlForLicenseType(id):
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


def getUrlFromRedirect(id):
    try:
        response = requests_session.get(
            base_url + license_type + "-" + str(id))
        if response.history:
            for resp in response.history:
                print(resp.status_code, resp.url)
            print("Final destination:")
            print(response.status_code, response.url)
            if(response.url != no_match_url):
                print('Found License user: ' + license_type + "-" + str(id))
                licensedUser = {"LicenseID": (
                    license_type + "-" + str(id)), 'URL': response.url}
                return licensedUser
        else:
            print("Request was not redirected")
            return None
    except Exception as e:
        print(e)
    else:
        print('Not Found License user: ' + license_type + str(id))
        return None


if __name__ == '__main__':
    main()


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
