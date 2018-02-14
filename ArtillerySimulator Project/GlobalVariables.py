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
    fps = 60
    # ----------------------------
    #---------cannons---------
    mass = [['sprites/cannon_0_pl.png', 'sprites/cannon_0_gun_d2.png', 0,0,90,1,10,10,50,2,(75,500),(-80,0),(110,0)], ['sprites/76-mm_zeni_lafett.png', 'sprites/76-mm_zenit_orudie.png', 0,0,90,1,50,10,50,2,(80,535),(-75,0),(70,0)]]
    gan_number = 1
    # -------- Game Logic --------
    gravity = 25
    air_friction = 1
    spr_alive = pygame.sprite.Group()
    sprites_groups = [spr_alive]
    # ----------------------------