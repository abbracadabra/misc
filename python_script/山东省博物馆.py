import requests

acc = '撒旦'
#123456
data={'name':acc,'time':'2019-10-10','num':'1','zhengjian':'身份证:110101199003078494','zname':'啊十分大师傅'}
r = requests.post('http://www.sdmuseum.com/gentleCMS/yuyuexinxi/addforyuyue.do',data=data)
print(r.text)