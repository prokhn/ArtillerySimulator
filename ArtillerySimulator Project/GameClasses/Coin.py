import pygame
from GlobalVariables import Globals

class Coin(pygame.sprite.Sprite):
    def __init__(self, x, y, sprite_name, value, groups=None):
        super().__init__(groups)
        self.image = Globals.images.get(sprite_name)
        if self.image is None:
            Globals.logger('e', 'Coin init: no sprite with name %s' % sprite_name)
            self.image = Globals.images['basic']
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.value = value