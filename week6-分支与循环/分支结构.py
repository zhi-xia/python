# >=60 通过 否则重修

# score = eval(input("请输入你的成绩"))
# if score >= 60 :
#     print(f"分数是{score}:恭喜你，顺利通过")
# else:
#     print(f"分数是{score}:非常遗憾，重修")


# 循环10次

# for i in range (0,10):
#     score = eval(input("请输入你的成绩"))
#     if score >= 60 :
#         print(f"分数是{score}:恭喜你，顺利通过")
#     else:
#         print(f"分数是{score}:非常遗憾，重修")
#     print(f"循环第{i+1}次")
# print("循环10次结束")


# >=90  优秀  >=80  良好  >=70  中等  >=60  及格  <60  不及格

# for i in range (2):
#     score = eval(input("请输入你的成绩"))
#     if score >= 90 :
#         print(f"分数是{score},等级是:优秀")
#     elif score >= 80:
#         print(f"分数是{score},等级是:良好")
#     elif score >= 70:
#         print(f"分数是{score},等级是:中等")
#     elif score >= 60:
#         print(f"分数是{score},等级是:及格")
#     else :
#         print(f"分数是{score},等级是:不及格")
# print("现在知道成绩和等级了吧")


# 使用while实现5次循环

# i = 0
# while i<5 :
#     score = eval(input("请输入你的成绩"))
#     if score >= 90 :
#         print(f"分数是{score},等级是:优秀")
#     elif score >= 80:
#         print(f"分数是{score},等级是:良好")
#     elif score >= 70:
#         print(f"分数是{score},等级是:中等")
#     elif score >= 60:
#         print(f"分数是{score},等级是:及格")
#     else :
#         print(f"分数是{score},等级是:不及格")
#     i += 1
# print("现在知道成绩和等级了吧")


# 使用while实现无限循环,直到输入q

while 1:
    score = input("请输入你的成绩(输入q退出程序):>")

    if score == 'q':
        print("退出程序")
        break
    else:
        score = eval(score)

    if score < 0 or score > 100:
        print("成绩无效，请重新输入")
        continue

    if score >= 90:
        print(f"分数是{score},等级是:优秀")
    elif score >= 80:
        print(f"分数是{score},等级是:良好")
    elif score >= 70:
        print(f"分数是{score},等级是:中等")
    elif score >= 60:
        print(f"分数是{score},等级是:及格")
    else:
        print(f"分数是{score},等级是:不及格")

print("现在知道成绩和等级了吧")
