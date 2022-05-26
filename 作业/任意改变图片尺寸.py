# 作业1 扩展功能，能够任意改变图片尺寸 保存 运行结果截图
from PIL import Image
tu = Image.open("./package/bird1.jpeg")
print("原始尺寸", tu.size)
newsize_x = int(input("请输入图片尺寸（x）像素:>"))
newsize_y = int(input("请输入图片尺寸（y）像素:>"))
print(f"图调整后的尺寸是（{newsize_x},{newsize_y}）")
tu2 = tu.resize((newsize_x,newsize_y))
tu2.save("./package/bird2.jpeg")