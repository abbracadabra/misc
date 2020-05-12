import requests
proxyDict = {"http": "http://ntproxy.qa.nt.ctripcorp.com:8080","https": "https://ntproxy.qa.nt.ctripcorp.com:8080"}
#proxyDict = {"http": "http://localhost:5389","https": "https://localhost:5389"}
# r = requests.post("https://eapi.broadwayinbound.com/BIWS.svc",data=r"""
# <soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
#   <soap:Header>
#     <AuthHeader xmlns="http://tempuri.org/">
#       <username>90063</username>
#       <password>Ctrip2019</password>
#     </AuthHeader>
#   </soap:Header>
#   <soap:Body>
#     <PerformancesPOHPricesAvailability xmlns="http://tempuri.org/">
#       <SaleTypesCode>F</SaleTypesCode>
#       <ShowCityCode>NYCA</ShowCityCode>
#       <DateBegins>2019-09-12</DateBegins>F
#       <DateEnds>2019-11-23</DateEnds>
#       <OneShowCode>poncho</OneShowCode>
#       <AvailabilityType></AvailabilityType>
#       <BestSeatsOnly></BestSeatsOnly>
#       <LastChangeDate>2000-01-01</LastChangeDate>
#     </PerformancesPOHPricesAvailability>
#   </soap:Body>
# </soap:Envelope>
# """,headers={'Content-Type': 'text/xml; charset=utf-8;',"SOAPAction":r'"http://tempuri.org/PerformancesPOHPricesAvailability"'},proxies=proxyDict)
# #
# print(r.status_code)
# print(r.text)

testacc='89550'
testpwd='Ctrip626x'
testurl='https://eapiqa.dqbroadwayinbound.com/BIWS.svc'
prdacc='90063'
prdpwd='Ctrip2019'
prdurl="https://eapi.broadwayinbound.com/BIWS.svc"
#
# #showbasics
r = requests.post(prdurl,data=r"""
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:tem="http://tempuri.org/">
   <soapenv:Header>
      <tem:AuthHeader>
         <tem:username>90063</tem:username>
         <tem:password>Ctrip2019</tem:password>
      </tem:AuthHeader>
   </soapenv:Header>
   <soapenv:Body>
      <tem:ShowBasics>
         <tem:SaleTypesCode></tem:SaleTypesCode>
         <tem:ShowCityCode>LASV</tem:ShowCityCode>
         <tem:ShowAddedDate>2001-01-01</tem:ShowAddedDate>
      </tem:ShowBasics>
   </soapenv:Body>
</soapenv:Envelope>
""",headers={'Content-Type': 'text/xml; charset=utf-8',"SOAPAction":'"http://tempuri.org/ShowBasics"'},proxies=proxyDict)
#
print(r.status_code)
print(r.text)