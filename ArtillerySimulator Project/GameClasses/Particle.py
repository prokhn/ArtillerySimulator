import pygame, random
from GlobalVariables import Globals, scale

class Particle(pygame.sprite.Sprite):
    def __init__(self, x, y, x_vel_max, y_vel_max):
        super().__init__()
        image_tag = random.choice(Globals.particles_image_tags)
        self.image = Globals.images[image_tag]
        self.image = pygame.transform.rotate(self.image, random.randint(0, 75))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed_x = random.randint(scale(-x_vel_max), scale(x_vel_max))
        self.speed_y = random.randint(scale(-10), (y_vel_max - 10))

        self.GRAVITY = Globals.gravity / 2

    def update(self, *args):
        super().update(*args)
        self.speed_y += self.GRAVITY / Globals.fps
        self.rect.x += round(self.speed_x)
        self.rect.y += round(self.speed_y)

        if self.rect.x > Globals.scr_width or self.rect.y >= Globals.scr_height:
            self.kill()
