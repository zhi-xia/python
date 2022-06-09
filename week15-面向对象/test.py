# 类的定义
class Car:
    # 类的属性
    wheel = 4

    def __init__(self, color, pinPai):
        self.yanSe = color
        self.pai = pinPai
        print("这个车的颜色是", self.yanSe)


# 创建对象
qq = Car("red", "BYD")
qq2 = Car("blue", "greatwall")
print(qq.wheel)
print(Car.wheel)

# 显示qq2的品牌
print("qq2的品牌是", qq2.pai)
# print(Car.pai) err 不能用类名调用实例属性

# qq2的颜色被改装成金色
print("qq2原来的颜色", qq2.yanSe)
qq2.yanSe = "gold"
qq2.laBa = "大喇叭"
print("qq2改装后的颜色", qq2.yanSe)
print("qq2新加的", qq2.laBa)


# 定义实例方法
# 定义一个Cat类
class Cat:

    def __init__(self, type="波斯猫", name="黑猫警长"):
        self.type = type
        self.name = name
        print(f"这只猫叫{self.name}种类是{self.type}")

    def eat(self):
        print("爱吃鱼")

    def eat2(self, no1, no2):
        self.favor = no1 + no2
        print(f"最喜欢吃的是{self.favor}")


cat1 = Cat()
cat1.eat()

# type 和 name 实例化时候输入，默认是波斯猫，黑猫警长
cat2 = Cat("蓝白", "Tom")
cat3 = Cat(name="飞飞")
cat3.eat()
cat3.eat2("肉骨头", "大鲨鱼")
Cat.eat(cat3)
Cat.eat2(cat3, "肉骨头", "大鲨鱼")


# 定义Card 有卡号 密码
class Card:
    def __init__(self, kh, mima):
        self.cardId = kh
        # 把密码定义成私有 外面是不能访问的
        self.__passWd = mima


card1 = Card(12345678, "88888")
print(card1.cardId)
# print(card1.__passWd) err


# 定义一个People类，使用People类
# 创建一个mayun对象，添加company属性，值是"阿里巴巴"
# 创建一个wangjianlin对象，添加company属性，值是"万达集团"
class Animal:
    def __init__(self, name, age, color, food):
        self.name = name
        self.age = age
        self.color = color
        self.food = food

    def run(self):
        print(f"{self.name}正在奔跑")

    def get_age(self):
        print(f"{self.name}今年{self.age}岁了")

    def eat(self):
        print(f"{self.name}正在吃{self.food}")


daxiongmao = Animal(age=5, color="黑白", name="大熊猫", food="竹子")
print(f"{daxiongmao.name}今年{daxiongmao.age}岁了，颜色是{daxiongmao.color}，喜欢吃{daxiongmao.food}")
daxiongmao.run()
daxiongmao.get_age()
daxiongmao.eat()

# 实例化对象
animal1 = Animal("大熊猫", 5, "黑白", "竹子")
print(f"{animal1.color}")
animal2 = Animal("猫", 0.5, "白色", "鱼")
