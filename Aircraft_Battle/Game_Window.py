# @Author  : Team_boy
# @Time    : 2019/7/1 0:42
import pygame
from plane_sprites import *

pygame.init()
# 创建游戏窗口
screen = pygame.display.set_mode((480, 700))

# 绘制背景图像

# 1.使用pygame.image.load()加载
bg = pygame.image.load("./images/background.png")
# 2.调用blit方法绘制到指定位置

# 3.调用display.update()方法更新
# pygame.display.update()
# 飞机
hero = pygame.image.load("./images/me1.png")
# screen.blit(hero, (180, 500))
# 创建时钟对象
clock = pygame.time.Clock()

# 定义rect记录飞机的初始位置
hero_rect = pygame.Rect(150, 300, 102, 126)

# 创建敌机的精灵对象

enemy = GameSprite("./images/enemy1.png")
enemy1 = GameSprite("./images/enemy1.png", 2)
enemy2 = GameSprite("./images/enemy1.png", 3)
enemy3 = GameSprite("./images/enemy1.png", 4)

# 创建敌机的精灵族
enemy_group = pygame.sprite.Group(enemy, enemy1, enemy2, enemy3)

while True:
    # 循环体中的帧数
    clock.tick(60)
    hero_rect.y -= 3
    # 判断飞机的位置
    if hero_rect.y + hero_rect.height <= 0:
        hero_rect.y = 700
    screen.blit(bg, (0, 0))
    screen.blit(hero, hero_rect)

    # 精灵族调用两个方法 update draw
    enemy_group.update()
    enemy_group.draw(screen)


    pygame.display.update()

    # 退出按钮监听
    # event.get 获取事件，遍历
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("游戏退出")
            # quit 卸载所有模块
            pygame.quit()
            # 直接退出程序
            exit()



