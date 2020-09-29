# 这是装饰函数
def timer(func):
  def wrapper(*args, **kw):
    t1=time.time()
    # 这是函数真正执行的地方
    func(*args, **kw)
    t2=time.time()

    # 计算下时长
    cost_time = t2-t1 
    print("花费时间：{}秒".format(cost_time))
  return wrapper

import time

@timer
def want_sleep(sleep_time):
  time.sleep(sleep_time)

want_sleep(10)


# 带参数的
@say_hello("china")
def chinese():
  print("我来自中国。")

@say_hello("america")
def american():
  print("I am from America.")

def say_hello(contry):
  def wrapper(func):
    def deco(*args, **kwargs):
      if contry == "china":
        print("你好!")
      elif contry == "america":
        print('hello.')
      else:
        return

      # 真正执行函数的地方
      func(*args, **kwargs)
    return deco
  return wrapper


