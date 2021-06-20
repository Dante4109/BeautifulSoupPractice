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


def getLicenseData(body):
    aDict = body
    bDict = aDict['searchResults']
    Licenses = bDict[0]['licensees']
    return Licenses


""" 
example_jsonString = "{\"searchResults\":[{\"total\":566,\"mapZoom\":13,\"pageNumber\":1,\"licensees\":[{\"entityId\":1569734,\"lastName\":\"Aguirre-Wong\",\"firstName\":\"Neenah\",\"middleName\":\"Corinne\",\"license\":{\"number\":\"PG205486\",\"status\":\"Active\",\"type\":\"DPM Postgraduate License\"},\"addresses\":[{\"type\":\"Practice Address\",\"priority\":\"PRIMARY\",\"street1\":\"1015 NW 22nd Ave\",\"street2\":\"\",\"city\":\"Portland\",\"state\":\"OR\",\"county\":\"Multnomah\",\"country\":\"United States\",\"zip\":\"97210\",\"longitude\":-122.697577000,\"latitude\":45.530083000}]},{\"entityId\":1449273,\"lastName\":\"Aizawa\",\"firstName\":\"Hideaki\",\"middleName\":\"R\",\"license\":{\"number\":\"DP00037\",\"status\":\"Expired\",\"type\":\"DPM License\"}},{\"entityId\":1449269,\"lastName\":\"Aizawa\",\"firstName\":\"Joseph\",\"middleName\":\"Yoshiji\",\"license\":{\"number\":\"DP00033\",\"status\":\"Retired\",\"type\":\"DPM License\"}},{\"entityId\":1449431,\"lastName\":\"Albright\",\"firstName\":\"Estelle\",\"middleName\":\"\",\"license\":{\"number\":\"DP00198\",\"status\":\"Lapsed\",\"type\":\"DPM License\"},\"addresses\":[{\"type\":\"Practice Address\",\"priority\":\"\",\"street1\":\"VA Med Ctr, 1481 W. 10th Street\",\"street2\":\"Surgery Department\",\"city\":\"Indianapolis\",\"state\":\"IN\",\"county\":\"Marion\",\"country\":\"United States\",\"zip\":\"46202\",\"longitude\":-86.186824000,\"latitude\":39.778182000},{\"type\":\"Practice Address\",\"priority\":\"SECONDARY\",\"street1\":\"1481 W 10th Street\",\"street2\":\"\",\"city\":\"Indianapolis\",\"state\":\"IN\",\"county\":\"Marion\",\"country\":\"United States\",\"zip\":\"46202\",\"longitude\":-86.186824000,\"latitude\":39.778182000},{\"type\":\"Practice Address\",\"priority\":\"PRIMARY\",\"street1\":\"1481 W 10th St\",\"street2\":\"\",\"city\":\"Indianapolis\",\"state\":\"IN\",\"county\":\"Marion\",\"country\":\"United States\",\"zip\":\"46202\",\"longitude\":-86.186824000,\"latitude\":39.778182000}]},{\"entityId\":1449499,\"lastName\":\"Alumbaugh\",\"firstName\":\"Dana\",\"middleName\":\"\",\"license\":{\"number\":\"DP00266\",\"status\":\"Expired\",\"type\":\"DPM License\"}},{\"entityId\":1449562,\"lastName\":\"Anderson\",\"firstName\":\"Dale\",\"middleName\":\"Charles\",\"license\":{\"number\":\"DP00329\",\"status\":\"Expired\",\"type\":\"DPM License\"},\"addresses\":[{\"type\":\"Practice Address\",\"priority\":\"\",\"street1\":\"1253 Us 27 S\",\"street2\":\"\",\"city\":\"Sebring\",\"state\":\"FL\",\"county\":\"Highlands\",\"country\":\"United States\",\"zip\":\"33872\",\"longitude\":-81.467567000,\"latitude\":27.472673000}]},{\"entityId\":1449529,\"lastName\":\"Arabshahi\",\"firstName\":\"Hamid\",\"middleName\":\"Reza\",\"license\":{\"number\":\"DP00296\",\"status\":\"Active\",\"type\":\"DPM License\"},\"addresses\":[{\"type\":\"Practice Address\",\"priority\":\"PRIMARY\",\"street1\":\"1475 Commercial St SE\",\"street2\":\"\",\"city\":\"Salem\",\"state\":\"OR\",\"county\":\"Marion\",\"country\":\"United States\",\"zip\":\"97302\",\"longitude\":-123.044589000,\"latitude\":44.926580000},{\"type\":\"Practice Address\",\"priority\":\"SECONDARY\",\"street1\":\"6464 SW Borland Rd, Unit B3\",\"street2\":\"\",\"city\":\"Tualatin\",\"state\":\"OR\",\"county\":\"Washington\",\"country\":\"United States\",\"zip\":\"97062\",\"longitude\":-122.743045000,\"latitude\":45.376024000}]},{\"entityId\":1482800,\"lastName\":\"Arndt\",\"firstName\":\"David\",\"middleName\":\"Richard\",\"license\":{\"number\":\"DP154209\",\"status\":\"Active\",\"type\":\"DPM License\"},\"addresses\":[{\"type\":\"Practice Address\",\"priority\":\"PRIMARY\",\"street1\":\"2875 NW Stucki Ave.\",\"street2\":\"\",\"city\":\"Hillsboro\",\"state\":\"OR\",\"county\":\"Washington\",\"country\":\"United States\",\"zip\":\"97124\",\"longitude\":-122.876853000,\"latitude\":45.539370000}]},{\"entityId\":1520556,\"lastName\":\"Arrhenius\",\"firstName\":\"Daniel\",\"middleName\":\"Anders\",\"license\":{\"number\":\"DP157406\",\"status\":\"Expired\",\"type\":\"DPM License\"},\"addresses\":[{\"type\":\"Practice Address\",\"priority\":\"\",\"street1\":\"12942 Harbor Boulevard\",\"street2\":\"\",\"city\":\"Garden Grove\",\"state\":\"CA\",\"county\":\"Orange\",\"country\":\"United States\",\"zip\":\"92840\",\"longitude\":-117.918206000,\"latitude\":33.775158000}]},{\"entityId\":1449542,\"lastName\":\"Ashdown\",\"firstName\":\"Brian\",\"middleName\":\"Douglas\",\"license\":{\"number\":\"DP00309\",\"status\":\"Active\",\"type\":\"DPM License\"},\"addresses\":[{\"type\":\"Practice Address\",\"priority\":\"PRIMARY\",\"street1\":\"2605 Willetta St SW Ste D2\",\"street2\":\"\",\"city\":\"Albany\",\"state\":\"OR\",\"county\":\"Linn\",\"country\":\"United States\",\"zip\":\"97321\",\"longitude\":-123.114219000,\"latitude\":44.616022000}]}]}]}"
print(aDict.keys())
print(bDict[0]['total'])
print(bDict[0]['licensees']) 

"""
