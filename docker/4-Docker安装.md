### 镜像（image）
	- docker镜像好比是一个模板，可以通过这个模板来创建服务，tomcat镜像 ====> run ===> tomcat1容器（提供服务器），通过这个镜像可以创建多个容器（最终服务运行或项目运行就是在服务中）
### 容器（container）
	- Dokcer利用容器技术，独立运行一个或一组应用，通过镜像来创建
	- 启动，停止，删除，基本命令
	- 容器就是简易的linux系统
### 仓库（repository）
	- 仓库就是存放镜像的地方
	- 仓库分为共有仓库和私有仓库
	- Docker Hub（默认是国外的）
	- 阿里云... 都是容器服务器（配置镜像加速）
	
### 安装（https://docs.docker.com/engine/install/ubuntu/）
	- 产看本地环境，uname -r  cat /etc/issue（查看ubuntu版本）
	- 卸载旧的版本
	- 需要的安装包
	- 设置镜像的仓库
	- 安装docker包 docker-ce 社区 docker-ee 企业版
	- 清除缓存 makecache fast
	- 启动docker docker version
	- 查看下载的镜像
		docker images
	- 卸载
		卸载依赖 containerd.ios
		删除资源 目录