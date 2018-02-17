import pygame, math
from GlobalVariables import Globals
from GameClasses.CannonBall import CannonBall


class Pivot:
    def __init__(self, mass):
        self.set_new(mass[0], mass[1])

    def set_new(self, x, y):
        self.x = x
        self.y = y
        if x == 0 and y == 0:
            self.dxy = 0
            self.tilt_0 = 0
        else:
            self.dxy = math.sqrt(x ** 2 + y ** 2)
            self.tilt_0 = math.acos(self.x / self.dxy)

    def __repr__(self):
        return '<Pivot({}, {})>'.format(self.x, self.y)

class Cannon(pygame.sprite.Sprite):
    def __init__(self, params):
        super().__init__()

        # Different values for all cannons
        self.tilt = Globals.mass[Globals.gan_number][2]           # Начальный наклон пушки
        self.tilt_min = Globals.mass[Globals.gan_number][3]      # Минимальный наклон
        self.tilt_max = Globals.mass[Globals.gan_number][4]    # Максимальный наклон
        self.tilt_delta = Globals.mass[Globals.gan_number][5]     # Прибавка к наклону за одно нажатие клавиши
        self.straigt = Globals.mass[Globals.gan_number][6]       # Скорость вылетающего снаряда
        self.straigt_min = Globals.mass[Globals.gan_number][7]   # Минимальная
        self.straigt_max = Globals.mass[Globals.gan_number][8]   # Максимальная
        self.straigt_delta = Globals.mass[Globals.gan_number][9]  # Прибавка за раз
        self.rotation_center = Globals.mass[Globals.gan_number][10]        # Центр вращения пушки
        self.pivot = Pivot(Globals.mass[Globals.gan_number][11])              # Координаты точки вращения пушки относительно центра
        self.ball_spawn = Pivot(Globals.mass[Globals.gan_number][12])         # Координаты спавна шарика отностительно центра
        self.platform = Globals.images[Globals.mass[Globals.gan_number][0]]    # Картинка платформы
        self.gun = Globals.images[Globals.mass[Globals.gan_number][1]]     # Картинка пушки
        # ----------------------------------------

        self.ball_spawn.set_new(self.ball_spawn.x - self.pivot.x, self.ball_spawn.y + self.pivot.y)

        self.gun_rot = self.gun
        self.rotation_center = (self.rotation_center[0] - self.pivot.x,
                                self.rotation_center[1] - self.pivot.y)

        self.pl_rect = self.platform.get_rect()
        self.pl_rect.x = x
        self.pl_rect.y = y

        self.rot_rect = self.gun_rot.get_rect()
        self.on_rotate()
        self.gl = Globals()

    def on_rotate(self):
        self.gun_rot = pygame.transform.rotate(self.gun, self.tilt)
        self.rot_rect = self.gun_rot.get_rect()
        self.rot_rect.center = (self.rotation_center[0] + self.pivot.x, self.rotation_center[1] + self.pivot.y)
        dx = self.pivot.dxy * math.cos(math.radians(self.tilt))
        dy = self.pivot.dxy * math.sin(math.radians(self.tilt))
        self.rot_rect.x += dx
        self.rot_rect.y -= dy

    def update(self, *args):
        if 1 in self.gl.input.m_pressed:
            print(self.gl.input.m_pos)
        if pygame.K_UP in self.gl.input.k_hold:
            if self.tilt < self.tilt_max:
                self.tilt += 1
                self.on_rotate()
        elif pygame.K_DOWN in self.gl.input.k_hold:
            if self.tilt > self.tilt_min:
                self.tilt -= 1
                self.on_rotate()

        if 4 in self.gl.input.m_pressed:
            if self.straigt + self.straigt_delta <= self.straigt_max:
                self.straigt += self.straigt_delta
            print(self.straigt)
        elif 5 in self.gl.input.m_pressed:
            if self.straigt - self.straigt_delta >= self.straigt_min:
                self.straigt -= self.straigt_delta
            print(self.straigt)

        if pygame.K_SPACE in self.gl.input.k_pressed: # or pygame.K_SPACE in self.gl.input.k_hold:
            x = self.rotation_center[0] + self.pivot.x + self.ball_spawn.dxy * math.cos(math.radians(self.tilt))
            y = self.rotation_center[1] - self.pivot.y - self.ball_spawn.dxy * math.sin(math.radians(self.tilt))
            # print(self.rotation_center, x, y)
            x_vel = self.straigt * math.cos(math.radians(self.tilt))
            y_vel = self.straigt * math.sin(math.radians(self.tilt))
            new_ball = CannonBall((x, y), x_vel, y_vel)
            self.gl.spr_alive.add(new_ball)

    def draw(self, screen: pygame.Surface):
        screen.blit(self.gun_rot, (self.rot_rect.x, self.rot_rect.y))
        screen.blit(self.platform, (self.pl_rect.x, self.pl_rect.y))