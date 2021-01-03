1、下载

```
# https://www.python.org/downloads/release
sudo curl -O https://www.python.org/ftp/python/3.8.7/Python-3.8.7.tgz


```

2、安装pyenv

```
# 安装命令
curl -L https://github.com/pyenv/pyenv-installer/raw/master/bin/pyenv-installer | bash

# 错误解决- 打开 https://www.ipaddress.com/ 输入访问不了的域名
# sudo vim /etc/hosts
199.232.68.133 raw.githubusercontent.com
199.232.68.133 user-images.githubusercontent.com
199.232.68.133 avatars2.githubusercontent.com
199.232.68.133 avatars1.githubusercontent.com

# 常用命令
pyenv commands  查看pyenv命令
 
 
pyenv install --list    #查看可安装的python版本
pyenv versions          #查看已安装版本
pyenv version           #查看当前使用的python版本
pyenv install -v 版本号  #安装python
pyenv rehash            #刷新python已安装列表
pyenv uninstall 版本号   #删除python
 
pyenv virtualenv 已有版本环境名名 新版本环境名  #按已有版创建新的python环境（调用virtualenv,python3 自带了virtualenv,py2要自行装）
 
pyenv global 版本号     #设置当前全局python版本
pyenv local  版本号     #设置当前目录局部python版本，以后进入目录就会自动切换到这个版本
pyenv local --unset     #取消局部python版本设置,或者删除当前目录下的.python-version文件
 
```

3、安装虚拟环境

```
pip install virtualenv:虚拟环境
pip install virtualenvwrapper:管理虚拟环境
    mkdir .virtualenvs
   	find / -name virtualenvwrapper.sh
    vim .bashrc
    #python virtualenv
    export WORKON_HOME=/root/virtualenvs
    source /usr/share/virtualenvwrapper/virtualenvwrapper.sh
    mkvirtaulenv python2
    mkvirtaulenv python3 -p /usr/bin/python3
/home/rabbit/.pyenv/shims/python3.6
```

