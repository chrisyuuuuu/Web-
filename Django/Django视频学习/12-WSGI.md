### django 请求声明周期
	- 中间件 - url - 视图
	- web框架的本质时socket
	- django里边没有socket,django用的别人的socket
	- 本地测试：sorckt + django 默认用到wsgiref 
	- 工作：uwsgi + django
	
### django
	- req:请求相关
	- res:字符串
### 约束
	- WSGI协议
		- socket, wsgiref,uwsgi
	- socket 服务端while循环，等待客户端连接
		- wsgiref 拿请求，解析，交给django
		- 你给我的当响应头，额外的响应体