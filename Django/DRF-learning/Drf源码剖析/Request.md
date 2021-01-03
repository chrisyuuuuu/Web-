### Request

- 第一个参数是Django中的Request
  - 并且作为自己的私有属性 _request
- 后续几个参数都是从APIView中获取的
- content_type
- stream
- query_params
- data
  - 解决POST，PUT，PATCH这些数据
- user
- auth
- successful_authenticator