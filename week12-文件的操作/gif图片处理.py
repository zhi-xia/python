# 把gif动画的帧保存下来  tell()
from PIL import Image
gif = Image.open("./package/gif1.gif")
gif.save(f"./package/zhen{gif.tell()}.png")

# 作业2 把gif动画的帧单独保存在一个文件夹，截图
