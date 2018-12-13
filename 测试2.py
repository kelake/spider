#! /usr/bin/env python
#  _*_ coding:utf-8 _*_
#  @Time    :2018/12/4  17:42
#  @Author   :Kelake
#  @FileName :测试2.py

import random
import requests
import re

header = [{'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.76 Mobile Safari/537.36'},
          {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'},
          {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)'},
          {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1'},
          {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)'}]

# header 是用来伪装成浏览器发送请求，一般加上最好，header 信息可以通过浏览器查看，也可在网上搜索得到。

req1 = requests.get('http://www.biqukan.cc/book/20461/12592815.html',
                    headers=header[random.randint(0, 4)])  # 向目标网站发送 get 请求
req2 = requests.get('http://www.biqukan.cc/book/20461/12592815_2.html', headers=header[random.randint(0, 4)])
result1 = req1.content
result1 = result1.decode('gbk')  # 查看网页源代码 看到 charset=gbk，即网页是用的 gbk 编码，故要用 gkb 的编码方式来解码，否则中文就会乱码。
result2 = req2.content
result2 = result2.decode('gbk')
title_re = re.compile(r' <li class="active">(.*?)</li>')  # 取出文章的标题
text_re = re.compile(r'<br><br>([\s\S]*?)</div>')  # 由于正文部分有很多的换行符，故要使用 [\s\S]
title = re.findall(title_re, result1)  # 找出标题
text1 = re.findall(text_re, result1)  # 找出第第一部分的正文
text2 = re.findall(text_re, result2)  # 找出第第二部分的正文
title = title[0]  # 由于返回的 title 是列表，故取出列表中的第一项
print(title)  # 打印出标题
text1.append(text2[0])  # 把正文两个部分添加到同一列表中，方便处理
text1 = '\r\n'.join(text1)  # 把两部分的正文连接成同一个个字符串
text1 = text1.split('\r\n')  # 把字符串按照换行符分割
text_1 = []  # 添加一个空列表，用来装处理后的正文
for sentence in text1:
    sentence = sentence.strip()  # 去掉每一句两边的空格
    if ' ' in sentence:
        sentence = sentence.replace(' ', '')  # 去掉句子中的  
        if '<br />' in sentence:
            sentence = sentence.replace('<br />', '')  # 去掉句子中的 <br />
            text_1.append(sentence)
        else:
            text_1.append(sentence)
    elif '<br />' in sentence:
        sentence = sentence.replace('<br />', '')
        text_1.append(sentence)
    elif '-->><p class="text-danger text-center mg0">本章未完，点击下一页继续阅读</p>' in sentence:
        sentence = sentence.replace(r'-->><p class="text-danger text-center mg0">本章未完，点击下一页继续阅读</p>',
                                    '')  # 去掉 -->><p class="text-danger text-center mg0">本章未完，点击下一页继续阅读</p>
        text_1.append(sentence)
    else:
        text_1.append(sentence)
count = text_1.count('')  # 统计列表中的空字符串
for i in range(count):
    text_1.remove('')  # 移除所有的空字符串
for sentence in text_1:
    print(sentence)  # 打印出所有的正文
