import pygame
from InputHandler import Input
from Logger import Logger

class Globals:
    # ---------- Screen ----------
    scr_width = 1280
    scr_height = 720
    screen = pygame.display.set_mode((scr_width, scr_height))
    # ----------------------------

    # ----------- Images ---------
    images = {}
    # ----------------------------

    # --------- Classes ----------
    input = Input()
    logger = Logger()
    # ----------------------------

    # ----------- Time -----------
    clock = pygame.time.Clock()
    fps = 200
    # ----------------------------

    # -------- Game Logic --------
    gravity = 50
    air_friction = 1
    spr_alive = pygame.sprite.Group()
    sprites_groups = [spr_alive]
    # ----------------------------