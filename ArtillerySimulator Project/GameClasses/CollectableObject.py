import pygame, random
from GlobalVariables import Globals
from GameClasses.Particle import Particle

class CollectableObject(pygame.sprite.Sprite):
    def __init__(self, image_tag, minx, maxx, miny, maxy):
        super().__init__()
        self.image = Globals.images[image_tag]
        self.rect = self.image.get_rect()
        self.minx, self.maxx, self.miny, self.maxy = minx, maxx, miny, maxy
        self.new_place()

        self.destroyed = False
        self.particles = pygame.sprite.Group()

    def new_place(self):
        self.destroyed = False
        new_x = random.randint(self.minx, self.maxx)
        new_y = random.randint(self.miny, self.maxy)
        self.rect.x = new_x
        self.rect.y = new_y
        for spr in Globals.spr_coins:
            if self.rect != spr.rect:
                if self.rect.colliderect(spr.rect):
                    self.new_place()
        for spr in Globals.spr_targets:
            if self.rect != spr.rect:
                if self.rect.colliderect(spr.rect):
                    self.new_place()

    def on_collect(self):
        pass

    def on_destroy(self):
        self.destroyed = True
        for i in range(Globals.particles_count):
            particle = Particle(self.rect.x, self.rect.y, 10, 10)
            self.particles.add(particle)
            Globals.spr_particles.add(particle)
        self.rect.center = (-200, -200)

    def update(self, *args):
        if self.destroyed:
            self.particles.update()
            if len(self.particles.sprites()) == 0:
                self.new_place()
        else:
            super().update(*args)
            for spr in Globals.spr_alive:
                if self.rect.colliderect(spr.rect):
                    spr.kill()
                    self.on_collect()