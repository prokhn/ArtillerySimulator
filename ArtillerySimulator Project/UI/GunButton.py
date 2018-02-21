import pygame
from GlobalVariables import Globals
from UI.Button import Button


class GunButton(Button):
    def __init__(self, x, x_align, y, y_align, img_bg, params, img_bg_locked, img_bg_hovered=None, img_bg_pressed=None):
        super(). __init__(x, x_align, y, y_align, img_bg, img_bg_hovered, img_bg_pressed)
        self.set_icon(params[0], params[1])
        self.cannon_num = params[2]
        self.score_unlock = params[3]
        self.price = params[4]
        self.img_bg_locked = Globals.images[img_bg_locked]
        self.locked = True
        self.update()

    def update(self):
        if Globals.score >= self.score_unlock and Globals.money >= self.price:
            self.locked = False
        super().update()

    def draw(self, screen: pygame.Surface):
        if self.locked:
            screen.blit(self.img_bg_locked, self.rect.topleft)
        else:
            super().draw(screen)


    def on_click_out(self, accept_click: bool):
        super().on_click_out(accept_click)
        if accept_click:
            if not self.locked:
                Globals.cannon_current = self.cannon_num
                Globals.money -= self.price
