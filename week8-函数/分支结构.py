# # 利用循环，分支结构完成下面内容
# # 实现90分以上A 80分以上B 70分以上C 60分以上D 59分以下E
# # 输入百分制分数，输出等级
# while 1:
#     score = eval(input("请输入百分制分数(按q退出):>"))
#     if score >= 0 and score <= 100:
#         if score >= 90:
#             print(f"{score}分，等级为A")
#         elif score >= 80:
#             print(f"{score}分，等级为B")
#         elif score >= 70:
#             print(f"{score}分，等级为C")
#         elif score >= 60:
#             print(f"{score}分，等级为D")
#         else :
#             print(f"{score}分，等级为E")
#     aaa = input("是否继续，想退出循环，请按q，继续按任意键:>")
#     if aaa == "q":
#         break

# # 把成绩-等级转换功能封装成一个函数 zhuanhuan(分数)，输出等级
# def zhuanhuan():  # 分数判断
#     score = eval(input("请输入百分制分数(按q退出):>"))
#     if score >= 90:
#         level = "A"
#     elif score >= 80:
#         level = "B"
#     elif score >= 70:
#         level = "C"
#     elif score >= 60:
#         level = "D"
#     else :
#         level = "E"
#     print(f"分数是{score},等级是{level}")

# def jixu():  # 是否继续
#     aaa = input("是否继续，想退出循环，请按q，继续按任意键:>")
#     if aaa == "q":
#         return True

# while True:
#     zhuanhuan()
#     if jixu():
#         break

# # 参数传递
# # 定义一个函数，实现输入参数的相加
# def add(a,b):
#     sum = a+b
#     return sum

# num1 = 10
# num2 = 15
# sum = add(num1,num2)
# print(sum)

# def add(a,b=15):
#     sum = a+b
#     return sum

# num1 = 10
# num2 = 15
# sum = add(num1)
# print(sum)

# # 可变参数传递
# def add(a,b,c=20,d=30):
#     sum = a+b+c+d
#     return sum

# num1 = 10
# num2 = 15
# sum1 = add(num1,num2)
# print(sum1)
# sum2 = add(num1,num1,num2)
# # 位置参数一定要放在最前面
# # sum2 = add(num1,b=num1,d=num2)
# print(sum2)


# # 参数个数不定，但是不能为空
# def add(a,*b):
#     he = a
#     for canshu in b:
#         he = he + canshu
#     return he

# print(add(1,2,3))
# print(add(1,2,3,4))
# print(add(1,2,3,7,8,9))
# print(add(1,2))


# # 给a设置初始值，则参数可以为空
# def add(a=99,*b):
#     he = a
#     for canshu in b:
#         he = he + canshu
#     return he

# print(add(1,2,3))
# print(add(1,2,3,4))
# print(add(1,2,3,7,8,9))
# print(add())


# # 函数的返回值
# def fact(n,m=1):
#     s = 1
#     for i in range(1,n+1):
#         s *= 1
#     return s//m, n, m

# fact(10,5)
# a,b,c = fact(10,5)
# print(a,b,c)


# # 定义一个函数，实现 输入两个参数 输出加减乘除
# def yunsuan(a,b):
#     jia = a+b
#     jian = a-b
#     cheng = a*b
#     chu = a/b
#     return jia,jian,cheng,chu

# yunsuan(b = 10,a = 20)
# # 清输出 乘法结果
# num1,num2,num3,num4 = yunsuan(10,20)
# print(num3)


# # 局部变量和全局变量
# n,s = 10,100  # n 和 s是全局变量

# def yunsuan(a,b):  # 定义乘法运算
#     k = a
#     y = k*s
#     return y   # 返回乘积

# shuchu = yunsuan(n,s)
# print(shuchu)  # 1000

# 定义全局变量
n, s = 10, 100


def yunsuan(a, b):  # 100 100
    n = a
    # s = 111   # 局部变量和全局变量重名，优先使用局部变量
    # print(s)
    y = n * s
    return y


shuchu = yunsuan(b=n, a=s)  # b=100 a = 100
print(shuchu)  # 10000
print(s)
