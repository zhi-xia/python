# 1.4 扩展：抽奖游戏，随机生成20个1-100之间的整数序列a，其中第10个数是一等奖,第15个是二等奖，第3个是三等奖，
#     其中奖品是 一等奖 电脑， 二等奖 手机 ，三等奖  微波炉
#     输入：抽奖号码
#     处理：判断是否中奖
#     输出：中奖的话输出奖项和奖品，不中奖的话输出：欢迎再来
import random

for i in range(20):
    num = random.randint(1, 100)
    if i == 3:
        jiangping = {num: '三等奖 微波炉'}
    if i == 10:
        jiangping[num] = '一等奖 电脑'
    if i == 15:
        jiangping[num] = '二等奖 手机'
print(jiangping)
maxTimes = 3
print(f"欢迎进入游戏时间，你有{maxTimes}次机会")
i = 1
while i <= maxTimes:
    try:
        choujiang = int(input("请输入抽奖号码:>"))
        if choujiang < 1 or choujiang > 100:
            print("不在指定范围内（1-100），请重新输入")
            continue
    except ValueError:
        print("不在指定范围内（1-100），请重新输入")
        continue
    try:
        print(jiangping[choujiang])
        print("恭喜你中奖了！")
        break
    except:
        print(f"很遗憾，没有中奖，还有{maxTimes - i}次机会。")
        i = i + 1
if i > maxTimes:
    print("游戏结束，欢迎再来。")