import urllib
proxy = urllib.ProxyManager('http://localhost:3128/')
proxy.request('GET', 'http://google.com/')