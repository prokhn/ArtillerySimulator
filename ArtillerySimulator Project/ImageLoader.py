import pygame
from GlobalVariables import Globals


class ImageLoader:
    def __init__(self, im_path_to_tag=[]):
        # im_path_to_tag - [ (im_path, tag), ... ]
        loaded = {}
        for path, tag in im_path_to_tag:
            try:
                im = pygame.image.load(path).convert_alpha()
            except Exception as e:
                Globals.logger('e', ', '.join(e.args))
