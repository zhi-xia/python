import random
import time
from sys import exit
import pygame
from pygame.locals import *

pygame.init()
# 屏幕宽度
screen_width = 450
# 屏幕高度
screen_height = 560
# 游戏剩余时间
times = 10
# 绘制窗口
screen = pygame.display.set_mode((screen_width, screen_height), 0, 32)

# 游戏标题
pygame.display.set_caption("孙悟空接桃")
# 分数字体，字号
run_time_font = pygame.font.SysFont('simhei', 48)


def game_start():
    # 加载图片
    monkey = pygame.image.load('monkey.png')
    banana = pygame.image.load('tao1.png')
    game_background = pygame.image.load('background.jpg')
    # 香蕉下落速度
    speed_list = [1, 2, 3, 4, 5]
    # 分数
    score = 0
    # 猴子位置信息
    monkey_x = 200
    monkey_y = 470
    # 设置移动速度
    monkey_x_speed = 1
    monkey_move = {K_LEFT: 0, K_RIGHT: 0}
    # 香蕉坐标列表
    pos_list = []
    # 绘制初始化香蕉
    for i in range(7):
        x = random.randint(0, 390)
        y = random.randint(0, 560)
        s = random.choice(speed_list)
        pos_list.append([x, y, s])
    # 帧率控制Clock对象
    clock = pygame.time.Clock()
    while True:
        screen.blit(game_background, (0, 0))
        # 接收信息处理
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            if event.type == KEYDOWN:
                if event.key in monkey_move:
                    monkey_move[event.key] = 1
            elif event.type == KEYUP:
                if event.key in monkey_move:
                    monkey_move[event.key] = 0
        second_time_passed = clock.tick(60)
        # 定位猴子移动后坐标
        monkey_x -= monkey_move[K_LEFT] * monkey_x_speed * second_time_passed
        monkey_x += monkey_move[K_RIGHT] * monkey_x_speed * second_time_passed
        # 判断猴子边界条件
        if monkey_x > 450 - monkey.get_width():
            monkey_x = 450 - monkey.get_width()
        elif monkey_x < 0:
            monkey_x = 0
        screen.blit(monkey, (monkey_x, monkey_y))
        for y in pos_list:  # 坐标循环，从y轴垂直下落
            y[1] = y[1] + y[2]
            screen.blit(banana, (y[0], y[1]))  # 绘制香蕉
            # 没接到桃子检测
            if y[1] >= 560:
                score -= 10
                y[1] = -banana.get_height()
            # 碰撞检测
            if monkey_x < y[0] < monkey_x + monkey.get_width() and monkey_y - banana.get_height() < y[1] < monkey_y:
                score += 10
                pos_list.remove([y[0], y[1], y[2]])
                x, y, s = random.randint(0, 390), random.randint(0, 560), random.choice(speed_list)
                if len(pos_list) <= 6:
                    pos_list.append([x, -y, s])

        screen_score = run_time_font.render('分数：' + str(score), True, (255, 0, 0))
        screen.blit(screen_score, (0, 0))
        screen_time = run_time_font.render('剩余时间：' + str(int(times - time.time() + start_time)), True, (255, 0, 0))
        screen.blit(screen_time, (0, 50))
        # 读取最高记录
        try:
            with open(r"record.txt", "r") as f:
                record = f.read()
        except FileNotFoundError:
            # 初始化最高记录
            with open(r"record.txt", "w+") as f:
                record = 0
                f.write(str(record))
        screen_score = run_time_font.render('最高记录：' + str(record), True, (255, 0, 0))
        screen.blit(screen_score, (0, 100))

        # 刷新显示
        pygame.display.update()
        # -100分游戏结束
        if score == -100:
            return -1
        # 游戏时间超过一分钟结束
        if time.time() - start_time >= times:
            # 刷新记录
            if score > int(record):
                with open(r"record.txt", "w+") as f:
                    f.write(str(score))
            return -1


if __name__ == '__main__':
    start_time = time.time()
    while True:
        if game_start() == -1:
            break
    print("游戏结束")

