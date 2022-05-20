# 在package下面创建文件test1.txt 往里面添加内容
# 1.今天我们来练习一下
file = open("./package/test1.txt", "w+t")
content = "今天我们来练习一下"
file.write(content)
file.close()

# 2.["张三","李四","王五"]
file = open("./package/test1.txt", "a+")
content = ["zhangsan", "lisi", "wangwu"]
print("显示文件内容1", file.read())
file.writelines(content)
print("显示文件内容2", file.read())
file.close()

# 修改上面代码，显示内容
file = open("./package/test1.txt", "w+")
file.write("今天天气很不错")
file.seek(0)
print("显示文件内容1", file.read())
content = ["zhangsan", "lisi", "wangwu"]
file.writelines(content)
print("显示文件内容2", file.read())
file.close()
