import random

a = []
# print(type(a))
for i in range(20):
    num = random.randint(1, 100)
    a.append(num)
# print(a)
num_1 = a[9]
num_2 = a[14]
num_3 = a[2]
# -------------------
# 奖品
haoma = {num_1: '一等奖', num_2: '二等奖', num_3: '三等奖'}
print(haoma)
jiangpin = {'一等奖': '电脑', '二等奖': '手机', '三等奖': '微波炉'}
print(jiangpin)

# 输入号码
cjhm = int(input("请输入抽奖号码0-100:>"))
print("输入的抽奖号码是", cjhm)
# for cjhm in haoma.keys():
#     print("此时的cjhm是", cjhm)

# 实现中奖号码检测, 输出
if cjhm in haoma.keys():
    print(f"恭喜你,中了{haoma[cjhm]}")
    print(f"奖品是{jiangpin[haoma[cjhm]]}")
else:
    print("很遗憾，没有中奖！")
