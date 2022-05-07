# # 创建一个字典  dict() 'key':value
# # 字典key不能重复,value可以重复
# b = {'张三':80,'李四':90}
# print(b)

# # 添加数据
# b['王五'] = 69
# print(b)

# # 修改数据
# b['王五'] = 79
# print(b)

# # 删除数据
# del b['李四']
# print(b)

# # 分别打印key和value
# print(b.keys())
# print(b.values())

# 练习
name = ['zs','ls','ww','ml']
score = [78,98,45,34]
for i in range(4):
    a = set()
    a[name]