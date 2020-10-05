```
@stu.route('/selectstu/')
def select_stu():

    # 查询年龄小于16岁的学生的信息
    # 第一种查询的方式
    stus = Student.query.filter(Student.s_age < 16)
    # 第二种查询的方式
    # __lt__表示小于   __le__表示小于等于
    stus = Student.query.filter(Student.s_age.__lt__(16))

    # 查询年龄大于16岁的学生的信息
    # 第一种查询的方式
    stus = Student.query.filter(Student.s_age > 16)
    # 第二种查询的方式
    # __gt__表示大于   __ge__表示大于等于
    stus = Student.query.filter(Student.s_age.__ge__(16))

    # 查询年龄在16,17,20,23的学生的信息
    stus = Student.query.filter(Student.s_age.in_([16,17,20,23]))

    # 查询所有学生的信息
    # 第一种查询方法
    stus = Student.query.all()
    # 第二种查询方法
    sql = 'select * from student;'
    stus = db.session.execute(sql)

    # 按照id降序排列(注意：不能用：Student.query.all。order_by)
    # 因为：.all后  返回的是一个装有对象的列表，列表是不能排序的
    stus = Student.query.order_by('-s_id')

    # 按照id降序获取3个
    stus = Student.query.filter.order_by('-s_id').limit(3)

    # 获取年龄最大的学生的信息
    stus = Student.query.filter.order_by('-s_id').first()

    # offset(2)表示跳过2个数据   limit（3）表示截取3个信息
    stus = Student.query.filter.order_by('s_id').offset(2).limit(3)

    # 获取id等于24的学生
    # 第一种方法
    stus = Student.query.filter(Student.s_id==24)
    # 第二种方法(和Django 不同)
    stus = Student.query.get(24)


    # 查询多个条件（from sqlalchemy import and_,or_,not_ ）
    stus = Student.query.filter(Student.s_age==18,Student.s_name=='张三')
    # and_ 并且条件(和上一个的效果一样)
    stus = Student.query.filter(and_(Student.s_age==18,Student.s_name=='张三'))
    # or_或者条件
    stus = Student.query.filter(or_(Student.s_age==18,Student.s_name=='张三'))
    # not_ 非条件
return render_template('student_list.html', stus=stus)
```