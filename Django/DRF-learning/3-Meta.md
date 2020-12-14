```
class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        # 模型名称
        model = User
        # 序列化返回的字段
        fields = ('id', 'account_name', 'users', 'created')
        # 这个字段不返回
        exclude = ('users',)
        # 显示的深度，会让外键变为只读
        depth = 1
        # 默认只读,不接受用户修改  跟字段设置的read_only=True效果一样
        read_only_fields = ('account_name',)
        # 额外参数，如果字段已在序列化程序类中显式声明，则该extra_kwargs选项将被忽略。
        extra_kwargs = {"title": {"validators": [my_validate,]}}
```

