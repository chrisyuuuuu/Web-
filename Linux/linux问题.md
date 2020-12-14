1. 关于Ubuntu中Could not get lock /var/lib/dpkg/lock解决方案
	https://www.cnblogs.com/yun6853992/p/9343816.html
2. E: Unable to locate package open-server
	https://blog.csdn.net/ystyaoshengting/article/details/101175939
3. pycharm 激活
	https://blog.csdn.net/weixin_30216561/article/details/99031544
	http://idea.medeming.com/jihuoma/
4.pycharm 添加环境变量
	修改环境变量
	　　sudo vim /etc/profile
	在最后一行添加 export PATH=~/Downloads/pycharm-community-2017.3.3/bin:$PATH
	重启生效
	在命令行输入pycharm.sh就发现pycharm可以直接运行了，其他环境变量类似
5. 装有道
	sudo dpkg -i youdao-dict_1.1.0-0-ubuntu_amd64.deb
	sudo apt-get install tesseract-ocr
	sudo apt-get -f install
	sudo dpkg -i youdao-dict_1.1.0-0-ubuntu_amd64.deb
6. 此虚拟机似乎在使用
	删除掉.lck文件夹

7. 全局配置虚拟环境
	->apt install virtualenv
	->apt install virtualenvwrapper
	->mkdir virtualenvs
	->find / -name virtualenvwrapper.sh 
	->vim .bashrc
	->最后添加 
	  #python virtualenv
	  export WORKON_HOME=/root/virtualenvs
	  source /usr/share/virtualenvwrapper/virtualenvwrapper.sh
	  /usr/share/virtualenvwrapper/virtualenvwrapper.sh

	->source .bashrc
	->mkvirtualenv python2
	->deactivate
	->mkvirtualenv python3 -p /usr/bin/python3

	遇到问题：https://www.it610.com/article/1294625073335967744.htm（pip配置）
		使用虚拟环境virtualenv 创建虚拟环境出现PermissionError: [Errno 13] Permission denied:
		解决办法：将目录及其文件的所有者改为当前用户

		解决命令：sudo chown -R 当前用户 待更改用户的目录/
		当前用户查看命令：whoami
	使用pip安装时出现pip._vendor.requests.exceptions.HTTPError: 404 Client Error: Not Found for url:的解决方法
		https://www.kanzhun.com/jiaocheng/500894.html
8. 安装虚拟环境- sudo virtualenv -p /usr/bin/python2.7 appenv3

