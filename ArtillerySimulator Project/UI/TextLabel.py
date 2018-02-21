import pygame
from GlobalVariables import Globals
from UI.Button import Button

class TextLabel(Button):
    def __init__(self, x, x_align, y, y_align, text=''):
        super().__init__(x, x_align, y, y_align, None)
        super().set_text(text)

    def update(self):
        super().update()

