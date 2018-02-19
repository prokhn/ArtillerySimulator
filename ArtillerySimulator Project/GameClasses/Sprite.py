import pygame
from GlobalVariables import Globals


class Sprite(pygame.sprite.Sprite):
    def __init__(self, x, y, im_tag, groups=None):
        super().__init__(groups)
        self.image = Globals.images[im_tag]
        self.rect = self.image.get_rect()
        self.set_pos(x, y)

    def set_pos(self, x, y):
        self.x = x
        self.y = y
        self.rect.x = x
        self.rect.y = y