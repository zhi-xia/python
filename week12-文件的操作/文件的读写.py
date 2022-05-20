# 文本文件的读写
file1 = open("package\\test.txt", "rt")
file2 = file1.read()
print(file2)
file1.close()
# 今天是5月19，
# 明天是5月20。


# 分别用文本方式和二进制方式读入文件，并在屏幕上显示读入内容
file1 = open("package\\test.txt", "rb")
file2 = file1.read()
print(file2)
file1.close()
# b'\xbd\xf1\xcc\xec\xca\xc75\xd4\xc219\xa3\xac\r\n\xc3\xf7\xcc\xec\xca\xc75\xd4\xc220\xa1\xa3'


# 对文件进行写入操作  打开-操作-关闭
# 往test文件写入“今天天气很不错”
file = open("package\\test.txt", "a+")  # a+ 可以读也可以写
file.write("\n今天天气很不错")
file2 = file.read()
print(file2)
file.close()
