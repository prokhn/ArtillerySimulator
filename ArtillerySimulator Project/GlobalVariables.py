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
    # Cannon.name: [button_icon, icon_borders, cannon_number, score_to_unlock, price]
    cannons_params = {'Cannon 0': ['cannon_0_icon', 10, 0, 0, 0],
                      'Cannon 1': ['cannon_1_icon', 10, 1, 0, 0],
                      'Cannon 2': ['cannon_2_icon', 10, 2, 0, 0],
                      'Cannon 3': ['cannon_3_icon', 10, 3, 1, 0]}
    # ----------------------------

    # -------- Game Logic --------
    score = 0
    money = 0
    gravity = 25
    air_friction = 1
    gun_left = 10
    gun_bottom = 960
    spr_alive = pygame.sprite.Group()
    sprites_groups = [spr_alive]
    # ----------------------------