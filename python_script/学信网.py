import requests
from bs4 import BeautifulSoup

http_proxy  = "http://127.0.0.1:5389"
https_proxy = "https://127.0.0.1:5389"

proxyDict = {
              "http"  : http_proxy,
              "https" : https_proxy
            }

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36"
}
r = requests.get('https://account.chsi.com.cn/passport/login?service=https%3A%2F%2Fmy.chsi.com.cn%2Farchive%2Fj_spring_cas_security_check',verify=False,headers=headers,proxies=proxyDict,allow_redirects=False)
soup = BeautifulSoup(r.text, 'lxml')
dt = {
# 'username': '15151966960',
# 'password': 'R09066097583',
    'username': '15837830325',
    'password': 'gao3021696',
    'lt': soup.select_one("input[name='lt']")['value'],
    'execution': soup.select_one("input[name='execution']")['value'],
    '_eventId': soup.select_one("input[name='_eventId']")['value'],
    'submit': soup.select_one("input[name='submit']")['value']
}
cks = r.cookies
r = requests.post('https://account.chsi.com.cn/passport/login;jsessionid='+cks['JSESSIONID']+'?service=https%3A%2F%2Fmy.chsi.com.cn%2Farchive%2Fj_spring_cas_security_check',cookies=cks,verify=False,headers=headers,proxies=proxyDict,allow_redirects=False,
                  data=dt)
loc_302 = r.headers['Location']
del r.cookies._cookies['account.chsi.com.cn']['/cas']['CASPRIVACY']
cks2 = {**cks, **(r.cookies)}
r = requests.get(loc_302,verify=False,cookies=cks2,headers=headers,proxies=proxyDict,allow_redirects=False)
cks3 = {**cks2, **r.cookies}
# loc_302_2 =  r.headers['Location']
# r = requests.get(loc_302_2,verify=False,cookies=cks3)

# r = requests.get('https://my.chsi.com.cn/archive/index.action',verify=False,cookies=cks3,headers=headers,proxies=proxyDict,allow_redirects=False)
# print(r.text)

r = requests.get('https://my.chsi.com.cn/archive/gdjy/xj/show.action',verify=False,cookies=cks3,headers=headers,proxies=proxyDict,allow_redirects=False)
cks4 = {**cks3, **r.cookies}
soup = BeautifulSoup(r.text, 'lxml')
photourl = soup.select("img.xjxx-img")[0]['src']
r = requests.get(photourl,verify=False,cookies=cks4,headers=headers,proxies=proxyDict,allow_redirects=False)
with open('./bbb.png', 'wb') as f:
    f.write(r.content)








