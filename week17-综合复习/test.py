# 数字类型 字符串
# 组合类型 list tuple str
a = [1, 2, 3, 4, 5, 6, 7, 8]
# print(a[0:-1])  # [1, 2, 3, 4, 5, 6, 7]
# 从第一个开始，到最后，间隔为2
# print(a[1::2])  # [2, 4, 6, 8]

b = "python"
# print(list(b))

# 把b插入到3和4之间
a.insert(3, b)
# print(a)

# 再把b加到list最后
a.append(b)
# print(a)

# 把第一个python删除
# a.remove("python")
# print(a)

# 利用集合去重
a_set = set(a)
# print(a_set)

# 往集合里面添加 999 666
a_set.add(999)
a_set.add(666)
# print(a_set)

# 删除6
a_set.discard(6)
# print(a_set)

# 转换为不可改变的类型 tuple
a_tuple = tuple(a_set)
# print(a_tuple)
# print(a_tuple[8])

# 访问最后字符串的第一位
# print(a_tuple[-1][0])

# 生成一个长度和a_tuple一样的整数序列，由100开始
c = len(a_tuple)
a1 = range(100, 100 + c)
print(a1)

# 生成字典，key:value item
a2 = {}
print(type(a2))

a2["class"] = "计算机13班"
a2["name"] = "周文博"
a2["数学"] = 99
print(a2)




