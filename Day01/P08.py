#coding=utf-8

from urllib2 import Request, urlopen,URLError,HTTPError

req = Request('http://bbs.csdn.net/callmewhy')

try:
	response = urlopen(req)
except HTTPError as e:
	print 'The server couldn\'t fullfill the request.'
	print 'Error code:',e.code

except URLError as e:
	print 'We failed to reach a server.'
	print 'Reason:',e.Reason

else:
	print 'No exception was raised.'