```
FROM centos

VOLUME ["容器内目录","容器内目录2"]

CMD echo "----end---"
CMD /bin/bash

docker build -f docker文件路径 -t  本地路径 . 
docker image


创建docker文件 名字随意 建议Dockerfile
文件中的内容 指令大写 参数 每个指令就是一层镜像
多个容器间数据如何同步 --volume-from 容器卷技术

### 测试
	启动三个容器
	docker images 
	docker run -it --name docker01 镜像名称：tag
	docker run -it --name docker02 --volume-from docker01 镜像名称：tag
	docker attach 镜像id
	cd volume01
	touch docker01

	里应当dokcer02有docker01
	数据卷容器相当于继承
	停掉父类，并删掉，docker01和docker02的数据依旧存在，双向拷贝的概念
### 多个mysql实现数据共享

### 结论
容器间配置信息的传递，数据卷容器的生命周期一直持续到没有容器为止
一旦-v持久化到了本地，这时候本地的数据不会删除
docker run -d -p 3301:3306 -v /etc/mysql/conf.d/ -v /var/lib/mysql -e MYSQL__ROOT_PASSWORD=123456 --name mysql01 mysql:5.7
docker run -d -p 3310:3306 -e MYSQL__ROOT_PASSWORD=123456 --name mysql02 mysql:5.7 volume-from 	mysql:5.7
这个时候可以实现两个容器数据同步
	
```
