# 作用域和明敏空间
# 私有变量
  # 命名：带有一个下划线的名称
  # 使用范围，避免名称与子类所定义的名称相冲突
  #  
# 迭代器，大多数容器对象都可以使用 for 语句
  # 作用
  # '''
  #  迭代器的使用非常普遍并使得 Python 成为一个统一的整体。 
  #  在幕后，for 语句会在容器对象上调用 iter()。 
  #  该函数返回一个定义了 __next__() 方法的迭代器对象，此方法将逐一访问容器中的元素。 
  #  当元素用尽时，__next__() 将引发 StopIteration 异常来通知终止 for 循环。 
  #  你可以使用 next() 内置函数来调用 __next__() 方法；这个例子显示了它的运作方式
  # '''
class Reverse:
    """Iterator for looping over a sequence backwards."""
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]
'''
>>> rev = Reverse('spam')
>>> iter(rev)
<__main__.Reverse object at 0x00A1DB50>
>>> for char in rev:
...     print(char)
...
m
a
p
s
'''

# 生成器
# 作用：用于创建迭代器的简单而强大的工具,自动创建 __iter__() 和 __next__() 方法,当生成器终结时，它们还会自动引发 StopIteration。
# 要返回数据时会使用 yield 语句。 每次对生成器调用 next() 时，它会从上次离开位置恢复执行（它会记住上次执行语句时的所有数据值）
def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]
'''
>>> for char in reverse('golf'):
...     print(char)
...
f
l
o
g
'''

# 对象方法，静态方法，类方法
class SeniorTestingEngineer:
    #属性--只能对象来调用self.salary
    work_year=3
    salary=15000
    #行为 函数

    #self对象方法
    def coding(self,language,rows):#self（不能缺少）用来标记这个方法是对象方法，这个方法只能对象来调用
        print('{0}代码一级棒，一天写{1}行代码'.format(language,rows))
        print('工作年限是{0}，月薪是{1}'.format(self.work_year,self.salary))#用对象来调用属性值

    @staticmethod#静态方法：是类中的函数，不需要特意创建对象来调用，当然也可以创建对象调用
    def do_mysql(name):
        print('数据库一级棒')
        # print('工作年限是{0}，月薪是{1}'.format(self.work_year,self.salary))#静态方法无法调用属性值,因为没有对象，AttributeError: 'str' object has no attribute 'work_year'
          

    @classmethod#类方法
    def do_linux(cls):#传一个类名进来
        print('linux一级棒')
        print('工作年限是{0}，月薪是{1}'.format(cls.work_year,cls.salary))#类方法必须用类名来调用属性值

    def do_auto_testing(self):
        print('自动化测试一级棒')
# 静态方法，类方法，对象方法 <==> 类、对象
s = SeniorTestingEngineer()
# 对象调用类方法
s.do_linux() #linux一级棒\n工作年限是3，月薪是15000 
# 对象调用静态方法
s.do_mysql('haha') # 数据库一级棒
# 对象调用对象方法
s.coding('js',10)# js代码一级棒，一天写10行代码
SeniorTestingEngineer.coding('s',1,2)

# 注意：使用静态方法，不能用self,访问类变量和实例变量
# 静态方法：不需要定义实例即可使用这个方法。另外，多个实例共享此静态方法。 
#  类方法：:方法的第一个参数都是类对象（cls）而不是实例对象



