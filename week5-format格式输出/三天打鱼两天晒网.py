# 实现一下 三天打鱼（0.01）两天晒网（0.01）
chushi = 1.0
dayu = 0.01
shaiwang = 0.01
dayup = chushi
# (1,366)是指从1到366
for i in range(1, 366):
    if i % 5 in [1, 2, 3]:
        dayup = dayup * (1 + dayu)
    else:
        dayup = dayup * (1 - shaiwang)
# {n}表示输出format中第n个数据
# print("三天打鱼{0}两天晒网{1}，初始时是{2}一年后是:{3:.2f}".format(dayu,shaiwang,chushi,dayup))
print(f"三天打鱼{dayu}两天晒网{shaiwang}，初始时是{chushi}一年后是:{dayup:.2f}")
