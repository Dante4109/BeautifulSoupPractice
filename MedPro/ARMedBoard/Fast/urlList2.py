from bs4 import BeautifulSoup
from lxml import etree
import cchardet
from dataSet import getDataFromXpathDom
import concurrent.futures
from concurrent.futures import ProcessPoolExecutor, as_completed
from concurrent.futures import ThreadPoolExecutor, as_completed
import time
import requests

start = time.perf_counter()

urlList = []
base_url = "http://www.armedicalboard.org/Public/verify/results.aspx?strPHIDNO=ASMB"
requests_session = requests.Session()
license_type = "PA"
startRng = 18409
endRng = 18600
ids = [*range(startRng, endRng, 1)]

# Max number of processes
number_of_chunks = 10
# Batches of tasks to complete on a single process
chunk_size = 50


def main():

    # context manager
    with concurrent.futures.ProcessPoolExecutor(max_workers=number_of_chunks) as executor:
        futures = []
        for i in range(number_of_chunks):
            chunk = ids[i*chunk_size:(i+1)*chunk_size]
            futures.append(executor.submit(checkUrlForLicenseType, chunk))

        for future in concurrent.futures.as_completed(futures):
            link = futures[0].get(future)
            try:
                data = future.result()
            except Exception as e:
                print(e)
            else:
                print("Link: {}, data: {}".format(link, data))

    requests_session.close()
    finish = time.perf_counter()
    print(urlList)
    print("Total number or urls checked: " + str(endRng - startRng))
    print("Total number of matches: " + str(len(urlList)))
    print(f'Finished in {round(finish-start, 2)} second(s)')
    return urlList


def checkUrlForLicenseType(ids):
    for id in ids:
        url = base_url + str(id)
        print(f'Checking License for: {id}')
        webpage = requests_session.get(base_url + str(id)).text
        soup = BeautifulSoup(webpage, "lxml")
        dom = etree.HTML(str(soup))
        License = getDataFromXpathDom(
            dom, '//*[@id="ctl00_MainContentPlaceHolder_lvResultsLicInfo_ctrl0_lblLicnumInfo"]')
        soup.decompose()
        if(License).startswith(license_type):
            print("Match!")
            urlList.append(url)
            return True
        else:
            return False

    print(f'Completed check for {len(ids)} ids!')


if __name__ == '__main__':
    main()


"""
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



results = executor.map(checkUrlForLicenseType, ids)

        for r in results:
            print(r)

Relevant info

Name xpath
//*[@id="ctl00_MainContentPlaceHolder_lvResults_ctrl0_lblPhyname"]

License xpath
//*[@id="ctl00_MainContentPlaceHolder_lvResultsLicInfo_ctrl0_lblLicnumInfo"]

"""
