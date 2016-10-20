#coding=utf-8

import urllib
import urllib2

data = {
	'name':'WHY',
	'location':'SDU',
	'language':'Python'
}

url_values = urllib.urlencode(data)

print url_values

# name=Somebody+Here&language=Python&location=Northampton
url = 'http://www.example.com.example.cgi'
full_url = url+'?'+url_values
# req = urllib2.Request(full_url)
response=urllib2.urlopen(full_url)
