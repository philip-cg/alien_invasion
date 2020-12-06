import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):

    def __init__(self, ai_settings, screen, ship):
        super(Bullet, self).__init__()
        self.screen = screen
        # 在(0,0)处创建一个表示子弹的矩形。
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width
                                , ai_settings.bullet_height)
