### ORM操作
	- Http请求
		url -> 视图（模板+数据）
	- ORM 操作表
		- 创建表
		- 修改表
		- 删除表
	- ORM 操作行
		- 增删改查
	- ORM利用pymysql第三方工具连接数据库
	- MySQL
		- 默认连接mysql --> MySQLDB(修改django默认连接mysql的方式)
	- 默认SQLlite
### 准备工作
	1. 创建数据库
	2. 修改数据库配置
	3. 
		```
			import pymysql
			pymysql.install_as_MySQLdb()
		```
### ORM操作表
	1. 创建模型
	2. 注册app
	3. 创建数据库表
	```
		命令：
			python manage.py makemigrations
			python manage.py migrate
		null =True || default = 1	默认不为空
		ug = models.ForeignKey("Groupuser",null),已有数据的情况下增加一列
		默认生成ug_id的一列，生成一对多关系
		
	```
### ORM操作行
	```
		增
		类.objects.create(title="销售部"，password='')
		
		查
			models.类.objects.all()
			类-表，对象-一行数据
			返回值：querySet:列表,列表中有对象，每个对象就是一行数据
			
			加条件
				filter(id=1,title=2)-- where 和 and，多条件
					__gt= --- 大于
					__lt= --- 小于
		删除
			models.objects.filter(id=1).delete()
				```
		更新 models.objects.filter(id=2).update(title="公关部")
		
		class User(models.Model):
			u_name = models.CharField(max_length=32)
			u_password = models.CharField(max_length=256)
			潜在字段 blog_set
			
		class Blog(models.Model):
			b_title = models.CharField(max_length=32)
			b_content = models.CharField(max_length=256)
			b_user = models.ForeignKey('User',null=True)
			潜在字段 b_user_id
	
		ret = objects.all().values('id')
		返回值：列表中包含字典
		
		ret = objects.all().values_list('id')
		返回值：列表中包含元组
		
		获取多个数据
			all()
			filter()
				for后可以点
				循环跨表
			values('id','dict')
				for后[]取
				跨表values("id","ut__title")
			values_list()
				for()后[0],[1]
				
		分页
			分批获取数据
				objects.all()[:10]
				objects.all()[10:20]
			django
				result = all()
				paginator = Paginator(result,10)
				per_page,每页条目数量
				count 数据总个数
				num_pages 总页数
				page_range 总页数范围
				page 对象
				
				paginator.page(1) 获取第一页
				
				has_next
				next_page_number
				has_previous  是否有上一页
				object_list 分页之后的数据
				number 当前页
				paginator paginator对象
						
	```
	
	

	
	
	
	
	
	
	