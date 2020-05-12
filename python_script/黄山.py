import requests
import hashlib
import json
import regex as re
import html

acc="xxx"
mi = "xxx"
tk="ticket2019011813585029018"

headers = requests.utils.default_headers()
headers.update(
    {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; Trident/7.0; rv:11.0) like Gecko'
    }
)



data = {"loginName":acc,"loginPass":hashlib.md5(mi.encode('utf-8')).hexdigest()}
r= requests.post("https://www.huangshan.com.cn/leaguerLogin?",data=data,allow_redirects=False,verify=False,headers=headers)
sess = r.cookies['sendinfoHsPc']
print(sess)
# idNos="110101199003079518"
# linkMans = "阿斯达"
# teles = "15151966960"
# data={"beginDate":"2020-04-29","endDate":"2020-04-30","amount":"1","linkMans":linkMans,"teles":teles,
#       "idNos":idNos,"rateCode":tk,
#       "couponCode":"","couponCheckCode":"","sign":hashlib.md5(("idNos=%s&linkMans=%s&teles=%s"%(idNos,linkMans,teles)).encode('utf-8')).hexdigest()}
#
# r= requests.post("https://www.huangshan.com.cn/order/ticket/"+tk+"?parkId=1",data=data,allow_redirects=False,cookies={'sendinfoHsPc':sess},verify=False,headers=headers)
# ordno = json.loads(r.text)[0]['data']['orderNo']
# iidd = json.loads(r.text)[0]['data']['id']
# zhn = json.loads(r.text)[0]['data']['orderInfo']
# paysum = json.loads(r.text)[0]['data']['paySum']

#31微信 21支付宝
# data={"orderId":iidd,"payType":31,"orderNo":ordno,"paySum":paysum,"orderInfo":zhn}
# r = requests.get("https://www.huangshan.com.cn/pay/ticket",params=data,allow_redirects=False,cookies={'sendinfoHsPc':sess},verify=False)
# qrc = re.search("weixin://.*?(?=')", r.text).group(0)
# print(qrc)

# data={"orderId":iidd,"payType":21,"orderNo":ordno,"paySum":paysum,"orderInfo":zhn}
# r = requests.get("https://www.huangshan.com.cn/pay/ticket",params=data,allow_redirects=False,cookies={'sendinfoHsPc':sess},verify=False,headers=headers)
# print(r.text)
# qrc = re.search("<form[.\s\S]+?</form>", r.text).group(0)
# print(qrc)






