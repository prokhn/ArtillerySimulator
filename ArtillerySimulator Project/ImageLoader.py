import pygame
from GlobalVariables import Globals


class ImageLoader:
    def __init__(self, spr_path):
        self.spr_path = spr_path

    def load(self, im_path_to_tag):
        # im_path_to_tag - [ (im_path, tag), ... ]
        loaded = {}
        for tag, path in im_path_to_tag:
            try:
                im = pygame.image.load(self.spr_path + path).convert_alpha()
                loaded[tag] = im
            except Exception as e:
                Globals.logger('e', ', '.join(e.args))
        return loaded
