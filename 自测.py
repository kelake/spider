#! /usr/bin/env python
# -*- coding: utf-8 -*-
#  @Time    :2018/12/5  16:55
#  @Author   :Kelake
#  @FileName :自测.py

#import urllib3
import random
import re
import requests

header = [{'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.76 Mobile Safari/537.36'},
          {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'},
          {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)'},
          {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1'},
          {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)'}]
#爬取笔趣阁的网络小说。
#respose = requests.get("http://www.biqukan.cc/book/20461/12592815.html",header = header[random.randint(0,4)])
#http = urllib3.PoolManager()
#爬取笔趣阁的网络小说。
r = requests.get('http://www.biqukan.cc/book/20461/12592816_2.html', headers=header[random.randint(0, 4)])
#爬取H网文
#r = requests.get('https://www.316pi.com/htm/novel10/112126.htm', headers=header[random.randint(0, 4)])
print("小说网站的状态码是：",r.status_code)
if r.status_code == 200:
    print("小说网正常！")
else:
    print("小说网不正常，请检查！")

#s = r.data.encode("UTF-8")
#s =  r.data.decode('UTF-8')
#s = r.data.encode('gb18030')
#s.decode('gbk')

#Python默认编码为ASCII码，网站源编码为utf-8，先要转成iso-8895-1,然后转成utf-8
#s = r.text.encode('iso-8859-1').decode('utf-8')
#Python默认编码为ASCII码，笔趣阁源编码为GBK，先要转成iso-8895-1,然后转成gbk
s = r.text.encode('iso-8859-1').decode('gbk')
#print(s)
#print(s)

#爬取笔趣阁的网络小说。
title = re.findall(r'<title>(.*?)</title>', s)

#爬取H网文
#title = re.findall(r'<title>(.*?) - </title>', s)

for t in title:
    print("\033[0;37;42m\t小说题目:\033[0m" + t)


#爬取笔趣阁的网络小说题目。
title = re.findall(r'<title>(.*?)</title>', s)

#爬取H网文题目
#kk = re.findall(r'<BR>(.*?)<BR>', s)

#爬取笔趣阁的网络小说。
#bookString=''
kk = re.findall(r'&nbsp;&nbsp;&nbsp;&nbsp;(.*?)<br />', s)
#for k in kk:
    #bookString=bookString+k
   #print(k)

str = '%s.*?<br />\r\n&nbsp;&nbsp;&nbsp;&nbsp;(.*?)<p class='%kk[-1]
#print(str)
#'<br />\r\n&nbsp;&nbsp;&nbsp;&nbsp;(.*?)<p class='
kkk = re.findall(str, s, re.S)
for k in kkk:
    kk.append(k)
#bookString=bookString+kkk[-1]

#print("这个是shabi：",kk)
for k in kk:
    print(k)



