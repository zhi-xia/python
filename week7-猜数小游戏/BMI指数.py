# # 编写一个根据体重和身高计算BMI值的程序，并输出国内的BMI指标建议值
# for i in range (5):  # 循环5次
#     print(f"现在是第{i+1}组数据")
#     height = eval(input("请输入身高m:>"))
#     weight = eval(input("请输入体重kg:>"))
#     print(height,weight)
#     BMI = weight/pow(height,2)
#     if BMI < 18.5:
#         print(f"BMI数值是{BMI:.2f},体型按国际标准是：偏瘦")
#     elif BMI < 26:
#         print(f"BMI数值是{BMI:.2f},体型按国际标准是：正常")
#     elif BMI < 30:
#         print(f"BMI数值是{BMI:.2f},体型按国际标准是：偏胖")
#     else:
#         print(f"BMI数值是{BMI:.2f},体型按国际标准是：肥胖")

#     if BMI < 18.5:
#         print(f"BMI数值是{BMI:.2f},体型按国内标准是：偏瘦")
#     elif BMI < 24:
#         print(f"BMI数值是{BMI:.2f},体型按国内标准是：正常")
#     elif BMI < 28:
#         print(f"BMI数值是{BMI:.2f},体型按国内标准是：偏胖")
#     else:
#         print(f"BMI数值是{BMI:.2f},体型按国内标准是：肥胖")

# # 使用while循环
# i = 0
# while i < 5 :
#     print(f"现在是第{i+1}组数据")
#     height = eval(input("请输入身高m:>"))
#     weight = eval(input("请输入体重kg:>"))
#     print(height,weight)
#     BMI = weight/pow(height,2)
#     if BMI < 18.5:
#         print(f"BMI数值是{BMI:.2f},体型按国际标准是：偏瘦")
#     elif BMI < 26:
#         print(f"BMI数值是{BMI:.2f},体型按国际标准是：正常")
#     elif BMI < 30:
#         print(f"BMI数值是{BMI:.2f},体型按国际标准是：偏胖")
#     else:
#         print(f"BMI数值是{BMI:.2f},体型按国际标准是：肥胖")

#     if BMI < 18.5:
#         print(f"BMI数值是{BMI:.2f},体型按国内标准是：偏瘦")
#     elif BMI < 24:
#         print(f"BMI数值是{BMI:.2f},体型按国内标准是：正常")
#     elif BMI < 28:
#         print(f"BMI数值是{BMI:.2f},体型按国内标准是：偏胖")
#     else:
#         print(f"BMI数值是{BMI:.2f},体型按国内标准是：肥胖")


# # 猜数游戏，设定一个0-9之间的整数，让用户通过键盘输入猜
# # 大于：很遗憾，太大  小于：很遗憾，小了  直到猜中：猜了n次，你终于猜对了
# import random
# # random.seed(10)
# flag = 1
# print("============让我们来玩猜数字游戏============")
# while flag:
#     print(f"================开始第{flag}轮游戏===============")
#     target = random.randint(0,9)
#     i = 0
#     while 1:
#         i += 1
#         num = input("请输入一个0-9之间的整数：")
#         if num == "q":
#             flag = 0
#             break
#         num = int(num)
#         if num > target:
#             print(f"你猜的数字是{num}，很遗憾，大了，继续加油")
#         elif num < target:
#             print(f"你猜的数字是{num}，很遗憾，小了，继续加油")
#         else:
#             print(f"你猜的数字是{num}，猜了{i}次，你终于猜对了")
#             flag += 1
#             break
#         print(f"继续加油，现在是第{i}次")
# print("==================游戏结束==================")


import random
# random.seed(10)
while 1:
    print("============让我们来玩猜数字游戏============")
    s = input("开始游戏(y),退出游戏(q):>")
    if s == "q":
        print("==================游戏结束==================")
        break
    target = random.randint(0,9)
    i = 0
    while 1:
        i += 1
        num = input("请输入一个0-9之间的整数：")
        while not num.isnumeric():    # 判断是否为数字
            num = input("请重新输入一个整数：")
        num = int(num)
        if num > target:
            print(f"你猜的数字是{num}，很遗憾，大了，继续加油")
        elif num < target:
            print(f"你猜的数字是{num}，很遗憾，小了，继续加油")
        else:
            print(f"你猜的数字是{num}，猜了{i}次，你终于猜对了")
            break
        print(f"继续加油，现在是第{i}次")
    print("恭喜你，终于猜对了")