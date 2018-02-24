import pygame
import Constants
from GlobalVariables import Globals, scale
from Engine.ImageLoader import ImageLoader
from Engine.CannonLoader import CannonLoader
from GameClasses.Coin import Coin
from GameClasses.Target import Target
from GameClasses.Sprite import Sprite
from UI.GunButton import GunButton
from UI.TextLabel import TextLabel
from UI.Tooltip import Tooltip


class Game:
    def __init__(self):
        self.__name__ = 'Game'

    def init_ui(self):
        x = scale(300)
        can_number = 0
        for cannon in Globals.cannons:
            btn = GunButton(x, 'left', scale(10), 'bottom', 'ui_btn_gun',
                            Globals.cannons_params[cannon.name],
                            'ui_btn_gun_locked', 'ui_btn_gun_hovered', 'ui_btn_gun_pressed')
            tooltip = Tooltip(btn, 0, scale(-100), 'ui_tooltip', ['Имя: %s' % cannon.name,
                                                           'Очки: %s' % btn.score_unlock,
                                                           'Цена: %s' % btn.price])

            x += btn.rect.width + scale(5)
            can_number += 1
            Globals.ui.add(btn)
            Globals.ui.add(tooltip)

        ui_score = TextLabel(scale(20), 'left', scale(10), 'up')
        ui_score.set_font(50)
        ui_coins = TextLabel(scale(20), 'left', scale(20) + ui_score.text_rect.height, 'up')
        ui_coins.set_font(50)
        ui_straight = TextLabel(scale(20), 'left', scale(10) + Globals.gun_bottom, 'up')
        ui_straight.set_font(30)
        Globals.ui.add(ui_score, ui_coins, ui_straight)
        return ui_score, ui_coins, ui_straight

    def on_load(self):
        iml = ImageLoader('sprites/')
        # ----- Game sprites -----
        Globals.images = iml.load([('basic',        '_basic.png'),
                                   ('background',   'background_fullhd.png'),
                                   ('ground',       'ground.png'),
                                   ('ground_grass', 'ground_grass.png'),
                                   ('cannon_0',     'cannon_0.png'),
                                   ('cannon_0_pl',  'cannon_0_pl.png'),
                                   ('cannon_1',     'cannon_1.png'),
                                   ('cannon_1_pl',  'cannon_1_pl.png'),
                                   ('cannon_2',     'cannon_2.png'),
                                   ('cannon_2_pl',  'cannon_2_pl.png'),
                                   ('cannon_3',     'cannon_3.png'),
                                   ('cannon_3_pl',  'cannon_3_pl.png'),
                                   ('cannon_4',     'cannon_4.png'),
                                   ('cannon_4_pl',  'cannon_4_pl.png'),
                                   ('ball_0',       'ball_1.png'),
                                   ('ball_2',       'ball_2.png'),
                                   ('target_bronze','target_bronze.png'),
                                   ('target_silver','target_silver.png'),
                                   ('target_gold',  'target_gold.png'),
                                   ('coin_1',       'coin_1.png'),
                                   ('coin_2',       'coin_2.png'),
                                   ('coin_3',       'coin_3.png'),
                                   ('particle_1',   'particle_1.png'),
                                   ('particle_2',   'particle_2.png'),
                                   ('particle_3',   'particle_3.png'),
                                   ('particle_4',   'particle_4.png'),])
        # ---------- UI ----------
        Globals.images.update(iml.load([('ui_btn_gun',         'ui_btn_gun.png'),
                                        ('ui_btn_gun_hovered', 'ui_btn_gun_hovered.png'),
                                        ('ui_btn_gun_pressed', 'ui_btn_gun_pressed.png'),
                                        ('ui_btn_gun_locked',  'ui_btn_gun_locked.png'),
                                        ('ui_tooltip',         'ui_tooltip.png')]))
        # ------- UI Icons -------
        Globals.images.update(iml.load([('cannon_0_icon', 'cannon_0_icon.png'),
                                        ('cannon_1_icon', 'cannon_1_icon.png'),
                                        ('cannon_2_icon', 'cannon_2_icon.png'),
                                        ('cannon_3_icon', 'cannon_3_icon.png'),
                                        ('cannon_4_icon', 'cannon_4_icon.png')]))
        # --------- End ----------


        cnl = CannonLoader('data/')
        Globals.cannons = cnl.load(['cannon_0.json',
                                    'cannon_1.json',
                                    'cannon_2.json',
                                    'cannon_3.json',
                                    'cannon_4.json'])

    def run(self):
        pygame.init()

        self.on_load()
        ui_score, ui_coins, ui_straight = self.init_ui()
        Globals.logger('o', 'Game.run() - loading ok')

        sprg_bg = pygame.sprite.Group()     # Background sprites
        sprg_fg = pygame.sprite.Group()     # Foreground sprites

        background = Sprite(0, 0, 'background', sprg_bg)
        ground = Sprite(0, 0, 'ground', sprg_bg)
        grass =  Sprite(0, 0, 'ground_grass', sprg_fg)

        ground.set_pos(0, Globals.scr_height - ground.rect.height)
        grass.set_pos(0, ground.rect.y - grass.rect.height)

        cannon = Globals.cannons[Globals.cannon_current]
        cannon.shot_count = 0
        cannon_curr = Globals.cannon_current

        target_bronze = Target(Globals.targets_params['bronze'])
        target_silver = Target(Globals.targets_params['silver'])
        target_gold =   Target(Globals.targets_params['gold'])

        coin_1 = Coin(Globals.coins_params['coin_1'])
        coin_2 = Coin(Globals.coins_params['coin_2'])
        coin_3 = Coin(Globals.coins_params['coin_3'])

        Globals.spr_targets.add(target_bronze, target_silver, target_gold)
        Globals.spr_coins.add(coin_1, coin_2, coin_3)

        Globals.logger('o', 'Game.run() - All objects was initialized successfully')

        running = True
        while running:
            Globals.input.update()
            if pygame.K_ESCAPE in Globals.input.k_pressed:
                Globals.logger('o', 'Game.run() - Quitting, cannon shoots %s times' % str(cannon.shot_count))
                return Constants.EXC_MENU
            elif Globals.input.quit:
                Globals.logger('o', 'Game.run() - Quitting, cannon shoots %s times' % str(cannon.shot_count))
                return Constants.EXC_EXIT

            # ------ Cheats ------
            if pygame.K_m in Globals.input.k_pressed:
                Globals.logger('o', 'Game.run() - Cheat! More money')
                Globals.money += 20
            if pygame.K_n in Globals.input.k_pressed:
                Globals.logger('o', 'Game.run() - Cheat! More score')
                Globals.score += 20
            if pygame.K_EQUALS in Globals.input.k_pressed:
                Globals.logger('o', 'Game.run() - Cheat! Setting new cannon (+)')
                if Globals.cannon_current + 1 < len(Globals.cannons):
                    Globals.cannon_current += 1
            if pygame.K_MINUS in Globals.input.k_pressed:
                Globals.logger('o', 'Game.run() - Cheat! Setting new cannon (-)')
                if Globals.cannon_current != 0:
                    Globals.cannon_current -= 1
            # --------------------

            if cannon_curr != Globals.cannon_current:
                Globals.logger('o', 'Game.run() - Cannon changing, prev one shoot %s times' % str(cannon.shot_count))
                cannon = Globals.cannons[Globals.cannon_current]
                cannon.shot_count = 0
                cannon_curr = Globals.cannon_current
                Globals.logger('o', 'Game.run() - Cannon changed to %s' % str(cannon_curr))


            ui_score.set_text('  Очки: %s' % Globals.score)
            ui_coins.set_text('Деньги: %s' % Globals.money)
            ui_straight.set_text('Сила: {} - от {} до {}'.format(cannon.straigt,
                                                                          cannon.straigt_min,
                                                                          cannon.straigt_max))
            pygame.display.update()

            sprg_bg.draw(Globals.screen)

            for sp_group in Globals.sprites_groups:
                sp_group.update()
                sp_group.draw(Globals.screen)

            Globals.spr_targets.update()
            Globals.spr_targets.draw(Globals.screen)
            Globals.spr_coins.update()
            Globals.spr_coins.draw(Globals.screen)

            cannon.update()
            cannon.draw(Globals.screen)

            sprg_fg.draw(Globals.screen)

            Globals.ui.update()
            Globals.ui.draw(Globals.screen)

            Globals.clock.tick(Globals.fps)

        return Constants.EXC_EXIT
