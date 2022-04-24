# python 基本数据类型
# 使用type()查看数据类型
'''
a = 5.2+6j
a1 = a.real
print(a1,type(a1))
a2 = a.imag
print(a2,type(a2))
# 把a1转换成整型，a2转换成bool型
a1 = int(a1)
a2 = bool(a2)
print(a1,type(a1))
print(a2,type(a2))
'''

# 假定1号是周1，29号是第几周星期几
# 使用整除，求余
'''
a = 29
b = 7
# 第几周
c = a//b
# 第几天 
d = a%b
print(c,d)
'''

# 使用math.divmod(x,y)函数求出c1,d1
'''
# print(divmod(29,7))
c1,d1 = divmod(29,7)
print(c1,d1)
'''

# 四舍五入
'''
print(round(4.49))
print(round(4.50))
print(round(4.51))
'''

# pi
'''
import math
a = math.pi
print(a)
'''

# daydayup1
# 每天进步0.001，初始值为1，一年后进步到哪一程度
'''
dayup = pow(1.001,365)
# pow函数是幂运算
print(dayup)
daydayup = 1*(1+0.001)**365
print(daydayup)
# 每天退步0.001，初始值为1，一年后进步到哪一程度 round()取有效数字
daydaydown = 1*(1-0.001)**365
daydaydown = round(daydaydown,3) 
print(daydaydown)
print("这个是刷手机的，知识技能下降为：{:.3f}".format(daydaydown))
money = 5000*(1.01)**365
print("每天增值1%，一年后是：{:.3f}元".format(money))
'''

# 有5000元，每天增值1%，复利，一年后有多少钱（用函数计算）
'''
def daydayup(chushizhi,factor,days):
    dayup = chushizhi*(1+factor)**days
    return dayup
money = daydayup(5000,0.01,365)
print(money)
print(daydayup(1,0.01,365))
'''

# 每天退步factor，写成函数daydaydown
'''
def daydaydown(chushizhi,factor,days):
    daydown = chushizhi*(1-factor)**days
    return daydown
money = daydaydown(5000,0.01,365)
print(money)
'''

# 努力的话进步1%，休息退步1%，努力五天休息两天，基数假定为1，一年后是多少
daylast = 1
for tian in range(1,365+1):
    if tian%7 in [5,6]:
        daylast = daylast*(1-0.01)
    else:
        daylast = daylast*(1+0.01)
# 保留三位小数点
# print("{:.3f}".format(daylast))
# 保留三位有效数字
print(round(daylast,3))