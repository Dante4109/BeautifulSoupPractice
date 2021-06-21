from seleniumwire import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from dataSet import getLicenseData
import requests
import json
import time


def getLicenseDataFromOR():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    """ options.add_argument('--headless') """
    options.add_argument('--no-sandbox')
    options.add_argument('--ignore-certificate-errors-spki-list')
    options.add_argument('--ignore-ssl-errors')
    webdriver_path = (
        'F:/Programs/Python/BeautifulSoupPractice/chromedriver_win32/chromedriver.exe')
    dataSetList = list()
    results = 30
    results_per_page = 10
    page_count = 1
    page_xpath_num = 2  # This is actually page 1 button starting

    # xpaths
    more_options = '/html/body/div[1]/div/alx-search/div/div[2]/div[1]/div/alx-form/form/div[3]/div[1]/button'
    license_type = '/html/body/div[1]/div/alx-search/div/alx-filter/div/div[3]/div[1]/span[2]'
    podiatrist = '/html/body/div[1]/div/alx-search/div/alx-filter/div/div[3]/ul/li[2]/div'
    search_button = '/html/body/div[1]/div/alx-search/div/div[2]/div[1]/div/alx-form/form/div[3]/div[2]/div/button[2]'

    web_url = 'https://techmedweb.omb.state.or.us/search'

    post_url = 'https://techmedweb.omb.state.or.us/api/licensee-search'
    data = {"distance": "5", "nameMatch": "Exact", "address": "All", "pagenumber": 1, "token": "03AGdBq24aFbrydUeiHxp8pPq4ZRz0rSf070XVmLL_yDfdLVZqhkbVjk4QLzV3hnPDuayhxYGkXsvxqNHrynWbOYEmnQtciW6VFkp6UMvhtER8YwPVEUxvzpAqBWA9M9Dk_CiTU150SrG7yYhqz-CViQp7NrQXmfDz4V7behUfdQSmckioO1aL0WTOrAuru1cCu60RsYzW_QEl64__xi144zyagyz1NwjZsk6H54Y0WgASyEr-l7KjxXbcICEyr502TQAxLcjev-6obfb--mJmDr-4_xZw0f2jLkOJwOl1415DlF08BPJbgzDgdw0k5CiMDT5uLDv0OUyYBxvnNBwgbwsbc4gBY4tAtGVkh-0DnoZ_Ajd2x6jxNWa6Ngo7B57jpMkn-kryDSuYhp9OjyYgSD7Vs23SWNY7rsvZIMPInSxFDJdj0Clib5b1zhYhVzw06D6N7LyhBue2Z8L85lHn-3Pw9AOcxmV4q11PjAFaLfSwTx9OGjCfxThPapHbXrfwJLcGGuCEo4W2OOFMTQ8Rq2XwmPbCn5zx5w", "license": "Podiatrist"}

    driver = webdriver.Chrome(options=options, executable_path=webdriver_path)
    driver.get(web_url)
    """ cookies = driver.get_cookies()
    print(cookies)
    agent = driver.execute_script("return navigator.userAgent")
    print(agent) """
    driver.find_element_by_xpath(more_options).click()
    WebDriverWait(driver, 10)
    if(driver.find_element_by_xpath(
            '/html/body/div[1]/div/alx-search/div/alx-filter')):
        print("element found!")
    else:
        print("element not found!")
    WebDriverWait(driver, 10)
    element = driver.find_element(By.XPATH, license_type)
    driver.execute_script("arguments[0].click();", element)
    print("Clicked license dropdown")
    WebDriverWait(driver, 10)
    element = driver.find_element(By.XPATH, podiatrist)
    driver.execute_script("arguments[0].click();", element)
    print("Clicked Podiatrist")
    WebDriverWait(driver, 100)
    driver.find_element_by_xpath(search_button).click()
    """ script = "alert('Alert via selenium')"
    driver.execute_script(script) """
    # You are now at page 1
    max_page_count = getMaxPageCount(results, results_per_page)
    print(max_page_count)
    # check return results
    page_xpath_num = page_xpath_num + 1  # expected to already be on page 1

    for i in range(page_count, (max_page_count + 1)):
        print("Page numnber: " + str(i))
        print("xpath_index: " + str(page_xpath_num))
        time.sleep(5)
        currentDataSet = getLicensesFromRequestData(driver)
        dataSetList.append(currentDataSet)
        time.sleep(5)
        if (page_xpath_num == 12):
            if(i & 1):
                page_xpath_num = 11
                # don't navigate to next page
            else:
                page_xpath_num = 3
                navigateNextPage(driver)
        time.sleep(10)
        navigateNextResult(driver, page_xpath_num)
        page_xpath_num = page_xpath_num + 1

    return dataSetList


def navigateNextResult(driver, page_xpath_num):
    WebDriverWait(driver, 10)
    page_button = (
        '/html/body/div[1]/div/alx-search/div/div[5]/div/alx-results/nav/ul/li[' + str(page_xpath_num) + ']/a')
    element = driver.find_element(By.XPATH, page_button)
    driver.execute_script("arguments[0].click();", element)


def navigateNextPage(driver):
    WebDriverWait(driver, 10)
    page_button = (
        '/html/body/div[1]/div/alx-search/div/div[5]/div/alx-results/nav/ul/li[12]/a')
    element = driver.find_element(By.XPATH, page_button)
    driver.execute_script("arguments[0].click();", element)


def getLicensesFromRequestData(driver):
    for request in driver.requests:
        if request.path == '/api/licensee-search':
            body_unicode = request.response.body.decode('utf-8')
            body = json.loads(body_unicode)
            licenses = getLicenseData(body)
    return licenses


def getMaxPageCount(results, results_per_page):
    max_page_count = round(results / results_per_page)
    if (max_page_count > 0):
        return max_page_count
    else:
        return 1
