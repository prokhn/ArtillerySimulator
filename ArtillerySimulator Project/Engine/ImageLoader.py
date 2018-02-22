import pygame
from GlobalVariables import Globals


class ImageLoader:
    def __init__(self, spr_path):
        self.spr_path = spr_path

    def load(self, im_path_to_tag):
        # im_path_to_tag - [ (im_path, tag), ... ]
        if Globals.scr_scale != 1:
            scale = True
        else:
            scale = False
        loaded = {}
        for tag, path in im_path_to_tag:
            try:
                im = pygame.image.load(self.spr_path + path).convert_alpha()
                if scale:
                    w, h = im.get_rect().size
                    im = pygame.transform.scale(im, (int(w * Globals.scr_scale), int(h * Globals.scr_scale)))
                loaded[tag] = im
            except Exception as e:
                Globals.logger('e', ', '.join(e.args))
        return loaded
