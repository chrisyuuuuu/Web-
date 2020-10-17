### 防盗链图片下载
```
	# 有防盗链机制的图片下载
	url = 'http://fm.shiyunjj.com/2018/1535/2ipw.jpg'
	# urllib.request.urlretrieve(url, 'meinv.jpg')
	headers = {
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
		'Referer': 'http://www.mmjpg.com/',
	}
	# 构建请求对象
	request = urllib.request.Request(url=url, headers=headers)
	response = urllib.request.urlopen(request)
	with open('meinv2.jpg', 'wb') as fp:
		fp.write(response.read())
```
### 拼接请求参数 urllib.parse.urlencode(data)
```
import urllib.parse

name = '狗蛋'
pwd = '123456'
height = 180
url = 'http://www.baidu.com/index.html?'
# get参数都写到一个字典中
data = {
    'username': name,
    'password': pwd,
    'height': height
}

query_string = urllib.parse.urlencode(data)
print(query_string)

```