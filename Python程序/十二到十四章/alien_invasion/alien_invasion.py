import sys
import pygame

from settings import Settings
from ship import Ship

class AlienInvasion:
    """管理游戏资源和⾏为的类"""

    def __init__(self):
        """初始化游戏并创建游戏资源"""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)) # 宽 1200 像素，高 800 像素
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

    def run_game(self):
        """开始游戏的主循环"""
        while True:
            # 侦听键盘和⿏标事件
            self._check_events()
            self._update_screen()

            self.clock.tick(60)
    
    def _check_events(self):
        """响应按键和⿏标事件"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
    
    def _update_screen(self):
            """更新屏幕上的图像，并切换到新屏幕"""
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()

            pygame.display.flip()

if __name__ == '__main__':
    # 创建游戏实例并运⾏游戏
    ai = AlienInvasion()
    ai.run_game()