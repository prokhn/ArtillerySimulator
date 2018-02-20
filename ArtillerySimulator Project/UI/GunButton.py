import pygame
from GlobalVariables import Globals
from UI.Button import Button


class GunButton(Button):
    def __init__(self, x, x_align, y, y_align, img_bg, cannon_num, img_bg_hovered=None, img_bg_pressed=None):
        super(). __init__(x, x_align, y, y_align, img_bg, img_bg_hovered, img_bg_pressed)
        self.cannon_num = cannon_num

    def on_click_out(self, accept_click: bool):
        super().on_click_out(accept_click)
        if accept_click:
            Globals.cannon_current = self.cannon_num
