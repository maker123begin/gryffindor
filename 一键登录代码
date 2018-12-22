import urllib.request
import urllib.parse
def denglv():
    
    headers={
       'Accept': 'application/json, text/javascript, */*; q=0.01',
	'Accept-Encoding': 'gzip, deflate',
	'Accept-Language': 'zh-CN,zh;q=0.9',
	'Connection': 'keep-alive',
	'Host': 'a.nuist.edu.cn',
	'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36'
    }
    my_data = {
     'username':'15751837766',
    'domain':'CMCC',
    'password':'MTIzMzIx',
    'enablemacauth':'0'
    }
    my_data=urllib.parse.urlencode(my_data).encode('utf-8')
    url3='http://a.nuist.edu.cn/index.php/index/login'
    z=urllib.request.Request(url3,data=my_data,headers=headers)
    a=urllib.request.urlopen(z)
    
denglv()
    
    
    
