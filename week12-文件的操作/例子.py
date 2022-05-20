fname = input("请输入文件名：")
fo = open(fname, "w+")
ls = ["唐诗", "宋词", "元曲"]
fo.writelines(ls)
fo.seek(0)
print(fo.read())
fo.close()