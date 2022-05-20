import PIL
from PIL import Image
tu = Image.open("./package/bird1.jpeg")

# 查看色彩模式
print(tu.mode)
print(tu.format)
print(tu.size)

# 把图片的大小调节为原来的70%，保存为bird2.jpeg
tu = Image.open("./package/bird1.jpeg")
print("原始尺寸", tu.size)
newsize_x = int(tu.size[0]*0.7)
newsize_y = int(tu.size[1]*0.7)
print(f"图调整后的尺寸是（{newsize_x}，{newsize_y}）")
tu2 = tu.resize((newsize_x, newsize_y))
tu2.save("./package/bird3.jpeg")

# 作业1 扩展功能，能够任意改变图片尺寸 保存 运行结果截图


