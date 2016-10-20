#coding=utf-8
import urllib2
#urllib2用一个Request对象来映射你提出的http请求
req = urllib2.Request('http://www.baidu.com')
#通过调用urlopen并传入request对象，将返回一个相关请求response对象
response = urllib2.urlopen(req)
#这个应答对象如同一个文件对象，可以在response中调用read()
the_page = response.read()
print the_page
