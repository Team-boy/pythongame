# @Author  : Team_boy
# @Time    : 2019/7/1 23:51
import pygame
from plane_sprites import *


class PlaneGame(object):
    """主游戏"""
    def __init__(self):
        print("游戏初始化")

    # 创建游戏窗口
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
    # 创建游戏时钟
        self.clock = pygame.time.Clock()
    # 调用私有方法，精灵和精灵族
        self.__create_sprites()
    # 调用定时器方法 创建敌机
        pygame.time.set_timer(CREATE_ENEMY_ENENT, 1000)

    # 发射子弹
        pygame.time.set_timer(HERO_FIRE_EVENT, 500)

    def __create_sprites(self):
        # 创建背景精灵和精灵族

        bg1 = Background()
        bg2 = Background(True)
        self.back_group = pygame.sprite.Group(bg1, bg2)

        # 敌机精灵族
        self.enemy_group = pygame.sprite.Group()

        # 创建飞机
        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)

        # 创建子弹

    def start_game(self):
        print("游戏开始")

        while True:
            # 设置刷新帧率
            self.clock.tick(FRAME_PER_SEC)
            # 事件监听
            self.__event_handler()
            # 碰撞检测
            self.__check_collide()
            # 更新精灵族
            self.__update_sprites()
            pygame.display.update()

    def __event_handler(self):
        for event in pygame.event.get():
            # 判断是否退出游戏
            if event.type == pygame.QUIT:
                PlaneGame.__game_over()
            elif event.type == CREATE_ENEMY_ENENT:
                # print("敌机出场")
                # 创建敌机精灵
                evemy = Enemy()
                self.enemy_group.add(evemy)
            elif event.type == HERO_FIRE_EVENT:
                 self.hero.fire()

            # elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            #     print("向右")
            # 使用键盘方法
        keys_pressed = pygame.key.get_pressed()
        # 判断元组是否又对应的案件
        if keys_pressed[pygame.K_RIGHT]:
            self.hero.speed = 3
            print("向右")
        elif keys_pressed[pygame.K_LEFT]:
            self.hero.speed = -3
            print("向左")
        elif keys_pressed[pygame.K_DOWN]:
            self.hero.speed_1 = 3
            print("向下")
        else:
            self.hero.speed = 0

    def __check_collide(self):
        # 子弹炸敌机
        pygame.sprite.groupcollide(self.hero.bullets, self.enemy_group, True, True)
        # 敌机炸飞机
        enemies = pygame.sprite.spritecollide(self.hero, self.enemy_group, True)
        if len(enemies) > 0:
            self.hero.kill()
            PlaneGame.__game_over()

    def __update_sprites(self):

        self.back_group.update()
        self.back_group.draw(self.screen)

        self.enemy_group.update()
        self.enemy_group.draw(self.screen)

        self.hero_group.update()
        self.hero_group.draw(self.screen)

        self.hero.bullets.update()
        self.hero.bullets.draw(self.screen)



    @staticmethod
    def __game_over():
        print("游戏结束")

        pygame.quit()
        exit()


if __name__ == '__main__':

    # 创建游戏对象
    game = PlaneGame()
    # 启动游戏
    game.start_game()
