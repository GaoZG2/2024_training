import pygame

class Ship:
    """管理⻜船的类"""

    def __init__(self, ai_game):
        """初始化⻜船并设置其初始位置"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # 加载⻜船图像并获取其外接矩形
        self.image = pygame.image.load('images/ship.bmp')
        self.image.set_colorkey((230, 230, 230)) # 12.2更改图片背景色
        self.rect = self.image.get_rect()

        # 每艘新⻜船都放在屏幕底部的中央
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """在指定位置绘制⻜船"""
        self.screen.blit(self.image, self.rect)