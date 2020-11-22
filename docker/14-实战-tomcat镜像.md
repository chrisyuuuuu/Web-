### 步骤
	1. 准备镜像文件tomcat压缩包，jdk的压缩包
	2. 编写dockerfile文件，官方命名 Dockerfile,build会自动寻找这个文件，不需要-f指定了
	```
		FROM centos
		MAINTAINER XXXXXXXXXX
		COPY readme.txt /ust/local/readme.txt
		
		ADD 压缩包 解压路径
		
		RUN yum -y install vim 
		
		ENV MYPATH /usr/local
		WORKDIR $MYPATH
		
		ENV JAVA_HOME /usr/local/jdk的压缩包1.8.0_11
		ENV CLASSPATH $JAVA_HOME/lib/dt.jar:$JAVA_HOME/lib/tools.jar
		ENV CATALINA_HOME /usr/local/apache-tomcat-9.0.22
		ENV CATALINA_BASH /usr/local/apache-tomcat-9.0.22
		ENV PATH $PATH:$JAVA_HOME/bin:$CATALINA_HOME/lib:$CATALINA_HOME/bin
		
		EXPOSE 8080
		
		CMD /usr/local/apache-tomcat-9.0.22/bin/startup.sh && tail -F /usr/local/apache-tomcat-9/bin/logs/catalina.out
	
	```
	3. 构建镜像
	4. 启动镜像
	5. 访问测试
	6. 发布
		- 注册docker账号
		- 确定账号可以登录
		- 在服务器提交我们的镜像
		- docker login -p  -u 
		
### 发布镜像到阿里云容器服务
	- 登录阿里云
	- 找到容器镜像服务
	- 创建命名空间
	- 创建容器镜像
	- 浏览阿里云