### 运行流程
	- 开始--> Docer会在本机寻找镜像 --> 判断本机是否有这个镜像，找到，使用这个镜像运行
									--> 去docker hub下载，找到下载到本地运行，找不到抛错
									
### Docker运行原理
	- Docker是怎么工作的？
		DOcker是一个CS结构的系统，Docker的守护进程运行在主机上，通过Socket从客户端访问
		DockerServer 接收到Docker-client 的指令，就会执行这个命令
	- （客户端，客户端，客户端）命令    --linux服务器的后台守护进程--->  访问linux服务器的不同docker容器（类似虚拟机中不同端口的服务）