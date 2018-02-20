import pygame, random
from GlobalVariables import Globals


class Target(pygame.sprite.Sprite):
    def __init__(self, params):
        super().__init__()
        img_tag, self.score_adds, self.minx, self.maxx, self.miny, self.maxy = params
        self.image = Globals.images[img_tag]
        self.rect = self.image.get_rect()
        self.new_place()

    def new_place(self):
        new_x = random.randint(self.minx, self.maxx)
        new_y = random.randint(self.miny, self.maxy)
        self.rect.x = new_x
        self.rect.y = new_y
        print(self.rect)

    def update(self, *args):
        super().update(*args)
        # Globals.logger('o', str(self.rect.collidelist(Globals.spr_alive)))
        for spr in Globals.spr_alive:
            if self.rect.colliderect(spr.rect):
                spr.kill()
                Globals.score += self.score_adds
                self.new_place()
