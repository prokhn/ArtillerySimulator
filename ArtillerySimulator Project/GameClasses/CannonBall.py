import pygame, time, math
from GlobalVariables import Globals

class CannonBall(pygame.sprite.Sprite):
    def __init__(self, x, y, vel_x, vel_y, image, alive_time=2, groups=None):
        if groups:
            super().__init__(groups)
        else:
            super().__init__()

        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x - self.rect.width // 2
        self.rect.y = y - self.rect.height // 2

        self.vel_x = vel_x
        self.vel_y = vel_y

        self.alive_time = alive_time
        self.freezed_time = None

        self.gl = Globals()

        self.freezed = False


    def update(self, *args):
        if self.freezed:
            if time.time() - self.freezed_time >= self.alive_time:
                self.kill()
            return
        self.vel_y -= self.gl.gravity / self.gl.fps
        if self.vel_x - self.gl.air_friction / self.gl.fps > 0:
            self.vel_x -= self.gl.air_friction / self.gl.fps
        else:
            self.vel_x = 0

        self.rect.x += round(self.vel_x)
        self.rect.y -= round(self.vel_y)

        if self.rect.x > self.gl.scr_width or self.rect.y + self.rect.height > Globals.gun_bottom:
            self.rect.y = Globals.gun_bottom - self.rect.height
            self.freezed = True
            self.freezed_time = time.time()
            # self.kill()