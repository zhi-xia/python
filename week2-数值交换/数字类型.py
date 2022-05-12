# input默认类型是字符串
# 需要转换类型（使用eval转换成数字）

# a = eval(input("输入第一个数："))
# b = eval(input("输入第二个数："))
# s = a * b
# print(s)
# print(type(s))


# 身份证实验
idnum = input("请输入身份证号码：")
# 提取出生年份
# print(idnum[6]+idnum[7]+idnum[8]+idnum[9])

# 连续提取方法提取不到最后一位数
# print(idnum[6:9])
print(idnum[6:10])
