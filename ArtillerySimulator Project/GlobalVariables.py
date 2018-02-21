import pygame
from Engine.InputHandler import Input
from Engine.Logger import Logger
from UI.UIHandler import UIHandler

class Globals:
    # ---------- Screen ----------
    scr_width = 1920
    scr_height = 1080
    fullscreen = True
    if fullscreen:
        screen = pygame.display.set_mode((scr_width, scr_height), pygame.FULLSCREEN)
    else:
        screen = pygame.display.set_mode((scr_width, scr_height))
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

    # ---------- Params ----------
    # Cannons - Cannon.name: [button_icon, icon_borders, cannon_number, score_to_unlock, price]
    cannons_params = {'Cannon 0': ['cannon_0_icon', 10, 0, 0, 0],
                      'Cannon 1': ['cannon_1_icon', 10, 1, 10, 0],
                      'Cannon 2': ['cannon_2_icon', 10, 2, 20, 0],
                      'Cannon 3': ['cannon_3_icon', 10, 3, 30, 20]}
    # Targets - rang: [img_tag, score_adds, minx, maxx, miny, maxy]
    targets_params = {'bronze': ['target_bronze', 5, 275, 700, 100, 900],
                      'silver': ['target_silver', 10, 900, 1500, 200, 800],
                      'gold':   ['target_gold', 20, 1600, 1860, 150, 800]}
    # Coins   - Coin_name: [img_tag, value, minx, maxx, miny, maxy]
    coins_params = {'coin_1': ['coin_1', 1, 100, 1850, 100, 800],
                    'coin_2': ['coin_2', 2, 700, 1850, 50, 600],
                    'coin_3': ['coin_3', 3, 1500, 1850, 10, 400]}
    # ----------------------------

    # -------- Game Logic --------
    score = 100
    money = 100
    gravity = 25
    air_friction = 1
    gun_left = 10
    gun_bottom = 960
    particles_count = 5
    particles_image_tags = ['particle_1', 'particle_2', 'particle_3', 'particle_4']
    spr_alive = pygame.sprite.Group()
    spr_particles = pygame.sprite.Group()
    spr_targets = pygame.sprite.Group()
    spr_coins = pygame.sprite.Group()
    sprites_groups = [spr_alive, spr_particles]
    # ----------------------------