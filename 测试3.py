#! /usr/bin/env python
#  _*_ coding:utf-8 _*_
#  @Time    :2018/12/7  14:57
#  @Author   :Kelake
#  @FileName :www.xbookcn.com.py

import random
import re
import requests
import urllib
import MySQLdb
import pymysql

# 打开数据库连接
db = MySQLdb.connect(host='192.168.7.248', user='root', passwd='KElake@1987', db="fiction_db", charset='utf8')
# 使用cursor()方法获取操作游标
cursor = db.cursor()
print("++++++++++++++++++++++++++")
cursor.execute("SELECT VERSION()")
data = cursor.fetchone()
print("Database version:MySQL_%s" %data[0])
print("++++++++++++++++++++++++++")
sql = """CREATE TABLE `FICTION` (
    `fiction`  text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL ,
    `link`  varchar(255) NOT NULL ,
    `title`  varchar(255) NULL ,
    `tag`  INT (255) NOT NULL AUTO_INCREMENT ,
    PRIMARY KEY (`tag`)
    );"""

try:
    cursor.execute(sql)
    print("try初始化创建数据表")
except:
    db.rollback()
    print("except跳过初始化创建表")


# def get_tag(str):
#     m1 = hashlib.md5()
#     m1.update(str.encode("utf-8"))
#     md5 = m1.hexdigest()
#     return md5


header = [{'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.76 Mobile Safari/537.36'},
          {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'},
          {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)'},
          {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1'},
          {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)'},
          {'User-Agent': 'Mozilla/5.0 (WindowsNT6.1; Win64;x64) AppleWebKit/537.36 (KHTML, likeGecko) Chrome/71.0.3578.80 Safari/537.36)'}]

# url="https://www.xbookcn.com/book/shenzhen/1.htm"
url = "https://www.317pi.com/htm/novel6/112131.htm"
resepose = requests.get(url, headers=header[random.randint(0, 5)])
if resepose.status_code == 200:
    print("网站状态正常！", resepose.status_code)

zhengwen = resepose.text.encode('iso-8859-1').decode('utf-8')
# print(zhengwen)

title = re.findall(r'<title>(.*?) - </title>' ,zhengwen)
for t in title:
    print("题目：%s" %(t))

zhengwen_jx = re.findall(r'<BR>(.*?)<BR>',zhengwen)

for zwjx in zhengwen_jx:
    print(zwjx)

zwjx = "".join(zhengwen_jx)
print("+++++++++++++++++插入数据+=============")
sql_inset = "REPLACE INTO FICTION(title,link,fiction) VALUES ('%s', '%s', '%s')" %(t, url, zwjx)
print(sql_inset)
print(zwjx)
print(type(zwjx))
try:
    cursor.execute(sql_inset)
    db.commit()
    print("try正常数据插入数据库……")
except:
    db.rollback()
    print("except插入数据库异常……")

cursor.execute("select * from FICTION")
kk = cursor.fetchone()
print(kk)
cursor.close()
db.close()

#################小说列表获取
# list_url = "https://www.316pi.com/htm/novellist6/"
list_url = "https://www.145du.com/htm/novellist1/"
xs_resepose = requests.get(list_url, headers=header[random.randint(0, 5)])
xs_jm = xs_resepose.text.encode('iso-8859-1').decode('utf-8')
xs_all = re.findall('<li><a class="text-overflow" href="/htm/novelindex.htm">(.*?)</a>',xs_jm)
xs_qg = re.findall('<li><a class="text-overflow" href="/htm/novellist1/">(.*?)</a>',xs_jm)
xs_xy = re.findall('<li><a class="text-overflow" href="/htm/novellist2/">(.*?)</a>',xs_jm)
xs_wx = re.findall('<li><a class="text-overflow" href="/htm/novellist4/">(.*?)</a>',xs_jm)
xs_jt = re.findall('<li><a class="text-overflow" href="/htm/novellist5/">(.*?)</a>',xs_jm)
xs_ll = re.findall('<li><a class="text-overflow active" href="/htm/novellist6/">(.*?)</a>',xs_jm)
xs_xa = re.findall('<li><a class="text-overflow" href="/htm/novellist8/">(.*?)</a>',xs_jm)
xs_qs = re.findall('<li><a class="text-overflow" href="/htm/novellist9/">(.*?)</a>',xs_jm)
xs_rq = re.findall('<li><a class="text-overflow" href="/htm/novellist10/">(.*?)</a>',xs_jm)
###########小说分类列表###############
print("###########小说分类列表###############")
print(xs_all[0])
# print(xs_qg[0])
print(xs_xy[0])
print(xs_wx[0])
print(xs_jt[0])
print(xs_ll[0])
print(xs_xa[0])
print(xs_qs[0])
print(xs_rq[0])

############小说列表############################
print("###########%s分类列表###############"%xs_ll[0])
lb = xs_resepose.text.encode('iso-8859-1').decode('utf-8')
xs_lb = re.findall('.htm" title="(.*?)" target="_blank"><span class="xslist text-bg-c">',lb)
for llb in xs_lb:
    print(llb)

#<li class="col-md-14 col-sm-16 col-xs-12 clearfix news-box">
# <a href="/htm/novel6/112182.htm" title="特别的生日礼物" target="_blank"><span class="xslist text-bg-c">特别的生日礼物　<font color="#808080">09-14</font></span></a></li><li class="col-md-14 col-sm-16 col-xs-12 clearfix news-box">
# <a href="/htm/novel6/112173.htm" title="我的出差奇遇记" target="_blank"><span class="xslist text-bg-c">我的出差奇遇记　<font color="#808080">09-13</font></span></a></li><li class="col-md-14 col-sm-16 col-xs-12 clearfix news-box">
# <a href="/htm/novel6/112162.htm" title="梦幻情人" target="_blank"><span class="xslist text-bg-c">梦幻情人　<font color="#808080">09-12</font></span></a></li><li class="col-md-14 col-sm-16 col-xs-12 clearfix news-box">
# <a href="/htm/novel6/112161.htm" title="疯狂的高潮" target="_blank"><span class="xslist text-bg-c">疯狂的高潮　<font color="#808080">09-12</font></span></a></li><li class="col-md-14 col-sm-16 col-xs-12 clearfix news-box">
# <a href="/htm/novel6/112146.htm" title="我的第一次绝对真人真事" target="_blank"><span class="xslist text-bg-c">我的第一次绝对真人真事　<font color="#808080">09-10</font></span></a></li><li class="col-md-14 col-sm-16 col-xs-12 clearfix news-box">
# <a href="/htm/novel6/112145.htm" title="孟氏和我的故事" target="_blank"><span class="xslist text-bg-c">孟氏和我的故事　<font color="#808080">09-10</font></span></a></li><li class="col-md-14 col-sm-16 col-xs-12 clearfix news-box">
# <a href="/htm/novel6/112131.htm" title="豪乳小姨子" target="_blank"><span class="xslist text-bg-c">豪乳小姨子　<font color="#808080">09-09</font></span></a></li><li class="col-md-14 col-sm-16 col-xs-12 clearfix news-box">
# <a href="/htm/novel6/112130.htm" title="比老婆还好的女人" target="_blank"><span class="xslist text-bg-c">比老婆还好的女人　<font color="#808080">09-09</font></span></a></li><li class="col-md-14 col-sm-16 col-xs-12 clearfix news-box">
# <a href="/htm/novel6/112105.htm" title="性愊有时我也很想要" target="_blank"><span class="xslist text-bg-c">性愊有时我也很想要　<font color="#808080">09-08</font></span></a></li><li class="col-md-14 col-sm-16 col-xs-12 clearfix news-box">
# <a href="/htm/novel6/112104.htm" title="五姊妹" target="_blank"><span class="xslist text-bg-c">五姊妹　<font color="#808080">09-08</font></span></a></li><li class="col-md-14 col-sm-16 col-xs-12 clearfix news-box">
# <a href="/htm/novel6/112103.htm" title="一段奇特香艳之旅" target="_blank"><span class="xslist text-bg-c">一段奇特香艳之旅　<font color="#808080">09-08</font></span></a></li><li class="col-md-14 col-sm-16 col-xs-12 clearfix news-box">
# <a href="/htm/novel6/112102.htm" title="我的骚货女朋友雯雯" target="_blank"><span class="xslist text-bg-c">我的骚货女朋友雯雯　<font color="#808080">09-08</font></span></a></li><li class="col-md-14 col-sm-16 col-xs-12 clearfix news-box">
# <a href="/htm/novel6/112071.htm" title="老爸的小媳妇" target="_blank"><span class="xslist text-bg-c">老爸的小媳妇　<font color="#808080">09-04</font></span></a></li><li class="col-md-14 col-sm-16 col-xs-12 clearfix news-box">
# <a href="/htm/novel6/112070.htm" title="我漂亮的太太李月儿" target="_blank"><span class="xslist text-bg-c">我漂亮的太太李月儿　<font color="#808080">09-04</font></span></a></li><li class="col-md-14 col-sm-16 col-xs-12 clearfix news-box">
# <a href="/htm/novel6/112069.htm" title="美味花蜜" target="_blank"><span class="xslist text-bg-c">美味花蜜　<font color="#808080">09-04</font></span></a></li><li class="col-md-14 col-sm-16 col-xs-12 clearfix news-box">
# <a href="/htm/novel6/112068.htm" title="肉欲客栈" target="_blank"><span class="xslist text-bg-c">肉欲客栈　<font color="#808080">09-04</font></span></a></li><li class="col-md-14 col-sm-16 col-xs-12 clearfix news-box">
# <a href="/htm/novel6/112051.htm" title="美姐凌辱计划" target="_blank"><span class="xslist text-bg-c">美姐凌辱计划　<font color="#808080">09-02</font></span></a></li><li class="col-md-14 col-sm-16 col-xs-12 clearfix news-box">
# <a href="/htm/novel6/112050.htm" title="被饲养的暑假旅游" target="_blank"><span class="xslist text-bg-c">被饲养的暑假旅游　<font color="#808080">09-02</font></span></a></li><li class="col-md-14 col-sm-16 col-xs-12 clearfix news-box">
# <a href="/htm/novel6/111994.htm" title="失恋后遗症" target="_blank"><span class="xslist text-bg-c">失恋后遗症　<font color="#808080">08-30</font></span></a></li><li class="col-md-14 col-sm-16 col-xs-12 clearfix news-box">
# <a href="/htm/novel6/111993.htm" title="忘記帶鎖匙" target="_blank"><span class="xslist text-bg-c">忘記帶鎖匙　<font color="#808080">08-30</font></span></a></li><li class="col-md-14 col-sm-16 col-xs-12 clearfix news-box">
# <a href="/htm/novel6/111992.htm" title="电影院的艳遇" target="_blank"><span class="xslist text-bg-c">电影院的艳遇　<font color="#808080">08-30</font></span></a></li><li class="col-md-14 col-sm-16 col-xs-12 clearfix news-box">
# <a href="/htm/novel6/111991.htm" title="异地的老婆找了个性伴侣" target="_blank"><span class="xslist text-bg-c">异地的老婆找了个性伴侣　<font color="#808080">08-30</font></span></a></li><li class="col-md-14 col-sm-16 col-xs-12 clearfix news-box">
# <a href="/htm/novel6/111990.htm" title="虐恋坠落" target="_blank"><span class="xslist text-bg-c">虐恋坠落　<font color="#808080">08-30</font></span></a></li><li class="col-md-14 col-sm-16 col-xs-12 clearfix news-box">
# <a href="/htm/novel6/111989.htm" title="难忘的聚会" target="_blank"><span class="xslist text-bg-c">难忘的聚会　<font color="#808080">08-30</font></span></a></li><li class="col-md-14 col-sm-16 col-xs-12 clearfix news-box">
# <a href="/htm/novel6/111988.htm" title="被情夫狂干" target="_blank"><span class="xslist text-bg-c">被情夫狂干　<font color="#808080">08-30</font></span></a></li>





