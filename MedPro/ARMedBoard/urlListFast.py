from bs4 import BeautifulSoup
from lxml import etree
import cchardet
from dataSet import getDataFromXpathDom
import concurrent.futures
from concurrent.futures import ProcessPoolExecutor, as_completed
import time
import requests

urlList = []
base_url = "http://www.armedicalboard.org/Public/verify/results.aspx?strPHIDNO=ASMB"
requests_session = requests.Session()
license_type = "PA"
startRng = 18409
endRng = 18412

start = time.perf_counter()


def main():

    # context manager
    with concurrent.futures.ProcessPoolExecutor(max_workers=50) as executor:
        ids = range(startRng, endRng+1)
        futures = {executor.submit(
            checkUrlForLicenseType, id, 10): id for id in ids}
        for result in as_completed(futures):
            link = futures.get(result)
            try:
                data = result.result()
            except Exception as e:
                print(e)
            else:
                print("Link: {}, data: {}".format(link, data))
        end = time.time()
        print("Time Taken: {:.6f}s".format(end-start))

    requests_session.close()
    finish = time.perf_counter()
    print(urlList)
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
        urlList.append(url)
        return True
    else:
        return False


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
