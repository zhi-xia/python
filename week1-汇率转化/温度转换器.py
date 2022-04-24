TempStr = input("请输入带温度表示符号的温度值（例如：32C）:")
if TempStr[-1] in ["F","f"]:
    F = eval(TempStr[0:-1])
    C = (F-32) / 1.8
    print("转换后的摄氏温度是：{:.2f}C".format(C))
elif TempStr[-1] in ["C","c"]:
    C = eval(TempStr[0:-1])
    F = C * 1.8 + 32
    print("转换后的华氏温度是：{:.2f}F".format(F))
else:
    print("error")