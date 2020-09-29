# 列表 可作为队列使用
'''
>>> from collections import deque
>>> queue = deque(["Eric", "John", "Michael"])
>>> queue.append("Terry")           # Terry arrives
>>> queue.append("Graham")          # Graham arrives
>>> queue.popleft()                 # The first to arrive now leaves
'Eric'
>>> queue.popleft()                 # The second to arrive now leaves
'John'
>>> queue                           # Remaining queue in order of arrival
deque(['Michael', 'Terry', 'Graham'])
'''
# 列表表达式
# for
squares = [x**2 for x in range(10)]
# for if 
[(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]

# 元组不可赋值
# 字典
# 当同时在两个或更多序列中循环时，可以用 zip() 函数将其内元素一一匹配。
'''
>>> questions = ['name', 'quest', 'favorite color']
>>> answers = ['lancelot', 'the holy grail', 'blue']
>>> for q, a in zip(questions, answers):
'''

# 指定顺序循环， sorted() 函数，它可以在不改动原序列的基础上返回一个新的排好序的序列
# >>> basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
# >>> for f in sorted(set(basket)):
# ...     print(f)

# 比较传递
#  a < b == c 会校验是否 a 小于 b 并且 b 等于 c
