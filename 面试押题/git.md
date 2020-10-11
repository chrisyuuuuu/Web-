//情形一、前提:远程未存在该分支，内容:本地提交(本地)->
		master合并并push(master)->将本地分支在云端存储(本地)
git add .(login)
git commit -m ''(login)
git checkout master
git merge login
git push

//把本地分支在云端存储
git checkout login
git push -u origin login


//情形二、前提:远程未存在该分支，内容:本地提交(本地)->
		将本地分支在云端存储(本地)->master合并并push(master)
//情形：未创建本地分支，直接在master分支写了，将master分支迁移到新分支
git branch
git checkout -b user（user）
git add .（user）
git commit -m '完成用户管理开发'（user）

* 显示user分支,推送到云端（第一次）
git branch（user）
git push -u origin user（user）

| 合并到master
git checkout master（master）
git merge user(在master分支上合并user分支)（master）

| 把本地master分支代码推送到云端
git push（master）


情形三：正常情形，前提:远程未存在该分支，内容:本地提交(本地)->
		将本地分支在云端存储(本地)->master合并并push(master)
git  checkout -b rights
git push -u origin rights

git add . 
git commit
git push

git checkout master
git merge rights
git branch
git push
