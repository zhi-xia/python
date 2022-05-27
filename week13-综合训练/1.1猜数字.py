# 任务1  编写程序实现猜数字游戏（10以内的整数）：
# 1.1	给定谜底数，给出猜的最大次数。程序运行时，首先出现“这是张三编写的猜数字游戏”。
#       然后提示用户进行猜测，并根据用户输入进行必要的提示（猜对了、太大了、太小了）。
#       如果猜对则提前结束程序，如果次数用完仍没有猜对，提示游戏结束并给出正确答案。
print("这是周文博编写的猜数字游戏")
midishu = 8
maxTimes = 3
print(f"欢迎进入游戏时间，你有{maxTimes}次机会")
for i in range(0, maxTimes):
    guess = int(input("请输入0-9之间的整数:>"))
    if guess == midishu:
        print("猜对了")
        break
    elif guess > midishu:
        print("太大了")
    else:
        print("太小了")
else:
    print("很遗憾，游戏结束")
    print(f"猜的数是{midishu}")