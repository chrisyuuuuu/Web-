# flask


## 第三方插件
- 了解需求
- 寻找插件
- 准备使用
    - 安装
    - 初始化(manager需要持有app，接收参数，将参数传给app.run())
    - 调用

### 例子
```
  pip install flask-script（执行命令行参数）
  manager = Manager(app)

  if __name__ == 'main':
    manager.run()//manager不知道管理的是谁，能够接收命令行参数，不知道传递给谁
  python FlaskProject.py runserver -p 8000 
```

### 初步拆分
- settings
- views
- models
- manage(入口)
- app

- manage调用app,app加载
                  - 各种配置（settings）
                  - 初始化路由（views）
                  - ext(最后加载，否则出现循环引用，未初始化好)
- models没人知道

### 接着拆分
- manage
- 整个项目体系
  - 模块初始化（app)，__init__,包括app创建
    - 加载配置settings
    - 加载ext(数据库，缓存的)
    - 和外部对接，初始化路由（views）
      - 使用models

### 最后拆分-啥时候加载，怎么加载，避免循环引用
- manage
- Project
  - __init__
    - 先加载settings
    - 再ext
    - 最后加载router
      - 加载views
- app1
  - views
    - 加载models
- app2
  - views
    - 加载models
