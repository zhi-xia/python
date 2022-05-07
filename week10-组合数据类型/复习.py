# 复习
# 集合
# 创建一个集合
a = set()
# 向里面添加元素
a.add(2)
print(a)  # {2}

# 将列表[2,2,3,4],加入集合
b = [2,2,3,4]
a.update(b)
print(a)  # {2,3,4}

# 把2从集合中删除
a.remove(2)
print(a)