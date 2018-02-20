import pygame
from InputHandler import Input
from Logger import Logger
from UI.UIHandler import UIHandler

class Globals:
    # ---------- Screen ----------
    scr_width = 1920
    scr_height = 1080
    screen = pygame.display.set_mode((scr_width, scr_height), pygame.FULLSCREEN)
    # ----------------------------

    # ----------- Images ---------
    images = {}
    # ----------------------------

    # --------- Classes ----------
    input = Input()
    logger = Logger()
    ui = UIHandler()
    # ----------------------------

    # ----------- Time -----------
    clock = pygame.time.Clock()
    fps = 60
    # ----------------------------

    # --------- Cannons ----------
    cannons = []
    cannon_current = 0
    # ----------------------------

    # -------- Game Logic --------
    gravity = 25
    air_friction = 1
    gun_left = 10
    gun_bottom = 960
    spr_alive = pygame.sprite.Group()
    sprites_groups = [spr_alive]
    # ----------------------------