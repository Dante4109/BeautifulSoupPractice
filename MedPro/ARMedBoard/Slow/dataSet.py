from bs4 import BeautifulSoup
from lxml import etree
import requests


class DataSet:
    def __init__(self,
                 Name,
                 PrimarySpeciality,
                 MailingAddress,
                 Address2,
                 City,
                 State,
                 Zip,
                 Phone,
                 Fax,
                 LicenseNumber,
                 OriginalIssueDate,
                 ExpirationDate,
                 LicenseStatus,
                 LicenseCateory,
                 BoardMinutes,
                 BoardOrders

                 ):
        self.Name = Name
        self.PrimarySpeciality = PrimarySpeciality
        self.MailingAddress = MailingAddress
        self.Address2 = Address2
        self.City = City
        self.State = State
        self.Zip = Zip
        self.Phone = Phone
        self.Fax = Fax
        self.LicenseNumber = LicenseNumber
        self.OriginalIssueDate = OriginalIssueDate
        self.ExpirationDate = ExpirationDate
        self.LicenseStatus = LicenseStatus
        self.LicenseCateory = LicenseCateory
        self.BoardMinutes = BoardMinutes
        self.BoardOrders = BoardOrders


def getDataSetFromUrl(url, requests_session):
    webpage = requests_session.get(url).text
    soup = BeautifulSoup(webpage, "lxml")
    dom = etree.HTML(str(soup))

    Name = getDataFromXpathDom(
        dom, '//*[@id="ctl00_MainContentPlaceHolder_lvResults_ctrl0_lblPhyname"]')
    PrimarySpeciality = getDataFromXpathDom(
        dom, '//*[@id="ctl00_MainContentPlaceHolder_lvResults_ctrl0_lblprimaryspecialty"]')
    MailingAddress = getDataFromXpathDom(
        dom, '//*[@id = "ctl00_MainContentPlaceHolder_lvResultsMail_ctrl0_lbladdr1"]')
    Address2 = getDataFromXpathDom(
        dom, '//*[@id = "ctl00_MainContentPlaceHolder_lvResultsMail_ctrl0_lbladdr2"]')
    City = getDataFromXpathDom(
        dom, '//*[@id = "ctl00_MainContentPlaceHolder_lvResultsMail_ctrl0_lblCity"]')
    State = getDataFromXpathDom(
        dom, '//*[@id = "ctl00_MainContentPlaceHolder_lvResultsMail_ctrl0_lblState"]')
    Zip = getDataFromXpathDom(
        dom, '//*[@id = "ctl00_MainContentPlaceHolder_lvResultsMail_ctrl0_lblZip"]')
    Phone = getDataFromXpathDom(
        dom, '//*[@id = "ctl00_MainContentPlaceHolder_lvResultsMail_ctrl0_lblphone"]')
    Fax = getDataFromXpathDom(
        dom, '//*[@id = "ctl00_MainContentPlaceHolder_lvResultsMail_ctrl0_lblFax"]')
    LicenseNumber = getDataFromXpathDom(
        dom, '//*[@id = "ctl00_MainContentPlaceHolder_lvResultsLicInfo_ctrl0_lblLicnumInfo"]')
    OriginalIssueDate = getDataFromXpathDom(
        dom, '//*[@id = "ctl00_MainContentPlaceHolder_lvResultsLicInfo_ctrl0_lblORdateInfo"]')
    ExpirationDate = getDataFromXpathDom(
        dom, '//*[@id = "ctl00_MainContentPlaceHolder_lvResultsLicInfo_ctrl0_lblEndDateInfo"]')
    LicenseStatus = getDataFromXpathDom(
        dom, '//*[@id = "ctl00_MainContentPlaceHolder_lvResultsLicInfo_ctrl0_lblStatusInfo"]')
    LicenseCateory = getDataFromXpathDom(
        dom, '//*[@id = "ctl00_MainContentPlaceHolder_lvResultsLicInfo_ctrl0_lblCategoryInfo"]')
    BoardMinutes = getDataFromXpathDom(
        dom, '//*[@id = "ctl00_MainContentPlaceHolder__lblBoardMinutes"]')
    BoardOrders = getDataFromXpathDom(
        dom, '//*[@id = "ctl00_MainContentPlaceHolder__lblBoardActions"]')

    newDataSet = DataSet(
        Name,
        PrimarySpeciality,
        MailingAddress,
        Address2,
        City,
        State,
        Zip,
        Phone,
        Fax,
        LicenseNumber,
        OriginalIssueDate,
        ExpirationDate,
        LicenseStatus,
        LicenseCateory,
        BoardMinutes,
        BoardOrders
    )
    return newDataSet


def getDataFromXpathDom(curDom, curXpath):
    try:
        value = (
            curDom.xpath(curXpath))
        if (value[0].text):
            return value[0].text
        else:
            return "none"
    except IndexError:
        return "none"


"""
Relevant Info

Name xpath
//*[@id="ctl00_MainContentPlaceHolder_lvResults_ctrl0_lblPhyname"]

Primary speciality xpath
//*[@id = "ctl00_MainContentPlaceHolder_lvResults_ctrl0_lblprimaryspecialty"]


MailingAddress
//*[@id="ctl00_MainContentPlaceHolder_lvResultsMail_ctrl0_lbladdr1"]

Address2
//*[@id="ctl00_MainContentPlaceHolder_lvResultsMail_ctrl0_lbladdr2"]

City
//*[@id="ctl00_MainContentPlaceHolder_lvResultsMail_ctrl0_lblCity"]

State
//*[@id="ctl00_MainContentPlaceHolder_lvResultsMail_ctrl0_lblState"]

Zip
//*[@id="ctl00_MainContentPlaceHolder_lvResultsMail_ctrl0_lblZip"]

Phone
//*[@id="ctl00_MainContentPlaceHolder_lvResultsMail_ctrl0_lblphone"]

Fax
//*[@id="ctl00_MainContentPlaceHolder_lvResultsMail_ctrl0_lblFax"]

LicenseNumber
//*[@id="ctl00_MainContentPlaceHolder_lvResultsLicInfo_ctrl0_lblLicnumInfo"]

OriginalIssueDate
//*[@id="ctl00_MainContentPlaceHolder_lvResultsLicInfo_ctrl0_lblORdateInfo"]

ExpirationDate
//*[@id="ctl00_MainContentPlaceHolder_lvResultsLicInfo_ctrl0_lblEndDateInfo"]

LicenseStatus
//*[@id="ctl00_MainContentPlaceHolder_lvResultsLicInfo_ctrl0_lblStatusInfo"]

LicenseCateory
//*[@id="ctl00_MainContentPlaceHolder_lvResultsLicInfo_ctrl0_lblCategoryInfo"]

BoardMinutes
//*[@id="ctl00_MainContentPlaceHolder_lblBoardMinutes"]

BoardOrders
//*[@id="ctl00_MainContentPlaceHolder_lblBoardActions"]


"""


"""
Relevant Info

base_xpath = '//*[@id="ctl00_MainContentPlaceHolder_lvResults_ctrl0_'

xPath_prefixes =


'//*[@id="ctl00_MainContentPlaceHolder_lvResults_ctrl0_lblPhyname"]'

Primary speciality xpath
//*[@id = "ctl00_MainContentPlaceHolder_lvResults_ctrl0_lblprimaryspecialty"]


MailingAddress
//*[@id="ctl00_MainContentPlaceHolder_lvResultsMail_ctrl0_lbladdr1"]

Address2
//*[@id="ctl00_MainContentPlaceHolder_lvResultsMail_ctrl0_lbladdr2"]

City
//*[@id="ctl00_MainContentPlaceHolder_lvResultsMail_ctrl0_lblCity"]

State
//*[@id="ctl00_MainContentPlaceHolder_lvResultsMail_ctrl0_lblState"]

Zip
//*[@id="ctl00_MainContentPlaceHolder_lvResultsMail_ctrl0_lblZip"]

Phone
//*[@id="ctl00_MainContentPlaceHolder_lvResultsMail_ctrl0_lblphone"]

Fax
//*[@id="ctl00_MainContentPlaceHolder_lvResultsMail_ctrl0_lblFax"]

LicenseNumber
//*[@id="ctl00_MainContentPlaceHolder_lvResultsLicInfo_ctrl0_lblLicnumInfo"]

OriginalIssueDate
//*[@id="ctl00_MainContentPlaceHolder_lvResultsLicInfo_ctrl0_lblORdateInfo"]

ExpirationDate
//*[@id="ctl00_MainContentPlaceHolder_lvResultsLicInfo_ctrl0_lblEndDateInfo"]

LicenseStatus
//*[@id="ctl00_MainContentPlaceHolder_lvResultsLicInfo_ctrl0_lblStatusInfo"]

LicenseCateory
//*[@id="ctl00_MainContentPlaceHolder_lvResultsLicInfo_ctrl0_lblCategoryInfo"]

BoardMinutes
//*[@id="ctl00_MainContentPlaceHolder_lblBoardMinutes"]

BoardOrders
//*[@id="ctl00_MainContentPlaceHolder_lblBoardActions"]


"""
