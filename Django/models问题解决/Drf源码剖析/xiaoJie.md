# Day06





### DRF源码剖析

- VIEW
  - CBV
- APIView
  - View子类
  - 封装了
    - Request
    - 转换
    - 版本
    - 认证
    - 权限
    - 节流
    - Response



### generics

- GenericAPIView
  - APIView
    - 封装了一系列对象操作
  - CreateAPIView
  - ListAPIView
  - ListCreateAPIView
  - RetrieveAPIview
  - UpdateAPIView
  - DestroyAPIView
  - RetrieveUpdateAPIview
  - RetrieveDestroyAPIView
  - RetrieveUpdateDestroyAPIView



### mixins

- 模型操作
- CreateModelMixin
- ListModelMixin
- RetrieveModelMixin
- UpdateModelMixin
- DestroyModelMixin



### 注册，登陆，数据级联

- 当默认实现调用存在冲突的时候，可以重写
  - 通过参数控制
- 修改存储过程
  - 序列化器修改
  - 在对象创建之前