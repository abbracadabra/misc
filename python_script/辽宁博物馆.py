import requests
import hashlib
import random
import json
from urllib import parse

#可定检查
# headers={'Content-Type':'application/x-www-form-urlencoded;charset=UTF-8'}
# r = requests.post("http://npay.lnkjg.cn/kjg/ashx/ZHJQ/ReservationService.ashx",headers=headers,data="action=getWeekTicket")
# print(r.status_code,r.text,r.cookies)

#登陆
# headers={'Content-Type':'application/x-www-form-urlencoded'}
# r = requests.post("http://www.lnkjg.cn:8080/doSSOLogin.do",headers=headers,data="username=15271894594&password=15271894594",allow_redirects=False)
# print(r.headers["Location"])
# print(r.cookies)
#空 Location

#下单
# headers={'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8'}
# entourage = 2
# data={"action":"commitReservationApp","dataInfo":'[{"name":"牛肉粉","date":"2019-08-15","passway":"身份证通行","idcard":"110101199003079315","childnum":'+str(entourage)+',"usernum":'+str(entourage+1)+'}]',"ticketnum":(entourage+1),"UserPhone":"15271894594"}
# r = requests.post("http://npay.lnkjg.cn/kjg/ashx/ZHJQ/ReservationService.ashx",headers=headers,data=data,allow_redirects=False)
#action=commitReservationApp&dataInfo=%5B%7B%22name%22%3A%22%E9%98%BF%E6%96%AF%E8%BE%BE%22%2C%22date%22%3A%222019-08-29%22%2C%22passway%22%3A%22%E8%BA%AB%E4%BB%BD%E8%AF%81%E9%80%9A%E8%A1%8C%22%2C%22idcard%22%3A%22110101199003070572%22%2C%22childnum%22%3A0%2C%22usernum%22%3A1%7D%5D&ticketnum=1&UserPhone=13554344282
# print(r.status_code,r.text)
# print(r.headers)
#200 {"resultcode":1,"msg":"预约人:【同意】 在此日期已经预约不能重复预约"}
#200 {"resultcode":0,"msg":"成功"}

#查询当日预约
headers={'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8'}
data={"action":"getResOrderListApp","phone":"17621980700","type":"0","size":"9999"}
r = requests.post("http://npay.lnkjg.cn/kjg/ashx/ZHJQ/ReservationService.ashx",headers=headers,data=data,allow_redirects=False)
print(r.status_code,r.text)
print(r.headers)
#{"total":1,"rows":[{"Id":47766,"ReservationUserName":"同意","ReservationDate":"2019-08-15","ChildrenNum":2,"TicketNum":3,"OrderNo":"E201908151512260675242189011","State":1,"PassWay":"身份证通行","ResIDCard":"1****************1","ReservationIDCard":"110101199003073271","ResState":"待出票","TypeName":"预约票","PersonSum":3,"bz_count":3}]}

#退
# headers={'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8'}
# data={"action":"cancelReservation","Id":"47520"}
# r = requests.post("http://npay.lnkjg.cn/kjg/ashx/ZHJQ/ReservationService.ashx",headers=headers,data=data,allow_redirects=False)
# print(r.status_code,r.text)
# print(r.headers)
#{"resultcode":0,"msg":"成功"}

