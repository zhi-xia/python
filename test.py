s = []
# 计算50以内素数
for i in range(2, 50):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        s.append(i)
# print(s[3])

