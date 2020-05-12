import requests
import hashlib
import random
import json
from urllib import parse

proxyDict = {"http": "http://ntproxy.qa.nt.ctripcorp.com:8080","https": "https://ntproxy.qa.nt.ctripcorp.com:8080"}
##proxyDict = {"http": "http://localhost:5389","https": "https://localhost:5389"}
acc = "17621980700"
pwd = "a123456789"

md5_pwd = hashlib.md5(pwd.encode('utf-8')).hexdigest()

logurl='http://www.jb.mil.cn/smartbus/interuser_loginNetUPK?method=loginNetNew&username={}&password={}&channel=111&{}'\
    .format(acc,md5_pwd,random.uniform(0, 1))
r = requests.get(logurl,proxies=proxyDict)
print(r.status_code,r.text,r.cookies)

jj = json.loads(r.text)
cookie="UserName={};phone={};globalUniqueID={};RealName=null;CardNo={};email={};UserType={};"\
    .format(jj['Result']['UserName'],jj['Result']['Phone'],jj['globalUniqueID'],jj['Result']['CardNo'],jj['Result']['Email'],jj['Result']['UserType']);

aspurl='http://ticket.jb.mil.cn/Home/Index?globalUniqueID={}'.format(jj['globalUniqueID'])
r = requests.get(aspurl,proxies=proxyDict)
print(r.status_code,r.cookies)

cookie+='ASP.NET_SessionId='+r.cookies['ASP.NET_SessionId']+';'

msg = '[{"Name":"asd","IdCard":"110101199003072551","PID":"677","CardType":"1"}]'
mm = 'zarr={}&larr={}&sarr={}&zarr2={}&date={}&price={}&GuideTel={}'.format(parse.quote(msg),parse.quote("[]"),parse.quote("[]"),parse.quote("[]"),parse.quote("2019-07-23"),parse.quote("0.00"),"15151966960")
r = requests.post('http://ticket.jb.mil.cn/Ticket/SingleOrderAdd',data=mm, \
              headers={'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8','Cookie':cookie})
print(r.status_code,r.text)





