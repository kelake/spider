#! /usr/bin/env python
#  _*_ coding:utf-8 _*_
#  @Time    :2018/12/11  16:17
#  @Author   :Kelake
#  @FileName :www.145du.com.py

import random
import re
import requests
import MySQLdb

header = [{'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.76 Mobile Safari/537.36'},
          {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'},
          {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)'},
          {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1'},
          {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)'}]

url_shouYe = "https://www.145du.com/"
respose = requests.get(url_shouYe, headers=header[random.randint(0, 4)])
print("小说网站的状态码是：", respose.status_code)
if respose.status_code == 200:
    print("小说网正常！")
else:
    print("小说网不正常，请检查！")


db = MySQLdb.connect(host='192.168.7.248', user='root', passwd='KElake@1987', db="www.145du.com", charset='utf8')
cursor = db.cursor()
cursor.execute("SELECT VERSION()")
data = cursor.fetchone()
print("Database version:MySQL_%s" %data[0])
# sql语句可以使用navicat工具来手动操作，然后再复制sql语句过来。
sql = """CREATE TABLE `shouYe` (
`tag`  int(255) NOT NULL AUTO_INCREMENT ,
`links`  varchar(255) NOT NULL ,
`title`  varchar(255) NULL ,
PRIMARY KEY (`tag`, `links`)
)
;"""

try:
    cursor.execute(sql)
    cursor.fetchall()
    print("try初始化创建数据表")
except Exception as e:
    print(e.args)
    db.rollback()
    cursor.fetchall()
    print("except跳过初始化创建表")


shouYe_text = respose.text.encode("iso-8859-1").decode("utf-8")
# print(shouYe_text)
# ====================进行大分类解析====================
print("======================================================")
title_01 = re.findall(r"""<div class="row-item-title bg_blue"><a href="#" class='c_white'>(.*?)</a></div>""", shouYe_text)
# print(title_01)

#取分类的链接地址
link = re.findall(r"""<a href=\"(.*?)" target=\"_blank\">""", shouYe_text)

list_02 = re.findall(r"""target=\"_blank\">(.*?)<\/a><\/li>""", shouYe_text)
# print(list_02)
for (link, list_02) in zip(link, list_02):
    title_02 = (list_02+"    ""https://www.145du.com%s"%link)
    print(title_02)
# "shouye"是mysql数据库的关键字，用双引号或者单引号没有用，必须使用键盘最左边那个符号才可以，不然显示mysql语法错误。
    sql_inset = """REPLACE INTO `shouYe`(links,title) VALUES ('%s', '%s')""" %(list_02, ("https://www.145du.com"+link))
    try:
        cursor.execute(sql_inset)
        cursor.fetchall()
        db.commit()
        print("try正在将数据写入数据库，请勿操作……")
    except:
        cursor.fetchall()
        db.rollback()
        print("except插入数据库异常……")
cursor.close()
db.close()