huilv = eval(input("请输入汇率："))
for i in range(0, 10):
    C = input("请输入人民币或美元：")
    if C[0] in ["$"]:
        d = eval(C[1:])
        r = d * huilv
        # print(d)
        print("转换后是：￥{:.2f}".format(r))
    elif C[0] in ["￥"]:
        r = eval(C[1:])
        d = r / huilv
        print("转换后是：${:.2f}".format(d))
    else:
        print("error")
