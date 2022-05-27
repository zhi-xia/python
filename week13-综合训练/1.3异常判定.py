# 1.3谜底随机产生，给出猜的最大次数。程序运行时，首先出现“这是张三编写的猜数字游戏”。
#    然后提示用户进行猜测。如果输入的不是指定范围内（0-10），提示重新输入，再根据用户输入进行必要的提示（猜对了、太大了、太小了）。
#    如果猜对则提前结束程序，如果次数用完仍没有猜对，提示游戏结束并给出正确答案。
import random

print("这是周文博编写的猜数字游戏")
midishu = random.randint(0, 9)
maxTimes = 3
print(f"欢迎进入游戏时间，你有{maxTimes}次机会")
i = 1
while i <= maxTimes:
    try:
        guess = int(input("请输入0-9之间的整数:>"))
    except:
        print("不在指定范围内（0-9），请重新输入")
        continue
    if guess < 0 or guess > 9:
        print("不在指定范围内（0-9），请重新输入")
        continue
    if guess == midishu:
        print("猜对了")
        break
    elif guess > midishu:
        print("太大了")
    else:
        print("太小了")
    i = i + 1
print("很遗憾，游戏结束")
print(f"猜的数是{midishu}")
