### View剖析

- as_view
- 源码结构
  - http_method_names
    - 提供了八种请求方法
    - Django最多支持这八种请求
  - \__init__
    - 获取所有关键字参数，添加属性到对象中
  - as_view
    - classonlymethod 装饰器
      - classmethod
      - 类可以调用这个方式
      - 实例不能调用这个方法
    - 迭代关键字参数
      - key如果是http_method_names 中的，会报错
        - 关键字参数的key不能是请求方法
      - key如果在类中并不存在对应属性，也会报错
        - 关键字参数的key，必须是类的属性
    - 定义View
      - 构建自己的对象
      - 记录属性
      - 调用dispatch
  - dispatch
    - 判定请求方式是否是我们列表中
    - 如果是 根据请求方法获取对应属性
      - 获取到正常返回
      - 获取不到返回默认值 
        - http_method_not_allowed
    - 如果不在列表中
      - 直接返回http_method_not_allowed
  - http_method_not_allowed
    - 返回了HttpResponseNotAllowed
      - HttpResponse的子类
      - 状态码405
  - options
    - 请求方式


