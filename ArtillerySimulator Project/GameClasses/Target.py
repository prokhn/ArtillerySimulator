import pygame, random
from GlobalVariables import Globals
from GameClasses.CollectableObject import CollectableObject


class Target(CollectableObject):
    def __init__(self, params):
        image_tag, score_adds, minx, maxx, miny, maxy = params
        super().__init__(image_tag, minx, maxx, miny, maxy)
        self.score_adds = score_adds

    def on_collect(self):
        super().on_collect()
        Globals.score += self.score_adds
        self.on_destroy()
        