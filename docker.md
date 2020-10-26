### docker 在不同环境中搬运，网络仓库中搬运（别人开发的软件在自己的电脑运行，忽略支持问题）
1. 安装
	apt-get install docker
	curl -fsSL XXX --mirror Aliyun	
2. docker换源
3. docker基本命令
	docker build -t xxx
	docker images
	docker run 镜像名
	docker ps -a 查看运行之中的容器
4. Dockerfile
	知道docker打包
	FROM 指定运行环境
	WorDIR 指定工作目录
	COPY 拷贝命令 build开辟新计算机，里边什么也没有，通过copy拷贝代码
	RUN 预运行命令 指定运行包
	CMD CMD运行指令
	vim dockerfile
	FROM python:3.7
	WORKDIR /fruit
	COPY fruit .
	RUN pip install -r requirements.txt
	CMD['python',"fruit.py"]
	
5. 将水果分类器进行docker分装
	- 项目文件夹
	- Dockerfile
	- 建立docker镜像
	- 根据docker镜像运行docker容器
	- 启动/停止容器
	docker --version
6. 打包
	- dockers build -t fruit(名称) .(路径) 
7. docker sudo images
8. sudo docker run fruit
9. docker包装nginx
	搜索镜像 docker search nginx
	启动(下载) docker pull nginx:9.0
	docker images
	docker run -d(后台) --name nginx01(容器命名) -p(宿主端口) 3334:80 nginx
	linux的端口 容器端口
	进入容器 docker exec -it 	nginx01 /bin/bash
	docker stop 镜像名
10. 



	