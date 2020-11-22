**如何判断session过期**
	- session不存在则过期
如何判断cookie过期
	- 当一个请求url的协议、域名、端口三者之间任意一个与当前页面url不同即为跨域
实现
**COOKIES**
	  客户端会话技术
		数据都存储在客户端
		特性
		  不能跨浏览器，不能跨域名，默认请求会携带本站的所有cookie
		  存储结构key-value,支持过期，过期怎么做的?有一个属性时间，调用的时候看看到么到时间（懒过期）
		  相对不安全，容易被伪造
		**session**
	  服务端会话技术
		服务端记客户端记不住，数据都存储在服务端
		session不能脱离cookie存在
		特性
		  相对安全
		  将数据的钥匙存在cookie中
		  存储结构key-value
		  支持过期
		Django中，单台设备处理请求有上限（1w）,存在内存共享困难
		  将session数据持久化到ORM中
		token
	  服务端会话技术
		自定义的session
		如果用在常规的Web中，和session就没什么区别
		主要解决的是不支持cookie的客户端

1. cookie的工作原理是：
	由服务器产生内容，浏览器收到请求后保存在本地；
	当浏览器再次访问时，浏览器会自动带上Cookie，这样服务器就能通过Cookie的内容来判断这个是“谁”了
2. ### 获取Cookie
    request.COOKIES['key']
    request.COOKIES.get('key') # 普通的cookie
    request.get_signed_cookie('key', default=RAISE_ERROR, salt='', max_age=None)  #加密的cookie
    
	### 设置Cookie,都需要一个HttpResponse
		rep = HttpResponse(...)
		rep ＝ render(request, ...)
		rep ＝ redirect(request, ...)
			
		rep.set_cookie(key,value,...)  # 设置普通的cookie
		rep.set_signed_cookie(key,value,salt='加密盐',...) # 设置加密后的cookie
	
	
	​	
	### set_cookie() 参数说明:
		key, 键
		value='', 值
		max_age=None, 超时时间
		expires=None, 超时时间(IE requires expires, so set it if hasn't been already.)
		path='/', Cookie生效的路径，/ 表示根路径，特殊的：根路径的cookie可以被任何url的页面访问
		domain=None, Cookie生效的域名
		secure=False, https传输
		httponly=False 只能http协议传输，无法被JavaScript获取（不是绝对，底层抓包可以获取到也可以被覆盖）
	
	
	​					   
	### 删除Cookie
		def logout(request):
			rep = redirect("/login/")	#得到HttpResponse对象
			rep.delete_cookie("user")  # 删除用户浏览器上之前设置的user的cookie值
			return rep 
3. Session
	### session的流程:
		1. 浏览器向服务发送请求,
		2. 服务器设置session,并保存在服务端的上(以数据库,文件,缓存等形式保存) . 生成一个session_id .以键值对的形式{session_id:{'键':'值'}}
		3. 服务器将sessionID发送给浏览器, 这个sessionID是服务器生成的.并通过cookie保存浏览器本地
		4. 当其他页面提交请求时,携带新的sessionID.
	
	### cookie 流程:
		1. 服务端发送一个cookie信息
		2. 本地浏览器保存,
		3. 发起其他请求时,携带cookie
		4. 服务器进行校验,从cookie获取一些信息 ,如:登录状态,记录用户浏览信息
	
	Cookie虽然在一定程度上解决了“保持状态”的需求,
		由于Cookie本身最大支持4096字节
		Cookie本身保存在客户端，可能被可能被拦截或窃取
	我们可以给每个客户端的Cookie分配一个唯一的id，这样用户在访问时，通过Cookie，服务器就知道来的人是“谁”。
	然后我们再根据不同的Cookie的id，在服务器上保存一段时间的私密资料，如“账号密码”等等。
	
	# 获取、设置、删除Session中数据
		request.session['k1']
		request.session.get('k1',None)
		request.session['k1'] = 123
		request.session.setdefault('k1',123) # 存在则不设置
		del request.session['k1']


	# 所有 键、值、键值对
		request.session.keys()
		request.session.values()
		request.session.items()   


	# 会话session的key
		request.session.session_key


	# 将所有Session失效日期小于当前日期的数据删除
		request.session.clear_expired()
	
	# 检查会话session的key在数据库中是否存在
		request.session.exists("session_key")
	
	# 删除当前会话的所有Session数据
		request.session.delete()
		
	### Django中默认支持Session，其内部提供了5种类型的Session供开发者使用。
		#1. 数据库Session
			SESSION_ENGINE = 'django.contrib.sessions.backends.db'   # 引擎（默认）
	
		#2. 缓存Session
			SESSION_ENGINE = 'django.contrib.sessions.backends.cache'  # 引擎
			SESSION_CACHE_ALIAS = 'default'                            # 使用的缓存别名（默认内存缓存，也可以是memcache），此处别名依赖缓存的设置
	
		#3. 文件Session
			SESSION_ENGINE = 'django.contrib.sessions.backends.file'    # 引擎
			SESSION_FILE_PATH = None                                    # 缓存文件路径，如果为None，则使用tempfile模块获取一个临时地址tempfile.gettempdir() 
	
		#4. 缓存+数据库
			SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'        # 引擎
	
		#5. 加密Cookie Session
			SESSION_ENGINE = 'django.contrib.sessions.backends.signed_cookies'   # 引擎


​			
​			
​			
​			
		##### 其他公用设置项：
			SESSION_COOKIE_NAME ＝ "sessionid" # Session的cookie保存在浏览器上时的key，即：sessionid＝随机字符串（默认）
			SESSION_COOKIE_PATH ＝ "/"            # Session的cookie保存的路径（默认）
			SESSION_COOKIE_DOMAIN = None          # Session的cookie保存的域名（默认）
			SESSION_COOKIE_SECURE = False         # 是否Https传输cookie（默认）
			SESSION_COOKIE_HTTPONLY = True        # 是否Session的cookie只支持http传输（默认）
			SESSION_COOKIE_AGE = 1209600          # Session的cookie失效日期（2周）（默认）
			SESSION_EXPIRE_AT_BROWSER_CLOSE = Fals# 是否关闭浏览器使得Session过期（默认）
			SESSION_SAVE_EVERY_REQUEST = False    # 是否每次请求都保存Session，默认修改之后才保存（默认）
		　　
		# 删除当前的会话数据并删除会话的Cookie。
			request.session.flush() 
			这用于确保前面的会话数据不可以再次被用户的浏览器访问
			例如，django.contrib.auth.logout() 函数中就会调用它。
	
		# 设置会话Session和Cookie的超时时间
			request.session.set_expiry(value)
				* 如果value是个整数，session会在些秒数后失效。
				* 如果value是个datatime或timedelta，session就会在这个时间后失效。
				* 如果value是0,用户关闭浏览器session就会失效。
				* 如果value是None,session会依赖全局session失效策略。
3. token(UUID)
	　	在settings中添加如下配置　

			INSTALLED_APPS = [
				......
				......
				'rest_framework.authtoken'
				......        
			]
			REST_FRAMEWORK = {
				'DEFAULT_AUTHENTICATION_CLASSES': (
					'rest_framework.authentication.SessionAuthentication',
					'rest_framework.authentication.TokenAuthentication',
				)
			}
		1.在代码中创建Toke
			from rest_framework.authtoken.models import Token
			from django.contrib.auth.models import User
			from rest_framework import permissions
			
			token = Token.objects.create(user=...)
			print token.key
	　  2.在接口中认证用户
		    class DoingView(views.APIView):
				permission_classes = (permissions.IsAuthenticated,)
				def get(self,request):
				   doning....
		3.前端请求参数
	　　　前端请求时需要在headers中带上如下参数，例如
	　　　“Authorization”：“Token c4742d9de47d2cfec1dbe5819883ce6a3e4d99b”
			