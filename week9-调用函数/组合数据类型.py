# 1 序列类型：字符串，元组，列表
# 1.1 字符串
a = "这个是zifuchuan类型,123"
print(a[2])  # 是
print(a[3:12])  # zifuchuan

# 1.2列表 list.[]
b = [1,2,"abc",a]
print(b)  # [1, 2, 'abc', '这个是zifuchuan类型,123']
print(b[2])  # abc
print(b[2:4])  # ['abc', '这个是zifuchuan类型,123']

print(type(b))  # <class 'list'>
print(type(a))  # <class 'str'>

# 1.2.1 列表增加元素(从最后加, 插队, 修改, 删除)
b.append("守纪律排队")
print(b)

b.insert(2,"插队")
print(b)

b[2] = "插队是不好的"
print(b)

b.pop(3)  # 按序号删除元素
print(b)

b.remove(2)  # 按内容删除元素
print(b)

# 1.3 元组 tuple()
# 把列表b转化为元组赋值给c
# 元组只支持查看操作,不支持修改
print("b的类型是",type(b))
c = tuple(b)
print(c)
print("c的类型是",type(c))

# 1.3.1 元组练习
# 报名 张三 李四 王五 马六
# 后来 陈七 林九 李三也报名了,其中李三要插在李四前面
# 李四说自己的名字写错了 应该是 李思
# 马六说不报名了
baoming = ["张三","李四","王五","马六"]
print(baoming)
baoming.append("陈七") 
baoming.append("林九") 
baoming.insert(1,"李三")
print(baoming)
baoming[2] = "李思"
print(baoming)
baoming.remove("马六")
print(baoming)

# 王五,陈七太想参加了,最后又报了一次名(重复报名)
a = ["王五","陈七"]
baoming = baoming + a
print(baoming)

# 统计报名人数
print(len(baoming))


# 2 集合类型 set()
# 无序
d = {1,2,"hhh",("txt","f",3.1)}
print(type(d))

d.add(200)
print(d)

d.add("kkk")
print(d)

# 删除kkk
d.remove("kkk")
print(d)

# 利用集合的特性，把baoming去重
print(baoming,type(baoming))
quchong = set(baoming)
print(quchong,type(quchong))
# 最终名单不能修改
final = tuple(quchong)
print(final,type(final))