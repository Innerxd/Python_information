# 函数和代码的复用
'''

# 函数的定义  调用
def fun(a,b):      # 形参
    s=a+b
    print(s)
fun(3,5)        #实参  位置传参

'''

'''
def fun(a,b=4):      # 形参 默认传参 必须在后面 def fun(a=4,b)错误
    s=a+b
    print(s)
fun(3,5)        #实参

def fun(a,b):      # 形参
    print(a)
    print(b)
fun(b=4,a=5)        #实参   关键字传参

def fun(*a):      # 形参
    print(a)
    print(type(a))
fun(1,2,3,4,5)        #实参   任意长度传参
'''

'''
# 变量的作用域  局部变量  全局变量

s = 3
def fun(a, b):
    global s            函数内部修改全局变量
    s = s + 5
    print(s)
fun(3, 5)
print(s)

'''
'''
#代码复用
def fun(a,b)
    s=a+b
fun(3,4)
# print(s)

def add(c,d)
    e=c*d
    # print(r)
add(3,5)
print(s)

'''
