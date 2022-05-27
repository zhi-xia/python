# 1.4 扩展：抽奖游戏，随机生成20个1-100之间的整数序列a，其中第10个数是一等奖,第15个是二等奖，第3个是三等奖，
#     其中奖品是 一等奖 电脑， 二等奖 手机 ，三等奖  微波炉
#     输入：抽奖号码
#     处理：判断是否中奖
#     输出：中奖的话输出奖项和奖品，不中奖的话输出：欢迎再来
import random

maxTimes = 3  # 剩余抽奖次数
jiangpined = [0]  # 抽过的奖品

# 创建奖品

for i in range(20):
    num = random.randint(1, 100)
    if i + 1 == 3:
        jiangpin = {num: '三等奖 微波炉'}
    if i + 1 == 10:
        jiangpin[num] = '一等奖 电脑'
    if i + 1 == 15:
        jiangpin[num] = '二等奖 手机'
    print(num)
# print(jiangpin)

# 开始抽奖
print(f"欢迎进入游戏时间，你有{maxTimes}次机会")
i = 1  # 抽奖次数
while i <= maxTimes:
    # 判断输入值是否合法 - 不合法就重新抽
    try:
        choujiang = int(input("请输入抽奖号码:>"))
        if choujiang < 1 or choujiang > 100:
            print("不在指定范围内（1-100），请重新输入")
            continue
    except:
        print("不在指定范围内（1-100），请重新输入")
        continue

    # 判断输入的号码是否被抽过 - 被抽过就重新抽
    j = 0
    for j in range(0, len(jiangpined)):
        if choujiang == jiangpined[j]:
            print("这个号码已经抽过了，请重新抽一个号码吧！")
            break
    if choujiang == jiangpined[j]:
        continue
    jiangpined.append(choujiang)
    # print(jiangpined)

    # 判断是否中奖
    try:
        print(jiangpin[choujiang])
        print(f"恭喜你中奖了！还有{maxTimes - i}次机会。")
    except:
        print(f"很遗憾，没有中奖，还有{maxTimes - i}次机会。")
    i = i + 1

# 游戏结束
print(f"奖品是{jiangpin}")
print("游戏结束，欢迎再来。")
