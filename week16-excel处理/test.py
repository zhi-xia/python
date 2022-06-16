python = [90, 86, 96, 67]
java = [67, 89, 54, 90]
spm = [90, 98, 92, 76]
print(type(python))

# 计算总分
total = python + java + spm
print(total)
score = [0, 0, 0, 0]
score[0] = python[0] + java[0] + spm[0]
print(score)
len(score)

# 为了便于计算，统计，引入numpy模块
import numpy as np

p = np.array(python)
j = np.array(java)
s = np.array(spm)
print(type(p))
ren_total = p + j + s
print(ren_total)
p.mean()
p.max()
