### 1.Celery是什么？参考-http://cnblogs.com/pyedu/p/12461819.html
	- Celery是一个简单、灵活且可靠的，处理大量消息的分布式系统，专注于实时处理的异步任务队列，同时也在支持任务调度
	- 分布式：将一个系统的不同组件（web服务器，web应用，数据库）架构在不同的服务器上，不同服务器的不同组件之间通过消息队列的方式实现协调工作，用户访问多台和一台感知一样
### 2.架构组成
	- 消息中间件
	- 任务执行单元
	- 任务结果存储
### 3.在同一时段出现100个订餐者，进程+协程可解决

### 4.结构
	- Django-生产者（user）：连接rabbitMQ,创建队列，向指定的队列插入数据
	- rabbitMP/Reids-消息中间件，消息队列
	- clery-任务执行单元-消费者：连接rabbitMQ,创建队列，监听队列，callback(内部实现异步请求)
	- last result store 任务结果存储
### 5.使用场景
	- 异步任务
		- 将耗时操作任务提交给Celery去异步执行，比如发送短信，邮件，消息推送，音视频处理等，
	- 同步任务
		- 定时执行某件事情，比如数据统计
### 6.优点
	- 使用维护简单，不需要配置文件
	- 高可用，worker和client网络连接丢失或失败时，自动进行重试，
	- 快速，单个的Celery可每分钟处理百万级的任务，并且只有毫秒级 的往返延迟
	- 灵活，几乎每个部分可扩展应用，序列化，日志记录，broker传输
### 7.我们要做哪些事？
	- 启动redis
	- 消费者
		- 定义异步任务（运用celery语法定义发短信，邮件等）函数
		- 监听异步任务
	- 生产
		- delay方法
### 8、简单案例
```
	#1.安装celery
	pip install -u celery
	#2. 创建异步执行文件
	import clery
	import time

	backend='redis://127.0.0.1:6379/1'
	broker='redis://127.0.0.1:6379/2'
	cel=celery.Celery('test',backend=backend,broker=broker)
	@cel.task
	def send_email(name):
		print("向%s发送邮件..."%name)
		time.sleep(5)
		print("向%s发送邮件完成"%name)
		return "ok"
	# 3.启动celery worker -A celery_app_task -l info

```