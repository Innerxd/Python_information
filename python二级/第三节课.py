# 程序控制结构
'''
# 单分支
<条件>        只要非零非空 都为真

if 8%2:
    print("考研吗")        #不执行
if 9%2:
    print("考研吗")         #执行


#二分支
#空格字符1   空字符串0
if " ":
    print("考研吗")
else:
    print("继续干饭")
'''

"""
#多分支结构
if 5<3:
    print("干什么")
elif "":
    print("干发明")
else:
    print("审判直接")
"""
'''
逻辑运算符
 if not 8%2==0 or 9%2==1:
     print("好久没")
'''
'''
#for 遍历循环
#while 条件循环

for i in "python":
    print(i)
for i in "123456":
    print(i)
# range 拿到数字
for i in  range (1,7):
    print(i)
    
# break  跳出整个循环
# continue  结束这一次循环
#range(start,end,step)表示一个从start开始，到end结束，步长为step的区间
for i in  range (1,7):
    # if i==1:   #打断后面else
    #     break
    print(i)
else:
    print("nhao")

data =input()
while data:
    data=input()
    print("hello")


# 列表推导式
ls=[]
#依次添加1，2，3，4
for i in range(1,5):
    ls.append(i)
print(ls)

print([i for i in range(1,5)])

# 列表推导式
ls=[]
for i in range(1,5):
    if i>2:
        ls.append(i)
    else:
        ls.append(o)
print(ls)

print([i if i>2 else 0 for i in range(1,5)])
        

'''

"""
try:
    n = eval(input("请输入数字！"))
    print(n + 2)
except:
    print("不是数字")
  ls = [111, 222, 333, 444]
lt = [999, 777, 555, 333]
s = 0
for i in range(len(lt)):
    s = s + ls[i] * lt[i]
    print(s)  
"""


L = 'abcd'
def f(x, result=['a', 'b', 'c', 'd','e']):
    if x:
        result.remove(x[-1])
        f(x[:-1])
    return result


print(f(L))
