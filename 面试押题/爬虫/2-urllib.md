### urllib.request.urlopen(url)
```
	import urllib.request

	# 代码中的url必须是完整的url  最后的斜杠加上
	url = 'http://www.baidu.com/'

	# 向这个url发送请求
	response = urllib.request.urlopen(url)

	# print(response)
	# response有属性和方法来获取你想要的内容
	# 获取请求的url
	# print(response.url)
	# 获取状态码
	# print(response.status)
	# 获取响应头
	# print(response.headers)
	# 获取响应内容
	# 字节格式内容，二进制格式内容
	# print(type(response.read().decode('utf8')))

	'''
	字节格式和字符串格式之间的转化
	字符串格式转化为字节格式  encode('utf8')
	字节格式转化为字符串格式  decode('gbk')
	'''
	# 【注】read方法只能读取一次
	content = response.read()
	# 将响应内容写到文件中  r  w  a  
	with open('baidu.html', 'w', encoding='utf8') as fp:
		fp.write(response.read().decode('utf8'))

	# 按照字节格式写文件
	with open('baidu1.html', 'wb') as fp:
		fp.write(response.read())
```

### urllib.request.urlretrieve(url,文件名)
```
	import urllib.request

	# url = 'http://www.baidu.com/'
	# 直接将url对应的响应保存到指定的文件中
	# urllib.request.urlretrieve(url, 'baidu2.html')

	image_url = 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1542624895743&di=bb880ceab889055c32f905d3a8b032b1&imgtype=0&src=http%3A%2F%2Fb-ssl.duitang.com%2Fuploads%2Fitem%2F201302%2F17%2F20130217172228_VQrwX.thumb.700_0.jpeg'
	response = urllib.request.urlopen(image_url)
	with open('qizhi.jpeg', 'wb') as fp:
    fp.write(response.read())
```

### urllib.request.Request(url=url, headers=headers)
```
	import urllib.request

	# url = 'http://www.baidu.com/'
	# response = urllib.request.urlopen(url)

	'''
	# 伪装ua
	url = 'http://www.baidu.com/'
	# 定制请求头部的过程
	headers = {
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
	}
	# 构建请求对象
	request = urllib.request.Request(url=url, headers=headers)

	# 发送请求，得到响应
	response = urllib.request.urlopen(request)
	'''

	import random
	url = 'http://www.baidu.com/'
	ua_list = [
		'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
		'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0',
		'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
		'Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11'
	]
	# 构建请求对象，应该从上面的ua列表中随机一个ua出来
	ua = random.choice(ua_list)
	headers = {
		'User-Agent': ua,
	}
	request = urllib.request.Request(url=url, headers=headers)
	response = urllib.request.urlopen(request)

```