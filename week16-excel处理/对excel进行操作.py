# 有一个成绩表，要对分数进行统计
import pandas as pd

data = pd.read_excel("./score.xlsx")
print(data)

# data["java"][2:4]
# 计算总分
p1 = data["python"]
p2 = data["java"]
p3 = data["spm"]
ren_total = p1 + p2 + p3
data["总分"] = ren_total
print(data)

# 把得到的结果保存到score.xlsx的“统计后”工作表
data.to_excel("./score1.xlsx", sheet_name="统计后", index=False)

# 直接对同一个excel文件读写操作
data["python"][4] = data["python"].mean()
data["java"][4] = data["java"].mean()
data["spm"][4] = data["spm"].mean()
data["姓名"][4] = "平均分"
print(data)

# 求平均，添加在列的后面
with pd.ExcelWriter("./score2.xlsx") as wenjian:
    data.to_excel(wenjian, sheet_name="统计后", index=False)
