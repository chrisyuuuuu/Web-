### 构建docker镜像的构建文件!命令脚本！每个命令就是一层！
```
### 构建步骤
1. 编写一个dockerfile文件
2. docker build 构建为一个镜像
3. docker run 运行镜像
4. docker push 发布镜像（DockerHub,阿里云镜像仓库）


FROM centos
VOLUME ["volume01","volume02"]
CMD echo "----------end----------"
CMD /bin/bash

docker build -f 构建镜像路径 -t 

```

### Dockerfile的构建过程
	- 基础知识
	1. 每一个关键字指令都是大写
	2. 执行顺序从上到下
	3. ’#‘ 表示注释
	4. 每一个指令都会创建提交一个新的镜像层，并提交
	
	5. dockerfile 是面向开发的，我们以后要开发项目，做镜像，就需要编写dockefile
	6. dockerfile:构建了文件，定义了一切的步骤，源代码
	7. dockerimages:通过dockerfile构建生成镜像，最终发布和运行产品
	8. docker容器：镜像运行起来提供服务器
### Dockerfile 的指令
```
	FROM 指定基础镜像（这个镜像的妈妈）
	MAINTINER 指定维护者信息，镜像是谁写的 姓名+邮箱
	RUN  想要它干啥，加run即可，镜像构建的时候需要运行的命令
	ADD 给点创业资金，添加内容
	WORKDIR 镜像的工作目录
	VOLUME 挂载主机目录
	EXPOSE 指定对外端口
	CMD 指定这个容器启动要运行的命令
	ENTRUYPOINT 指定这个容器启动的时候要运行的命令，可以追加命令
	ONBUILD 当构建一个被继承Dockerfile的时候被运行
	COPY 将文件拷贝到镜像中
	ENV 构建的时候设置环境变量
	
```
### 实战测试
	- Docker Hub中99%镜像都是从这个基础镜像过来的FROM scratch ,然后配置需要的软件
	```
		cd ~
		mkdir dockerfile
		vim mydockerfile
			FROM centos
			MAINTAINER wangbq<wangbq@163.com>
			
			ENV MYPATH /usr/local 一进去就是工作目录
			WORKDIR $MYPATH
			
			RUN yum -y install vim
			
			EXPOSE 80
			
			CMD echo $MYPATH
			CMD echo "---end--"
			CMD /bin/bash
	
		docker build -f mydockerfile -t mycentos(自定义镜像名):0.1（tag） .
		docker run -it mycentos:0.1
		docker history
		
	```
### CMD 和ENTRYPOINT区别
```
	CMD 指定这个容器启动的时候要运行的命令，只要最后一个生效，可被替代
	ENTRUYPOINT 指定这个容器启动的时候，可以追加命令
	
	想要追加
		CMD:追加时会被完全替换 ls -a加-l ---> -l
		ENTRUYPOINT:追加时被替换需要替换的部分ls -a加-l --->ls -al
```













