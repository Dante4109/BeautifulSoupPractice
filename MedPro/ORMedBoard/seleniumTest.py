from seleniumwire import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from dataSet import getLicenseData
import requests
import json
import time


def seleniumTestChrome():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    """ options.add_argument('--headless') """
    options.add_argument('--no-sandbox')
    options.add_argument('--ignore-certificate-errors-spki-list')
    options.add_argument('--ignore-ssl-errors')
    webdriver_path = 'F:/Programs/Python/BeautifulSoupPractice/chromedriver_win32/chromedriver.exe'
    driver = webdriver.Chrome(options=options, executable_path=webdriver_path)

    starting_pagexpath_index = 2

    # xpaths
    more_options = '/html/body/div[1]/div/alx-search/div/div[2]/div[1]/div/alx-form/form/div[3]/div[1]/button'
    license_type = '/html/body/div[1]/div/alx-search/div/alx-filter/div/div[3]/div[1]/span[2]'
    podiatrist = '/html/body/div[1]/div/alx-search/div/alx-filter/div/div[3]/ul/li[2]/div'
    search_button = '/html/body/div[1]/div/alx-search/div/div[2]/div[1]/div/alx-form/form/div[3]/div[2]/div/button[2]'

    web_url = 'https://techmedweb.omb.state.or.us/search'

    post_url = 'https://techmedweb.omb.state.or.us/api/licensee-search'
    data = {"distance": "5", "nameMatch": "Exact", "address": "All", "pagenumber": 1, "token": "03AGdBq24aFbrydUeiHxp8pPq4ZRz0rSf070XVmLL_yDfdLVZqhkbVjk4QLzV3hnPDuayhxYGkXsvxqNHrynWbOYEmnQtciW6VFkp6UMvhtER8YwPVEUxvzpAqBWA9M9Dk_CiTU150SrG7yYhqz-CViQp7NrQXmfDz4V7behUfdQSmckioO1aL0WTOrAuru1cCu60RsYzW_QEl64__xi144zyagyz1NwjZsk6H54Y0WgASyEr-l7KjxXbcICEyr502TQAxLcjev-6obfb--mJmDr-4_xZw0f2jLkOJwOl1415DlF08BPJbgzDgdw0k5CiMDT5uLDv0OUyYBxvnNBwgbwsbc4gBY4tAtGVkh-0DnoZ_Ajd2x6jxNWa6Ngo7B57jpMkn-kryDSuYhp9OjyYgSD7Vs23SWNY7rsvZIMPInSxFDJdj0Clib5b1zhYhVzw06D6N7LyhBue2Z8L85lHn-3Pw9AOcxmV4q11PjAFaLfSwTx9OGjCfxThPapHbXrfwJLcGGuCEo4W2OOFMTQ8Rq2XwmPbCn5zx5w", "license": "Podiatrist"}
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

    time.sleep(10)
    # Get Requests
    starting_pagexpath_index = starting_pagexpath_index + 1
    navigateNextResult(driver, starting_pagexpath_index)

    time.sleep(10)
    # Get Requests
    starting_pagexpath_index = starting_pagexpath_index + 1
    navigateNextResult(driver, starting_pagexpath_index)

    time.sleep(10)
    # Get Requests
    starting_pagexpath_index = starting_pagexpath_index + 1
    navigateNextResult(driver, starting_pagexpath_index)

    time.sleep(10)
    # Get Requests
    starting_pagexpath_index = starting_pagexpath_index + 1
    navigateNextResult(driver, starting_pagexpath_index)

    time.sleep(10)
    # Get Requests
    starting_pagexpath_index = starting_pagexpath_index + 1
    navigateNextResult(driver, starting_pagexpath_index)


def navigateNextResult(driver, starting_pagexpath_index):
    WebDriverWait(driver, 10)
    page_button = (
        '/html/body/div[1]/div/alx-search/div/div[5]/div/alx-results/nav/ul/li[' + str(starting_pagexpath_index) + ']/a')
    element = driver.find_element(By.XPATH, page_button)
    driver.execute_script("arguments[0].click();", element)


def getLicensesFromRequestData(driver):
    for request in driver.requests:
        if request.path == '/api/licensee-search':
            body_unicode = request.response.body.decode('utf-8')
            body = json.loads(body_unicode)
            licenses = getLicenseData(body)
      return licenses 

