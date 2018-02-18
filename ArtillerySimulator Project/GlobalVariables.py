import pygame
from InputHandler import Input
from Logger import Logger

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
    # ----------------------------

    # ----------- Time -----------
    clock = pygame.time.Clock()
    fps = 60
    # ----------------------------

    # --------- Cannons ----------
    cannons = []
    cannon_current = 0
    # mass = [['cannon_0_pl', 'cannon_0', 0,0,90,1,12,10,12,2,(75,850),(-80,0),(110,0)],
    #         ['76-mm', 'sprites/76-mm_', 0,0,50,1,20,10,20,2,(80,540),(-65,0),(70,0)],
    #         ['152', 'sprites/152-mm_g', 0,0,50,1,60,10,60,2,(155,550),(-50,0),(90,0)]]

    # -------- Game Logic --------
    gravity = 25
    air_friction = 1
    gun_left = 10
    gun_bottom = 960
    spr_alive = pygame.sprite.Group()
    sprites_groups = [spr_alive]
    # ----------------------------