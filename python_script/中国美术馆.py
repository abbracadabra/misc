import requests
import hashlib
import random
import json
from urllib import parse
import time
#可定
# r = requests.get("http://www.namoc.org/ucenter/bookinfo.jsp",allow_redirects=False)
# print(r.text)
# print(r.headers)

#登陆
r = requests.get("http://www.namoc.org/ids/admin/login.jsp",allow_redirects=False)
trsidsssosessionid = r.cookies['trsidsssosessionid']
print(trsidsssosessionid)
r = requests.get('http://www.namoc.org/ids/admin/abc.code',cookies={"trsidsssosessionid":trsidsssosessionid},allow_redirects=False)
verifycode=1111
data={"returnUrl":"","loginType":"userName","show2FA":"false","userName":"15151966969","password":"15151966969","verifycode":verifycode}
r = requests.post("http://www.namoc.org/ids/admin/do_login.jsp",data=data,allow_redirects=False,cookies={'trsidsssosessionid':trsidsssosessionid})
r = requests.get("http://www.namoc.org/ucenter/noop.jsp",allow_redirects=False)
ucJSESSIONID = r.cookies['JSESSIONID']
print(ucJSESSIONID)
r = requests.get(r.headers['Location'],allow_redirects=False,cookies={'trsidsssosessionid':trsidsssosessionid})
r = requests.get("http://www.namoc.org/ucenter/index.jsp",allow_redirects=False,cookies={'JSESSIONID':ucJSESSIONID,'com.trs.idm.coSessionId':ucJSESSIONID})
print(r.text)

#ucJSESSIONID = '0E7AF1B51B251D8CC1CC737C506994E7'
#可定
# r = requests.get('http://www.namoc.org/ucenter/ticket.jsp',cookies={'JSESSIONID':ucJSESSIONID,'com.trs.idm.coSessionId':ucJSESSIONID},allow_redirects=False)
# print(r.status_code, r.text)



#下单
# data={'bookDate':'2019-08-31','bookDateText':'2019年08月31日+星期六','trueName':'大十分','userMobile':'17621988911','userIdNo':'110101199003071495','bookCount':'1'}
# r = requests.post('http://www.namoc.org/ucenter/bookUser',data=data,cookies={'JSESSIONID':ucJSESSIONID,'com.trs.idm.coSessionId':ucJSESSIONID},allow_redirects=False)
# print(r.status_code,r.text)
#info||您已成功预约2019年08月23日+星期五的门票1张!
#alert||您今天已经预约1张，最多还可预约0张
#一个账号一天一单


#退
# r = requests.get('http://www.namoc.org/ucenter/delBookUser?bookID=247836&bookDate=2019-08-30',cookies={'JSESSIONID':ucJSESSIONID,'com.trs.idm.coSessionId':ucJSESSIONID},allow_redirects=False)
# print(r.status_code, r.text)