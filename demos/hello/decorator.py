import time,functools


def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("call %s():" % func.__name__)
        print("args = {}".format(*args))
        return func(*args, **kwargs)

    return wrapper

# @log def func: 等同于 func = log(func)
@log
def test2(p):
    print(test2.__name__ + " param:" + p)


test2("I'm a param2!")


def metric(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kw):
        time1 = time.time()*1000
        fn(*args, **kw)
        time1 = time.time()*1000-time1
        print('%s executed in %s ms' % (fn.__name__, time1))
        return fn(*args, **kw)
    return wrapper

# 测试
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y;

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z;

f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')