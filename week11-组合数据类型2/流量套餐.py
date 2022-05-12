# 为了避免选择超出范围，要求输入不合要求的，重新输入
# 变量用list类型
# 扩展 有具体费用 要求还要输出套餐费用（三者相加）
duration_fy = {"0分钟": 0, "50分钟": 30, "100分钟": 60, "30分钟": 100, "不限量": 150}  # 时长
data_fy = {"0M": 0, "500M": 10, "1G": 20, "5G": 30, "不限量": 50}  # 流量
message_fy = {"0条": 0, "50条": 5, "100条": 10}  # 短信

# 把字典里面的关键字用列表存储
duration = list(duration_fy.keys())
data = list(data_fy.keys())
message = list(message_fy.keys())


# 判定合法输入函数
def panding(xuhao, duixiang):
    a = int(xuhao)
    while a - 1 not in list(range(len(duixiang))):
        a = int(input("请重新输入"))
    return a


# 运行界面
print("定制自己的手机套餐：")
print("A：设置通话时长：")

# 遍历列表输出
for i in range(len(duration)):
    print(f"{i + 1}. {duration[i]}")

# 选择
sj = int(input("输入选择的通话时长编号："))
panding(sj, duration)

# 流量选择
print("\nB：设置流量：")
# 遍历列表输出
for i in range(len(data)):
    print(f"{i + 1}. {data[i]}")

# 选择
ll = int(input("输入选择的流量编号："))
panding(ll, data)

# 短信选择
print("\nC：设置短信：")
# 遍历列表输出
for i in range(len(message)):
    print(f"{i + 1}. {message[i]}")

# 选择
dx = int(input("输入选择的短信编号："))
panding(dx, message)

# 输出选择
print(f"通话时长选择是：{duration[sj - 1]},流量选择是：{data[ll - 1]},短信选择是：{message[dx - 1]}")
# 计算费用
total = duration_fy[duration[sj - 1]] + data_fy[data[ll - 1]] + message_fy[message[dx - 1]]
print(f"套餐费用是{total}")
