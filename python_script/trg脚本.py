#唐人街
from bs4 import BeautifulSoup
import re
import requests
import logging
import time
import warnings
import traceback
logging.getLogger('requests').propagate = False
warnings.filterwarnings("ignore", category=UserWarning, module='bs4')
requests.packages.urllib3.disable_warnings()

filepath = r'D:\Users\yl_gong\Desktop\rrr.txt'
startpost=285349
stoppost=324828

dict1 = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0",
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
"Accept-Language": "en",
"Connection": "keep-alive",
"Upgrade-Insecure-Requests": "1"
}
#qazwsx18
#qwertyaz
#hhfbfdvv

session = requests.Session()


f = open(filepath, mode="a", encoding='utf-8')


# def continueread(i):
#     conurl = "https://www.trg2019.com/continue-read?id="+str(i)
#     session.get(conurl, headers=dict1, verify=False)

def logout():
    r = session.get('https://www.trg2019.com/logout', headers=dict1, verify=False)

def login():
    r = session.get('https://www.trg2019.com/login', headers=dict1, verify=False)
    soup = BeautifulSoup(r.content.decode("UTF-8"),"html.parser")
    _tk = str(soup.find("input", {"name": "_token"})['value'])
    dict2 = dict1.copy()
    dict2['Content-Type'] = 'application/x-www-form-urlencoded'
    dict2['Referer'] = 'https://www.trg2019.com/login'
    r = session.post("https://www.trg2019.com/login",
                     data={'_token': _tk, "username": "hhfbfdvv", "password": "a123456789", "remember": "on"},
                     headers=dict2, verify=False)

while stoppost>=startpost:
    #time.sleep(0.3)
    try:
        url = "https://www.trg2019.com/thread/" + str(stoppost)
        r = session.get(url, headers=dict1, verify=False)
        rawhtm = r.content.decode("UTF-8")
        if r'<a href="/login">登录</a>' in rawhtm:
            login()
            continue
        if r"看了这么多，请发个帖子分享下您的" in rawhtm:
            logout()
            login()
            continue
        soup = BeautifulSoup(rawhtm,"html.parser")
        breadcrumb = soup.find("ol", {"class": "breadcrumb"}).encode_contents().decode("UTF-8")
        content = soup.find("div", {"class": "panel panel-default"}).encode_contents().decode("UTF-8")
        pubtime = re.search(r'(?<=发表时间：).*?(?=\n)', rawhtm).group()
        tx = url + "---g3j81c63h424mrj---" + pubtime + "---g3j81c63h424mrj---" + breadcrumb + "---g3j81c63h424mrj---" + content
        tx = "<br/>".join(tx.split("\n"))+"\n"
        f.write(tx)
        f.flush()
        print(stoppost)
        stoppost -= 1
    except Exception:
        traceback.print_exc()
        stoppost -= 1
