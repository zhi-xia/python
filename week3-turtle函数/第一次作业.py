# 这样import不用写前缀turtle.
from turtle import *
setup(600,400,None,None)
title("第一次作业——海龟绘图")
pendown()
pensize(5)
pencolor("pink")
# 设置填充颜色
fillcolor("skyblue")
begin_fill()
#隐藏小海龟
# ht()
# 设置箭头形状:turtle,arrow,circle,suqare,triangle,classic(默认)
shape("turtle")
# 设置海龟方向
seth(0)
# 设置运动距离
fd(100)
# 设置运动速度
speed(1)
seth(90)
fd(100)
seth(180)
fd(100)
seth(270)
fd(100)
end_fill()
done
