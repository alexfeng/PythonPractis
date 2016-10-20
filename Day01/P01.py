# coding=utf-8

import urllib2 

#使用urllib2组件来抓取网页，以urlopen函数的形式提供了一个非常简单的接口。
response = urllib2.urlopen('http://baidu.com')
html = response.read()
print html