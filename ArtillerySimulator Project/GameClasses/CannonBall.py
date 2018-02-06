import pygame, time
from GlobalVariables import Globals

class CannonBall(pygame.sprite.Sprite):
    def __init__(self, pos, vel_x, vel_y, groups=None):
        if groups:
            super().__init__(groups)
        else:
            super().__init__()

        self.image = pygame.image.load('sprites/cannonball_small_16x.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = pos[0] - self.rect.width // 2
        self.rect.y = pos[1] - self.rect.height // 2

        self.vel_x = vel_x
        self.vel_y = vel_y

        self.gl = Globals()

        self.time_to_kill = 0
    def update(self, *args):
        if self.rect.y + 16 >= 600:
            if self.time_to_kill == 0:
                self.time_to_kill = time.time() + 3
            else:
                if time.time() >= self.time_to_kill:
                    self.kill()
            return

        if self.rect.x > self.gl.scr_width or self.rect.y > self.gl.scr_height:
            self.kill()
        self.vel_y -= self.gl.gravity / self.gl.fps
        if self.vel_x - self.gl.air_friction / self.gl.fps > 0:
            self.vel_x -= self.gl.air_friction / self.gl.fps
        else:
            self.vel_x = 0

        self.rect.x += round(self.vel_x)
        self.rect.y -= round(self.vel_y)