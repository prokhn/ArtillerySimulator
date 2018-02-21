import pygame, math
from GlobalVariables import Globals
from GameClasses.CannonBall import CannonBall

def arg_strip(arg):
    return arg.strip()

class Pivot:
    def __init__(self, coords='', x=None, y=None):
        if coords != '':
            x, y = map(arg_strip, coords.split(','))
            x = int(x[1:])
            y = int(y[:-1])
        self.set_new(x, y)

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

        '''
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
        '''

        # ---------------------------------------------
        self.name = params['name']
        self.tilt = params['tilt']                      # Начальный наклон пушки
        self.tilt_min = params['tilt_min']              # Минимальный наклон
        self.tilt_max = params['tilt_max']              # Максимальный наклон
        self.tilt_delta = params['tilt_delta']          # Прибавка к наклону за одно нажатие клавиши
        self.straigt = params['straigt']                # Скорость вылетающего снаряда
        self.straigt_min = params['straigt_min']        # Минимальная
        self.straigt_max = params['straigt_max']        # Максимальная
        self.straigt_delta = params['straigt_delta']    # Прибавка за раз
        self.gun_rotc = Pivot(params['gun_rotc'])       # Координаты точки вращения пушки относительно центра
        self.plt_rotc = Pivot(params['plt_rotc'])       # Координаты ТВ пушки относительно лево-верх платформы
        self.ball_spawn = Pivot(params['ball_spawn'])   # Координаты спавна шарика отностительно центра
        self.img_gun = Globals.images[params['img_gun']]                # Картинка пушки
        self.img_platform = Globals.images[params['img_platform']]      # Картинка платформы
        self.img_ball = Globals.images[params['img_ball']]              # Картинка снаряда
        # ---------------------------------------------

        self.pl_rect = self.img_platform.get_rect()
        self.pl_rect.x = Globals.gun_left
        self.pl_rect.y = Globals.gun_bottom - self.pl_rect.height

        self.ball_spawn.set_new(self.ball_spawn.x - self.gun_rotc.x, self.ball_spawn.y + self.gun_rotc.y)

        self.gun_rot = self.img_gun
        self.pivot = Pivot(x=self.pl_rect.x + self.plt_rotc.x - self.gun_rotc.x,
                           y= self.pl_rect.y + self.plt_rotc.y - self.gun_rotc.y)


        self.rot_rect = self.gun_rot.get_rect()
        self.on_rotate()

    def on_rotate(self):
        self.gun_rot = pygame.transform.rotate(self.img_gun, self.tilt)
        self.rot_rect = self.gun_rot.get_rect()
        self.rot_rect.center = (self.pivot.x + self.gun_rotc.x, self.pivot.y + self.gun_rotc.y)
        dx = self.gun_rotc.dxy * math.cos(math.radians(self.tilt))
        dy = self.gun_rotc.dxy * math.sin(math.radians(self.tilt))
        self.rot_rect.x += dx
        self.rot_rect.y -= dy

    def update(self, *args):
        if 1 in Globals.input.m_pressed:
            # print(Globals.input.m_pos)
            pass
        if pygame.K_UP in Globals.input.k_hold:
            if self.tilt < self.tilt_max:
                self.tilt += 1
                self.on_rotate()
        elif pygame.K_DOWN in Globals.input.k_hold:
            if self.tilt > self.tilt_min:
                self.tilt -= 1
                self.on_rotate()

        if 4 in Globals.input.m_pressed:
            if self.straigt + self.straigt_delta <= self.straigt_max:
                self.straigt += self.straigt_delta
        elif 5 in Globals.input.m_pressed:
            if self.straigt - self.straigt_delta >= self.straigt_min:
                self.straigt -= self.straigt_delta

        if pygame.K_SPACE in Globals.input.k_pressed: # or pygame.K_SPACE in Globals.input.k_hold:
            # Это чертова тригонометрия
            # Не лезь, дибил курва сраный, она сожрет тебя!!!
            # Это не шутки, дружище, поверь, тут тебе не стандратная конструкция
            # Это самый настоящий ад!!!
            x = self.pivot.x + self.gun_rotc.x + self.ball_spawn.dxy * math.cos(math.radians(self.tilt))
            y = self.pivot.y - self.gun_rotc.y - self.ball_spawn.dxy * math.sin(math.radians(self.tilt))
            x -= self.ball_spawn.y * math.sin(math.radians(self.tilt))
            y -= self.ball_spawn.y * math.cos(math.radians(self.tilt))
            # Ты еще жив?
            # Тогда держи на закуску еще двоих
            x_vel = self.straigt * math.cos(math.radians(self.tilt))
            y_vel = self.straigt * math.sin(math.radians(self.tilt))
            # ЧЕРТОВА ТРИГОНОМЕТРИЯ, ДЖОННИ, ОНА ПРЯЧЕТСЯ В КОДЕ!
            # Впрочем, опасность миновала
            # Кажется, у нас почти нет потерь
            # Продолжаем вести наблюдение
            new_ball = CannonBall(x, y, x_vel, y_vel, self.img_ball)
            Globals.spr_alive.add(new_ball)

    def draw(self, screen: pygame.Surface):
        screen.blit(self.gun_rot, (self.rot_rect.x, self.rot_rect.y))
        screen.blit(self.img_platform, (self.pl_rect.x, self.pl_rect.y))

    def __repr__(self):
        return '<Cannon "{}">'.format(self.name)