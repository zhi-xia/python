# 作业2 把gif动画的帧单独保存在一个文件夹，截图
from PIL import Image
gif = Image.open("./package/gif1.gif")
try:
    while True:
        gif.seek(gif.tell()+1)
        gif.save(f"./动画帧/frame{gif.tell():02d}.png")
except:
    print(f"总共{gif.tell()}帧")
    print("处理结束")