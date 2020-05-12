# coding=utf8
# fa = open(r"C:\yl_gong\all_tmp4.txt",encoding="utf-8")
# fb = open(r"C:\yl_gong\all_tmp5.txt",'w',encoding="utf-8")
# for line in fa:
#     if not any(bad_word in line for bad_word in bad_words):
#         fb.write(line)
# fa.close()
# fb.close()

#提取地区
# map = {}
# fa = open(r"C:\yl_gong\all_tmp.txt",encoding="utf-8")
# fb = open(r"C:\yl_gong\all_tmp1.txt",'w',encoding="utf-8")
# i=0
# for line in fa:
#     try:
#         i+=1;
#         a = line.index(r'【')
#         b = line.index(r'】')
#         loc = line[a + 1:b]
#         map[loc] = 0
#         fb.write(loc + "---g3j81c63h424mrj---" + line)
#     except Exception as e:
#         print(i)
#         print(e)
# print(map)
# fa.close()
# fb.close()

# fa = open(r"C:\yl_gong\all_tmp1.txt",encoding="utf-8")
# fb = open(r"C:\yl_gong\all_tmp2.txt",'w',encoding="utf-8")

# bad_words=[r'<div','公告','举报','虚假','唐人阁','将军','版务','全国','临时','警告']
# fa = open(r"C:\yl_gong\all_tmp7.txt",encoding="utf-8")
# fb = open(r"C:\yl_gong\all_tmp8.txt",'w',encoding="utf-8")
# for line in fa:
#     sd = line.index('---g3j81c63h424mrj---')
#     dfr = line[0:sd]
#     if not any(bad_word in dfr for bad_word in bad_words):
#         fb.write(line)
# fa.close()
# fb.close()


# fa = open(r"C:\yl_gong\all_tmp7.txt",encoding="utf-8")
# fb = open(r"C:\yl_gong\all_tmp8.txt",'w',encoding="utf-8")
# for line in fa:
#     sd = line.index('---g3j81c63h424mrj---')
#     dfr = line[0:sd]
#     if len(dfr)<20:
#         fb.write(line)
# fa.close()
# fb.close()

# import re
# import datetime
# from dateutil.relativedelta import relativedelta
# tod = datetime.date.today()
# fa = open(r"C:\yl_gong\all_tmp8.txt",encoding="utf-8")
# fb = open(r"C:\yl_gong\all_tmp9.txt",'w',encoding="utf-8")
# for line in fa:
#     id = re.search("(?<=https://www.trg2019.com/thread/).*?(?=---g3j81c63h424mrj---)",line).group(0)
#     tim = line.split('---g3j81c63h424mrj---')[2]
#     if('年前' in tim):
#         delt = int(tim[0:-2])
#         nn = str(2019-delt)
#         mm = '02'
#     elif('月前' in tim):
#         delt = int(tim[0:-2])
#         frth = tod - relativedelta(months=delt)
#         nn = str(frth.year)
#         mm = str(frth.month)
#         if len(mm)==1:
#             mm='0'+mm
#     else:
#         nn = '2019'
#         mm = '01'
#     derq=nn+'_'+mm
#     cccc=id+'---g3j81c63h424mrj---'+derq
#     p = re.compile("---g3j81c63h424mrj---")
#     lll = list(p.finditer(line))
#     srta = lll[0].end()
#     endoe = lll[2].start()
#     newccc = line[0:srta]+cccc+line[endoe:]
#     fb.write(newccc)
# fa.close()
# fb.close()


# map={}
# import re
# fa = open(r"C:\yl_gong\all_tmp9.txt",encoding="utf-8")
# fb = open(r"C:\yl_gong\all_tmp10.txt",'w',encoding="utf-8")
# for line in fa:
#     p = re.compile("---g3j81c63h424mrj---")
#     lll = list(p.finditer(line))
#     srta = lll[2].end()
#     endoe = lll[3].start()
#     ccc = line[srta:endoe]
#     replaced = re.sub('【.*?】', '', ccc)
#     xps = re.compile("(?<=>)[^>]*?(?=</a>)")
#     xpsl = list(xps.finditer(replaced))
#     newccc = line[0:srta]+xpsl[0].group(0)+'---g3j81c63h424mrj---'+xpsl[1].group(0)+'---g3j81c63h424mrj---'+xpsl[2].group(0)+line[endoe:]
#     fb.write(newccc)
# fa.close()
# fb.close()

# import re
# fa = open(r"C:\yl_gong\all_tmp10.txt",encoding="utf-8")
# fb = open(r"C:\yl_gong\all_tmp11.txt",'w',encoding="utf-8")
# for line in fa:
#     h4 = re.search('<h4>(.*?)</h4>', line).group(1)
#     replaced = re.sub('\s', '', h4)
#     replaced = re.sub('<br/>', '', replaced)
#     replaced = re.search('^[^【]*?(?=：)', replaced)
#     if replaced == None or replaced.group().strip()=='':
#         replaced=r'无'
#     else:
#         replaced = replaced.group()
#     newccc = replaced+'---g3j81c63h424mrj---'+line
#     fb.write(newccc)
# fa.close()
# fb.close()


# from bs4 import BeautifulSoup
# import re
# fa = open(r"C:\yl_gong\all_tmp11.txt",encoding="utf-8")
# fb = open(r"C:\yl_gong\all_tmp12.txt",'w',encoding="utf-8")
# for line in fa:
#     p = re.compile("---g3j81c63h424mrj---")
#     lll = list(p.finditer(line))
#     srta = lll[-1].end()
#     sssr = line[srta:]
#     soup = BeautifulSoup(sssr, "html.parser")
#     xrt = soup.find("div", {"class": "post_xx small"})
#     mpp = {}
#     if xrt != None:
#         lcf = xrt.findChildren("div" , recursive=False)
#         for i in lcf:
#             ttr = i.text.strip()
#             if r'金币购买本帖' in ttr:
#                 continue
#             if ttr=='':
#                 continue
#             ixx = ttr.index(':')
#             kk = ttr[0:ixx].strip()
#             vv = ttr[ixx + 1:].strip()
#             if vv.strip() == '' or vv.strip() == '-':
#                 pass
#             else:
#                 mpp[kk] = vv
#     ppstr = str(mpp)
#     bbrq = soup.find("div", {"class": "post"})
#     postcon='无'
#     if bbrq != None:
#         postcon = bbrq.text
#     newccc = line[0:srta]+'---g3j81c63h424mrj---'+ppstr+'---g3j81c63h424mrj---'+postcon+'\n'
#     fb.write(newccc)
# fa.close()
# fb.close()

# import re
# fa = open(r"C:\yl_gong\all_tmp13.txt",encoding="utf-8")
# fb = open(r"C:\yl_gong\all_tmp14.txt",'w',encoding="utf-8")
# for line in fa:
#     line = re.sub("\s*！支持原创作者啊，有问题可联系发帖人，或评分/回帖/点评\.", '', line)
#     fb.write(line)
# fa.close()
# fb.close()



# import xlsxwriter
# workbook = xlsxwriter.Workbook('Expenses01.xlsx')
# worksheet = workbook.add_worksheet()
# fa = open(r"C:\yl_gong\all_tmp14.txt",encoding="utf-8")
# row = 0
# for line in fa:
#     col = 0
#     lss = line.split('---g3j81c63h424mrj---')
#     for ls in lss:
#         worksheet.write(row, col, ls)
#         col+=1
#     row += 1
# workbook.close()











