# 输入一个100-1000的数
num = input("请输入一个大于100,小于1000的三位整数:")
num = int(num)
# 创建一个列表存储水仙花数
sxh = []

for n in range(100,num+1):
    i = n // 100
    j = n // 10 % 10
    k = n % 10
    if n == i ** 3 + j ** 3 + k ** 3:
        # 将水仙花数保存到列表
        sxh.append(n)
        # 保存为最大的数
        max = n

print("--------(周文博)程序结果输出如下--------")
# 判断是否有水仙花数
if len(sxh) != 0:
    print(f"输入的数是{num},有{len(sxh)}个水仙花数,最大的是{max}")
    print(f"水仙花数是{sxh}")
else:
    print(f"输入的数是{num},没有水仙花数")