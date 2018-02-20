import pygame
from GlobalVariables import Globals

class Button:
    def __init__(self, x, x_align, y, y_align, img_bg, img_bg_hovered=None, img_bg_pressed=None):
        super().__init__()

        self.x_abs = x
        self.y_abs = y
        self.x = 0
        self.y = 0
        self.x_align = x_align
        self.y_align = y_align

        self.img_bg = Globals.images[img_bg]
        self.rect = self.img_bg.get_rect()
        if img_bg_hovered:
            self.img_bg_hovered = Globals.images[img_bg_hovered]
        else:
            self.img_bg_hovered = None
        if img_bg_pressed:
            self.img_bg_pressed = Globals.images[img_bg_pressed]
        else:
            self.img_bg_pressed = None

        self.icon = None
        self.icon_rect = pygame.Rect(0, 0, 0, 0)
        self.text = None
        self.font = pygame.font.Font(None, 10)

        self.update_coords(x, x_align, y, y_align)

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
            self.y = Globals.scr_height - self.rect.height - y
        else:
            raise ValueError('Button.init(): incorrect y_align - %s' % y_align)

        self.rect.x = self.x
        self.rect.y = self.y

    def set_icon(self, icon, borders):
        self.icon = Globals.images[icon]
        self.icon = pygame.transform.scale(self.icon, (self.rect.width - 2 * borders, self.rect.height - 2 * borders))
        self.icon_rect = self.icon.get_rect()
        self.icon_rect.center = self.rect.center

    def set_text(self):
        pass

    def update(self):
        # self.img_bg = pygame.Surface()
        # self.rect = pygame.Rect()

        if self.enabled:
            if self.rect.collidepoint(*Globals.input.m_pos):
                if not self.hovered:
                    self.on_mouse_enter()
                if 1 in Globals.input.m_pressed:
                    self.on_click()
                elif 1 in Globals.input.m_hold:
                    pass
                else:
                    if self.clicked:
                        self.on_click_out(True)
            else:
                if self.hovered:
                    self.on_mouse_exit()
                if self.clicked:
                    self.on_click_out(False)

    def draw(self, screen: pygame.Surface):
        screen.blit(self.img_bg, self.rect.topleft)
        if self.hovered:
            if self.img_bg_hovered:
                screen.blit(self.img_bg_hovered, self.rect.topleft)
        if self.clicked:
            if self.img_bg_pressed:
                screen.blit(self.img_bg_pressed, self.rect.topleft)
        if self.icon:
            screen.blit(self.icon, self.icon_rect.topleft)
        if self.text:
            self.font.render(self.text, 0, pygame.Color('white'))

    def on_mouse_enter(self):
        self.hovered = True

    def on_mouse_exit(self):
        self.hovered = False

    def on_click(self):
        self.clicked = True

    def on_click_out(self, accept_click: bool):
        self.clicked = False