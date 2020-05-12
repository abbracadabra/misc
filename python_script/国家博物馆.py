import requests

proxyDict = {"http": "http://localhost:5389","https": "https://localhost:5389"}

#登陆
headers={'Content-Type': 'application/x-www-form-urlencoded','User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36"}
#
# r = requests.post("http://ticketapi.chnmuseum.cn/api/users/login",data="p=w&phone=17621980700&password=17621980700",headers=headers,proxies=proxyDict)
# print(r.status_code)
# print(r.text)
# print(r.cookies)

#下单
#单人api_token=978bd9b55bd475a262e9435f2ab9582c&p=w&td_tp_id=2644&toi_username%5B0%5D=asd&toi_cardtype_id%5B0%5D=1&toi_card_num%5B0%5D=110101198903079594&td_tp_ids%5B0%5D=&pt_id%5B0%5D=1&_sign=j9SqX0ESZk8aA1aANjSrLCyqdnguITmfq%252FzLD74I8To%253D
#多人api_token=978bd9b55bd475a262e9435f2ab9582c&p=w&td_tp_id=2644&toi_username%5B0%5D=%E8%AE%BD%E5%BE%B7%E8%AF%B5%E5%8A%9F&toi_username%5B1%5D=%E5%A4%A7%E5%B8%88%E5%82%85&toi_cardtype_id%5B0%5D=1&toi_cardtype_id%5B1%5D=1&toi_card_num%5B0%5D=11010119890307657X&toi_card_num%5B1%5D=110101198903072499&td_tp_ids%5B0%5D=&td_tp_ids%5B1%5D=&pt_id%5B0%5D=1&pt_id%5B1%5D=1&_sign=Dj3ZCFSf8Vgt%252FXMu90Q4lXNmXcPaRl0I1iIF5Nrnf6Q%253D
headers={"Content-Type":"application/x-www-form-urlencoded","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36",\
         }
data = {"api_token":"978bd9b55bd475a262e9435f2ab9582c","p":"w","td_tp_id":"4818","toi_username[0]":"阿斯达","toi_cardtype_id[0]":"1",\
        "toi_card_num[0]":"110101199003077934","td_tp_ids[0]":"","pt_id[0]":"1","_sign":"j9SqX0ESZk8aA1JVNjSrLCyqdnguITmfq/zLD74I8To="}
r = requests.post("http://ticketapi.chnmuseum.cn/api/ticketorder",data=data,headers=headers,proxies=proxyDict)
print(r.status_code)
print(r.text)
print(r.cookies)

#價格庫存
# headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36"}
# r = requests.get("http://ticketapi.chnmuseum.cn/api/ticket/calendar?p=w",headers=headers)
# print(r.status_code)
# print(r.text)
# print(r.cookies)

#查詢我的訂單
# headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36"}
# r = requests.get("http://ticketapi.chnmuseum.cn/api/my/ticketorder/detail?p=w&api_token=978bd9b55bd475a262e9435f2ab9582c&torder_id=1191359",headers=headers)
# print(r.status_code)
# print(r.text)
# print(r.cookies)
