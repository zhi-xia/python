import math

while 1:
    a = int(input("输入一个整数:>"))
    b = pow(a,0.5)
    print(f"{b:+>30.3f}")
    c = input("输入q退出程序,按任意键继续:>")
    if c == "q":
        break