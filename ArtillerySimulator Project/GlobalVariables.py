import pygame
from Engine.InputHandler import Input
from Engine.Logger import Logger
from UI.UIHandler import UIHandler
from Constants import *


def scale(num: int):
    return int(num * SCR_SCALE)

class Globals:
    # ---------- Screen ----------
    scr_abs_w = ABS_W
    scr_abs_h = ABS_H
    scr_width = SCR_W
    scr_height = SCR_H
    scr_scale = scr_width / scr_abs_w
    fullscreen = FULLSCREEN
    if fullscreen:
        screen = pygame.display.set_mode((scr_width, scr_height), pygame.FULLSCREEN)
    else:
        screen = pygame.display.set_mode((scr_width, scr_height))
    pygame.display.set_caption('Artillery Simulator')
    icon = pygame.image.load('sprites/_icon.png')
    pygame.display.set_icon(icon)
    # ----------------------------

    # ----------- Images ---------
    images = {}
    # ----------------------------

    # --------- Classes ----------
    input = Input()
    logger = Logger(time_need=True, immed_write=False, to_conlose=False)
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
    targets_params = {'bronze': ['target_bronze', 5,  scale(275),  scale(700),  scale(100), scale(900)],
                      'silver': ['target_silver', 10, scale(900),  scale(1500), scale(200), scale(800)],
                      'gold':   ['target_gold',   20, scale(1600), scale(1860), scale(150), scale(800)]}
    # Coins   - Coin_name: [img_tag, value, minx, maxx, miny, maxy]
    coins_params = {'coin_1': ['coin_1', 1, scale(100),  scale(1300), scale(100), scale(800)],
                    'coin_2': ['coin_2', 2, scale(700),  scale(1850), scale(50),  scale(600)],
                    'coin_3': ['coin_3', 3, scale(1500), scale(1850), scale(10),  scale(400)]}
    # ----------------------------

    # -------- Game Logic --------
    score = 0
    money = 0
    gravity = scale(25)
    air_friction = 1
    gun_left = scale(10)
    gun_bottom = scale(960)
    particles_count = 7
    particles_image_tags = ['particle_1', 'particle_2', 'particle_3', 'particle_4']
    spr_alive = pygame.sprite.Group()
    spr_particles = pygame.sprite.Group()
    spr_targets = pygame.sprite.Group()
    spr_coins = pygame.sprite.Group()
    sprites_groups = [spr_alive, spr_particles]
    # ----------------------------

    logger('o', 'Globals class initialized, scr_scale is %s' % str(round(scr_scale, 3)))
    logger('o', 'Other params: scr_width = {}, scr_height = {}'.format(scr_width, scr_height))