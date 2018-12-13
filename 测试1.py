#! /usr/bin/env python
#  _*_ coding:utf-8 _*_
#  @Time    :2018/12/4  14:50
#  @Author   :Kelake
#  @FileName :测试1.py

import random
import requests
import re
header = [{'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.76 Mobile Safari/537.36'},
          {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'},
          {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)'},
          {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1'},
          {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)'}]
# header 是用来伪装成浏览器发送请求，一般加上最好，header 信息可以通过浏览器查看，也可在网上搜索得到。
req = requests.get('http://www.biqukan.cc/book/20461/12592815.html',headers=header[random.randint(0, 4)])  # 向目标网站发送 get 请求
#req2 = requests.get('http://www.biqukan.cc/book/20461/12592815_2.html',headers=header[random.randint(0, 4)])
result = req.content
result = result.decode('gbk')  # 查看网页源代码 看到 charset=gbk，即网页是用的 gbk 编码，故要用 gkb 的编码方式来解码，否则中文就会乱码。
title_re = re.compile(r' <li class="active">(.*?)</li>')
text_re = re.compile(r'<br><br>([\s\S]*?)</div>')
title = re.findall(title_re,result)
text = re.findall(text_re,result)
text = text.split('\r\n')
text_1 = []
title = title[0]
print(title)
#print(result)