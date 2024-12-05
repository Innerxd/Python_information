

'''
# 序列类型
# 字符串 元组 列表
s='hello'
t=(1,2,3,4,5)
ls=[2,3,4,5]
print(id(s))
print(id(t))

'''

"""
#不可变数据
#元组定义的时候记得保留逗号
t=("py",123,(1,3),6,9)
t1=(1,)
print(type(t))

#print(len(t))       # 长度为 5
#打印 3
#print(t[2][1])
"""

"""
#列表可变
ls=[1,3,4,5,6]
print(id(ls))
ls[2]=8
print(id(ls))

ls=[3,45,(2,5,[["hello",6]]),"python"]
len(ls)
#打印出 "el"
ls[2][2][0][0][1:3]

ls=[1]
print(type(ls))

ls=[1,5,7,2,4]
#   7改成9
ls[2]=9
#4后面增加一个6  尾部添加
ls.append(6)
#删除2  remove直接是数字  pop是位置
#ls.remove(2)
ls.pop(3)

"""
'''
#   = 和 copy 不一样的
ls=[1,5,7,2,4]
# lt=ls
lt=ls.copy()
ls[1]=9
print(lt)


ls=[1,5,7,2,4]
# 1和5之间插入8      第一个是位置 的二个是数
ls.insert(1,8)

'''
"""
# 集合类型
# 集合是无序的

s={1,3,3,5,7,9}
len(s)      #5   从1开始，两个3算一个 重复的算一个


映射类型

d={"name":"你好","age":35}
# 字典的键必须是唯一且不可改变的  前面是键，后面是值可一样
#socre  60 加进去
d["score"]=60
print(d)

#修改  35  =>  25
d["age"]=25
print(d)
#age 35 删了
del d["age"]
print(d)

# 找到    你好
print(d["name"])
print(d.get("name"))
print(d)
"""
'''

'''
#如果要把无序的元组变成有序的列表
d={"张三":80,"北北":59,"密码":61}
print(list(d.items()))      #list转化