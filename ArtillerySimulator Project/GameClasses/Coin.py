import pygame, random
from GlobalVariables import Globals

class Coin(pygame.sprite.Sprite):
    def __init__(self, params):
        super().__init__()
        self.image = Globals.images[params[0]]
        self.rect = self.image.get_rect()
        self.value = params[1]
        self.minx, self.maxx, self.miny, self.maxy = params[2:]
        self.new_place()

    def new_place(self):
        new_x = random.randint(self.minx, self.maxx)
        new_y = random.randint(self.miny, self.maxy)
        self.rect.x = new_x
        self.rect.y = new_y
        for spr in Globals.spr_coins:
            if self.rect != spr.rect:
                if self.rect.colliderect(spr.rect):
                    self.new_place()
        for spr in Globals.spr_targets:
            if self.rect.colliderect(spr.rect):
                self.new_place()

    def update(self, *args):
        super().update(*args)
        for spr in Globals.spr_alive:
            if self.rect.colliderect(spr.rect):
                spr.kill()
                Globals.money += self.value
                self.new_place()