# 输入一个大于2的自然数，输出小于该数字的所有素数组成的集合，并求出该素数组合的数目和平均数
# 输入10
print("1920170040周文博的代码 求素数 验证的时候请输入8")
num = int(input("请输入一个大于2的自然数:"))
s = []
# 计算素数
for i in range(2, num + 1):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        s.append(i)
print(f"输入的是{num},那么小于{num}的素数有")
# 素数个数
n = len(s)
Sum = 0
for i in range(n):
    Sum += s[i]
# 计算平均值
avg = Sum / n
s_set = set(s)
print(s_set)
print(f"一共有{n}个,它们的平均值是{avg}")
