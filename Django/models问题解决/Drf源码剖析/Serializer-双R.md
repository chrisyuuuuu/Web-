## Mixin

- 混合
- 在python代表的多继承的父类

### 属性操作

- setattr( key, value )
  - 动态添加属性
- getattr( key )
  - 获取属性
  - getattr( key, default_value )
  - 属性存在给值，不存在给默认值
- hasattr( obj, key )
  - 判定指定对象是否拥有指定属性



### RESTful

- Flask-RESTful
  - 轻量级
- Django-REST-Framework
  - 基于Django实现的RESTApi接口的重量级框架



### HelloDRF

- 安装
- 创建序列化器
  - serializers
- 创建视图集合
  - viewsets
- 创建路由
  - routers



### serializers

- BaseSerializer
- Serializer
  - 原生序列化
- ModelSerializer（多用）
  - 模型序列化
  - 企业开发中使用最多
- HyperLinkedModelSerializer
  - 模型序列化
  - 带超链接的
- ListSerializer



### 客户端向服务器提交

- form-data
  - 二进制提交
  - 文件上传混合提交
- x-www-form-urlencoded
  - key=value 提交
- raw
  - 原格式提交



### 参数处理

- Django中
  - GET可以处理请求参数，url上的
  - POST只能处理POST的请求参数
- Flask中
  - args
    - 可以处理请求参数，url上的
  - form
    - 可以处理请求体参数，包含POST，PUT，PATCH



### Request

- Django中默认是WSGIRequest
- DRF中Request
  - request.data



### Response

- 继承自Django
  - SimpleTemplateResponse
    - 继承HttpResponse
- rendered_content
  - 根据请求客户端属性，决定渲染返回的类型



### status

- 方便阅读
- 提升代码格调



### 包装API views

- FBV
  - 添加装饰器 @api_view
  - 添加了访问方法权限
- CBV
  - 修改继承，继承APIView
