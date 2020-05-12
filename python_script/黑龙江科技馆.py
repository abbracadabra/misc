import requests
import json
import regex
# data={}
# requests.post('http://ticket.hljstm.org.cn/api/ticketorder',data=)

#可定
date='2019-09-11'
r = requests.get('http://ticket.hljstm.org.cn/api/ticket/calendar?p=w')
print(r.text)
js = json.loads(r.text)
tpid = [j for j in js['data']['yy_date'] if j['t_date']==date][0]['tp'][1]['td_tp_id']

#登陆
r = requests.get('http://www.hljstm.org.cn/portal/guest/index')
sessid = r.cookies['PHPSESSID']
r = requests.post('http://www.hljstm.org.cn/user/login/dologin',cookies={'PHPSESSID':sessid},data={'username':'2062460209@qq.com','password':'123456'})
r = requests.get('http://www.hljstm.org.cn/portal/guest/index',cookies={'PHPSESSID':sessid,'userName':'2062460209%40qq.com','pwd':'123456'})
apitoken=regex.search('(?<=data-token=")([^"]+)(?=")',r.text).group(0)

#下单
# data={'api_token':apitoken,'p':'w','toi_username[]':'阿斯达','toi_username[]':'发大水','toi_cardtype_id[]':'1','toi_cardtype_id[]':'1','toi_card_num[]':'110101199003076616','toi_card_num[]':'110101199003076018','toi_child_count[]':'0','toi_child_count[]':'0','td_tp_id':str(tpid)}
# r = requests.post('http://ticket.hljstm.org.cn/api/ticketorder',data=data)
# print(r.text)
# js = json.loads(r.text)
# tid = js['data']['torder_id']

#查询
# r = requests.get('http://ticket.hljstm.org.cn/api/my/ticketorder/detail?p=w&api_token='+apitoken+'&torder_id='+str(tid))
# print(r.text)
# js = json.loads(r.text)
# titems = [j['titem_id'] for j in js['data']['item']]

#退票
# data={'p':'w','api_token':apitoken,'titem_id':titems[0]}
# requests.post('http://ticket.hljstm.org.cn/api/ticketorder/refund',data=data)
# print(r.text)

