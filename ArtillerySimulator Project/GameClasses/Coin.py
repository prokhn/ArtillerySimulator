import pygame, random
from GlobalVariables import Globals
from GameClasses.CollectableObject import CollectableObject


class Coin(CollectableObject):
    def __init__(self, params):
        image_tag, value, minx, maxx, miny, maxy = params
        super().__init__(image_tag, minx, maxx, miny, maxy)
        self.value = value

    def on_collect(self):
        super().on_collect()
        Globals.money += self.value
        self.on_destroy()
