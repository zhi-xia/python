# 可视化
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2 * np.pi, 2 * np.pi, 100)
# print(x)

y = np.sin(x)
plt.rcParams["font.sans-serif"] = "SimHei"
plt.rcParams["axes.unicode_minus"] = False
plt.plot(x, y, "r--d")
plt.plot(x, np.cos(x))
plt.legend(["sin(x)", "cos(x)"])
plt.title("16周我画的")
plt.xlabel("xlable")
plt.ylabel("hhhhh")
plt.show()


# 直方图
x1 = [10, 20, 35]
x2 = [21, 13, 45]
x = [0, 1, 2]
plt.bar(x, x1)
plt.bar(x, x2)
plt.show()
