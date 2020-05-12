import baostock as bs
import pandas as pd

#### 登陆系统 ####

lg = bs.login(user_id="anonymous", password="123456")
day = "2013-01-04"
rs = bs.query_all_stock(day=day)

rows_list = []
while (rs.error_code == '0') & rs.next():
    code = rs.get_row_data()[0];
    rsx = bs.query_history_k_data(code,
                                 "code,peTTM",
                                 start_date=day, end_date=day,
                                 frequency="d", adjustflag="3")
    if rsx.data[0][1] != '' and float(rsx.data[0][1])>0:
        rows_list.append([code, float(rsx.data[0][1])])
df = pd.DataFrame(rows_list,columns=['code','pe'])
df = df.sort_values('pe')
pd.set_option('display.max_rows', 400)
print(df.head(400))





#### 结果集输出到csv文件 ####
# result.to_csv("D:\\peTTM_sh.600000_data.csv", encoding="gbk", index=False)
# print(result)

#### 登出系统 ####
bs.logout()