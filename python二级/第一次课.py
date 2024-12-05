print("你好呀, 我叫赛利亚")
# 真的十七  注释

'''
if 5 > 3:
    print("你好\n北北！")  #缩进
'''

# a=3   变量  字母 数字（不能开头）下划线 中文    不能是关键字
# 表达式 赋值语句 引用

# @基本的输入输出函数
n = eval(input())
print(n + 3)  # n是字符串，不能直接使用
# eval()  去除双引号

print(2, end="+")
print(3, end="\n")
#2+3

# 数字类型  整数 浮点数 复数
# 不确定尾数  print(0.1+0.2)   0.300000004
# 复数 4+4j    4是浮点数 4.0

'''
n=3+4j
print(n.real)       # 返回实部 发现是浮点数 3.0
'''
"""
abs(-10)        10
abs(3+4j)       5.0
4/2     2.0         / 号结果一定是浮点数
10//3   3   取整
10%3    1   取余

divmod(10,3)      3 1 取整取余的结果
2**3    8
pow(2,3)    8

round(1.2)  1
round(3.1415,1)     3.1
round(3.5)     4
round(4.5)      4       小数点前面 奇进 偶不进
max(3,5,6)      6

#索引
s="python"
#  "h"
print(s[3])
#切片
# ”th"  左开右闭
print(s[2:4])
#"otp"  倒着跳
print(s[-2:-7:2])       #-2到-7 跳两个
"""

'''
格式化字符串
s="{}计算机考试考了{}分".format("北北"，"59")

name=input()
score=input()
s="{}计算机考试考了{}分".format("name"，"score")
print(s)
括号里面是分割的对象
分割得到的数据是列表
s="bj tj sh cq"
ls=s.split("")
print(ls)

s="$a$d$v$$$"
s=s.strip("$")
从左或从右依次删除指定字符,遇到别的停止
print(s)        a$d$v

print('2'+'3')     23字符
print()
in float str
'''
