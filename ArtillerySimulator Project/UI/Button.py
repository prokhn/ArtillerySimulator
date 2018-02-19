import pygame
from GlobalVariables import Globals

class Button(pygame.sprite.Sprite):
    def __init__(self, x, x_align, y, y_align, img_bg, icon=None, text=''):
        super().__init__()

        self.x_abs = x
        self.y_abs = y
        self.x = 0
        self.y = 0
        self.x_align = x_align
        self.y_align = y_align

        self.img_bg = Globals.images[img_bg]
        self.rect = self.img_bg.get_rect()
        # self.rect = pygame.Rect()

        self.update_coords(x, x_align, y, y_align)

        if icon:
            self.icon = Globals.images[icon]
        else:
            self.icon = None

        self.text = text

        self.enabled = True
        self.hovered = False
        self.clicked = False

    def update_coords(self, x=None, x_align=None, y=None, y_align=None):
        if x_align:
            self.x_align = x_align
        if not x:
            x = self.x_abs

        if self.x_align == 'left':
            self.x = x
        elif self.x_align == 'center':
            self.x = (Globals.scr_width - self.rect.width) // 2 + x
        elif self.x_align == 'right':
            self.x = Globals.scr_width - x
        else:
            raise ValueError('Button.init(): incorrect x_align - %s' % x_align)

        if y_align:
            self.y_align = y_align
        if not y:
            y = self.y_abs

        if self.y_align == 'up':
            self.y = y
        elif self.y_align == 'center':
            self.y = (Globals.scr_height - self.rect.height) // 2 + y
        elif self.y_align == 'bottom':
            self.y = Globals.scr_height - y
        else:
            raise ValueError('Button.init(): incorrect y_align - %s' % y_align)

        self.rect.x = self.x
        self.rect.y = self.y

    def update(self, *args):
        self.img_bg = pygame.Surface()
        self.rect = pygame.Rect()

        if self.enabled:
            if self.rect.collidepoint(*Globals.input.m_pos):
                if not self.hovered:
                    self.on_mouse_enter()
                if 1 in Globals.input.m_pressed:
                    self.on_click()
            else:
                if self.hovered:
                    self.on_mouse_exit()

    def on_mouse_enter(self):
        self.hovered = True

    def on_mouse_exit(self):
        self.hovered = False

    def on_click(self):
        self.clicked = True