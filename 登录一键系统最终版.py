import urllib.request
import urllib.parse

def denglv():
    name={
        'username':'15751837766',
        'domain':'CMCC',
        'password':'MTIzMzIx',
        'enablemacauth':'0'
        }
    name=urllib.parse.urlencode(name).encode('utf-8')
    



    headers1={
       'Accept': 'application/json, text/javascript, */*; q=0.01',
	'Accept-Encoding': 'gzip, deflate',
	'Accept-Language': 'zh-CN,zh;q=0.9',
	'Connection': 'keep-alive',
	'Host': 'a.nuist.edu.cn',
	'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36'
       }
    req=urllib.request.Request('http://a.nuist.edu.cn/index.php/index/login',data=name,headers=headers1)
    response=urllib.request.urlopen(req)
    html=response.read().decode('unicode-escape')
    print(html)

denglv()
        
