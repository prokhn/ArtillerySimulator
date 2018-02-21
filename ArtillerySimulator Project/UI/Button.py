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

        if img_bg:
            self.img_bg = Globals.images[img_bg]
            self.rect = self.img_bg.get_rect()
        else:
            self.img_bg = None
            self.rect = pygame.Rect(x, y, 0, 0)
        if img_bg_hovered:
            self.img_bg_hovered = Globals.images[img_bg_hovered]
        else:
            self.img_bg_hovered = None
        if img_bg_pressed:
            self.img_bg_pressed = Globals.images[img_bg_pressed]
        else:
            self.img_bg_pressed = None

        self.update_coords(x, x_align, y, y_align)

        self.icon = None
        self.icon_rect = pygame.Rect(0, 0, 0, 0)
        self.text = ''
        self.font = pygame.font.Font(None, 30)
        self.text_rendered = self.font.render(self.text, 1, pygame.Color('black'))
        self.text_rect = self.text_rendered.get_rect()
        self.text_rect.centerx = self.rect.centerx
        self.text_rect.centery = self.rect.centery

        self.enabled = True
        self.hovered = False
        self.clicked = False
        self.doing_action = False

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

    def set_text(self, text, font_size=None):
        self.text = text
        if font_size:
            self.set_font(font_size)

        self.text_rendered = self.font.render(self.text, 10, pygame.Color('black'))
        self.text_rect = self.text_rendered.get_rect()
        self.text_rect.x = self.rect.x
        self.text_rect.y = self.rect.y

    def set_text_rect(self, x, x_align, y, y_align):
        if x_align == 'left':
            self.text_rect.x = self.rect.x + x
        elif x_align == 'center':
            self.text_rect.centerx = self.rect.centerx
        elif x_align == 'right':
            self.text_rect.x = self.rect.x - x
        else:
            raise ValueError('Button.set_text_rect(): incorrect x_align - %s' % x_align)


        if y_align == 'up':
            self.text_rect.y = self.rect.y + y
        elif y_align == 'center':
            self.text_rect.centery = self.rect.centery
        elif y_align == 'bottom':
            self.text_rect.y = self.rect.y - self.rect.height - y
        else:
            raise ValueError('Button.set_text_rect(): incorrect y_align - %s' % y_align)

    def set_font(self, font_size):
        self.font = pygame.font.Font(None, font_size)
        self.set_text(self.text)

    def update(self):
        if self.doing_action:
            self.doing_action = False
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
        if self.img_bg:
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
            screen.blit(self.text_rendered, self.text_rect.topleft)

    def action(self):
        self.doing_action = True

    def on_mouse_enter(self):
        self.hovered = True

    def on_mouse_exit(self):
        self.hovered = False

    def on_click(self):
        self.clicked = True

    def on_click_out(self, accept_click: bool):
        self.clicked = False
        if accept_click:
            self.action()