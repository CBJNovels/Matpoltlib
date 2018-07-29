from __future__ import(absolute_import, division,
                   print_function, unicode_literals)

try:
    #Python 2.x版本
    from urllib2 import urlopen
except ImportError:
    # Python 3.x版本
    from  urllib.request import urlopen
import json
import requests

try:
    json_url = 'http://raw.githubusercontent.com/muxuezi/btc/master/btc_close_2017.json'
    response = urlopen(json_url)
    print("下载成功")
except:
    print("下载失败")

#读取数据
req = response.read()
req_1 = requests.get(json_url)#下载获取

#将数据写入文件
with open('btc_close_2017.json', 'wb') as f:
    f.write(req)
with open('btc_close_2017.json', 'w') as f:
    f.write(req_1.text)

#加载json格式
file_urllib = json.loads(req) #json.loads()针对内存，json.load()针对本地文件
file_requests = req_1.json()
print(file_urllib)
print(file_requests)

#判定是否相等
print(file_urllib == file_requests)