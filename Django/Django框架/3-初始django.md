- Django程序目录
	- mysite
		- mysite 
			- settings.py
			- url.py
			- wsgi.py  用于定义django用的socket,wsgiref,uwsgi
		- App
			
- 参数request
- 返回格式 HttpResponse()

- templates:
	- 配置：settings.py中路径的配置
	- 使用：render(request,'*.html')
- statics:
	- 配置：settings.py中路径的配置
		- STATIC_URL = '/static/',static---href对应的前缀static，href= "/static/commposee.css"
			STATICFILES_DIRS = (
				os.path.joing(BASE_DIR,'sta'), sta-目录
			)
	- 使用：样式 <link rel="stylesheet" href= "/static/commposee.css">
	
### 创建project项目步骤
	- 创建project
	- 配置
		- 模板路径
		- 静态文件路径
	- 额外配置
		- MODDLEWARE
			- 注释 csrf
### templates
	- form 
		- 表单填完提交（submit）到哪，method="POST" action = "/login/",找login的url
		- input 中的name相当于 key
			- 对应request.POST[name] | request.POST.get()
		- {{特殊字符需要传值}}--- render(request,'*.html'，{“msg”：“ok”})
### url的对应关系
	- /login/   login函数
	- def login(request):
		- request.method
		- request.GET
		- request.POST
		- HttpResponse
		- render
		- redirect
	- GET请求，值只在url中,请求头的url
	- POST请求，值在request.GET和request.POST,请求体
		- action="/login/?page=3"
### 模板引擎的特殊标记
	```
	login.html
		{{name}}
	# 显示单个
	users.0 users.1
	user_dict.k1 user_dict.k2
	
	# 循环
	{% for item in users %}
		<h3>{{item}}</h3>
	{% endfor %}
	# 跳转 a 
	<td><a href = "/del/？nid={{item.nid}}">删除</a></td>
	
	def login(request):
	
		return render(request,'.html',{"name":"ok",
										"users":["",""],
										"user_dict":{
												'k1':v1,
												'k2':v2
											}
										})
	```
	
	
	
	
	
	
	
	
	
	
	