from operator import truediv
from pickle import TRUE
import random


def Award(i, Directory):
    while True:
        try:
            if i == Directory[10]:
                print("一等奖 电脑")
                break
            elif i == Directory[15]:
                print("二等奖 手机")
                break
            elif i == Directory[3]:
                print("三等奖 微波炉")
                break
            else:
                print("没有中奖哦")
                break
        except ValueError:
            print("请输入范围在（0-10以内的数字）")


print("这是王小康的猜数字游戏")

Awards = {3: '微波炉', 2: '手机', 1: '电脑'}
AdNum = {}
for i in range(0, 20):
    Rdm = random.randint(1, 100)
    AdNum[i] = Rdm

for key, value in AdNum.items():
    print('key: ', key, 'value: ', value)

while TRUE:
    try:
        Gnum = int(input("请输入你的号码"))
        Award(Gnum, AdNum)
    except ValueError:
        print("请输入范围在（0-100以内的数字）")
