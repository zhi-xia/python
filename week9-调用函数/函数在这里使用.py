# 通过调用7段数码管数字显示函数drawDigit(),显示自己的生日
import turtle
import test

turtle.setup(700,300,400,200)
turtle.penup()
turtle.fd(-200)
turtle.pendown()
birthday = input("请输入生日格式如20100810:>")
for num in birthday:
    num = int(num)
    test.drawDigit(num)

turtle.penup()
turtle.goto(-200,-100)
turtle.color("red")
turtle.write("张三的出生时间",font=("Arial",50,"normal"))

turtle.done