# @Author  : Team_boy
# @Time    : 2019/7/1 23:26
import random
import pygame


# 游戏精灵
SCREEN_RECT = pygame.Rect(0, 0, 480, 700)
# 刷新帧率
FRAME_PER_SEC = 60
# 敌机定时器常量
CREATE_ENEMY_ENENT = pygame.USEREVENT
# 子弹 定时器常量加1
HERO_FIRE_EVENT = pygame.USEREVENT + 1

class GameSprite(pygame.sprite.Sprite):

    def __init__(self, image_name, speed=1):
        #  调用父类的初始化方法
        super().__init__()
        # 定义对象属性
        self.image = pygame.image.load(image_name)

        self.rect = self.image.get_rect()
        self.speed = speed


    def update(self):
        self.rect.y += self.speed


class Background(GameSprite):

    """游戏背景精灵"""
    def __init__(self, is_alt=False):
        # 调用父类方法实现精灵创建
        super().__init__("./images/background.png", 1)

        # 判断是否是交替图像
        if is_alt:
            self.rect.y = -self.rect.height


    def update(self):
        # 调用父类方法
        super().update()

        # 判断是否移除屏幕
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height


class Enemy(GameSprite):

    """敌机精灵"""
    def __init__(self):
        # 调用父类方法，创建敌机精灵，
        super().__init__("./images/enemy1.png")
        # 随机速度
        self.speed = random.randint(1, 5)
        # 随机位置
        # 垂直方向
        self.rect.bottom = 0
        # 水平方向
        max_x = SCREEN_RECT.width - self.rect.width
        self.rect.x = random.randint(0, max_x)

    def update(self):
        # 调用父类方法 保持飞行
        super().update()
        # 判断是否飞出屏幕
        if self.rect.y >= SCREEN_RECT.height:
            # print("飞出屏幕")
            self.kill()

    def __del__(self):
        # print("敌机销毁 %s" % self.rect)
        pass


class Hero(GameSprite):
    """飞机类"""
    def __init__(self):
        # 调用父类
        super().__init__("./images/me1.png", 0)
        # 设置初始位置

        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom - 120

        self.bullets = pygame.sprite.Group()

    def update(self):

        # 水平方向移动
        self.rect.x += self.speed

        # 垂直方向
        # self.rect.y += self.speed_1

        # 不能离开屏幕
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.right > SCREEN_RECT.right:
            self.rect.right = SCREEN_RECT.right

    def fire(self):

        for i in (0, 1, 2):
            bullet = Bullet()

            bullet.rect.bottom = self.rect.y - i * 20
            bullet.rect.centerx = self.rect.centerx

            self.bullets.add(bullet)



class Bullet(GameSprite):
    """子弹"""
    def __init__(self):
        # 父类方法
        super().__init__("./images/bullet1.png", -2)

    def update(self):
        super().update()
        # 判断子弹飞出屏幕
        if self.rect.bottom < 0:
            self.kill()

    def __del__(self):
        print("子弹 %s" % self.rect)
