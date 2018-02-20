import pygame
from GlobalVariables import Globals
from ImageLoader import ImageLoader
from Engine.CannonLoader import CannonLoader
from GameClasses.Cannon import Cannon
from GameClasses.Coin import Coin
from GameClasses.Target import Target
from GameClasses.Sprite import Sprite
from UI.GunButton import GunButton

class Game:
    def __init__(self):
        pass

    def init_ui(self):
        x = 300
        can_number = 0
        for cannon in Globals.cannons:
            btn = GunButton(x, 'left', 10, 'bottom', 'ui_btn_gun',
                            Globals.cannons_params[cannon.name],
                            'ui_btn_gun_locked', 'ui_btn_gun_hovered', 'ui_btn_gun_pressed')
            x += btn.rect.width + 5
            can_number += 1
            Globals.ui.add(btn)

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
                                   ('ball_0',       'ball_1.png'),
                                   ('target_bronze','target_bronze.png'),
                                   ('target_silver','target_silver.png'),
                                   ('target_gold',  'target_gold.png'),
                                   ('coin_1',       'coin_1.png'),
                                   ('coin_2',       'coin_2.png'),
                                   ('coin_3',       'coin_3.png')])
        # ---------- UI ----------
        Globals.images.update(iml.load([('ui_btn_gun',         'ui_btn_gun.png'),
                                        ('ui_btn_gun_hovered', 'ui_btn_gun_hovered.png'),
                                        ('ui_btn_gun_pressed', 'ui_btn_gun_pressed.png'),
                                        ('ui_btn_gun_locked', 'ui_btn_gun_locked.png')]))
        # ------- UI Icons -------
        Globals.images.update(iml.load([('cannon_0_icon', 'cannon_0_icon.png'),
                                        ('cannon_1_icon', 'cannon_1_icon.png'),
                                        ('cannon_2_icon', 'cannon_2_icon.png'),
                                        ('cannon_3_icon', 'cannon_3_icon.png')]))
        # --------- End ----------


        cnl = CannonLoader('data/')
        Globals.cannons = cnl.load(['cannon_0.json',
                                    'cannon_1.json',
                                    'cannon_2.json',
                                    'cannon_3.json'])
        Globals.logger('o', 'Game.on_load() ok. Loaded {} cannons'.format(len(Globals.cannons)))


    def run(self):
        pygame.init()

        self.on_load()
        self.init_ui()

        sprg_bg = pygame.sprite.Group()     # Background sprites
        sprg_fg = pygame.sprite.Group()     # Foreground sprites

        # coin = Coin(100, 100, 'skbvks', 10, all_sprites)
        #all_sprites.add(cannon)

        background = Sprite(0, 0, 'background', sprg_bg)
        ground = Sprite(0, 0, 'ground', sprg_bg)
        grass =  Sprite(0, 0, 'ground_grass', sprg_fg)

        ground.set_pos(0, Globals.scr_height - ground.rect.height)
        grass.set_pos(0, ground.rect.y - grass.rect.height)

        cannon = Globals.cannons[Globals.cannon_current]
        cannon_curr = Globals.cannon_current

        target_bronze = Target(Globals.targets_params['bronze'])
        target_silver = Target(Globals.targets_params['silver'])
        target_gold =   Target(Globals.targets_params['gold'])

        coin_1 = Coin(Globals.coins_params['coin_1'])
        coin_2 = Coin(Globals.coins_params['coin_2'])
        coin_3 = Coin(Globals.coins_params['coin_3'])

        Globals.spr_targets.add(target_bronze, target_silver, target_gold)
        Globals.spr_coins.add(coin_1, coin_2, coin_3)

        running = True
        while running:
            Globals.input.update()
            if pygame.K_ESCAPE in Globals.input.k_pressed:
                running = False
                Globals.input.quit = True
            elif Globals.input.quit:
                running = False

            if pygame.K_EQUALS in Globals.input.k_pressed:
                if Globals.cannon_current + 1 < len(Globals.cannons):
                    Globals.cannon_current += 1
                    cannon = Globals.cannons[Globals.cannon_current]
            if pygame.K_MINUS in Globals.input.k_pressed:
                if Globals.cannon_current != 0:
                    Globals.cannon_current -= 1
                    cannon = Globals.cannons[Globals.cannon_current]

            if cannon_curr != Globals.cannon_current:
                cannon = Globals.cannons[Globals.cannon_current]
                cannon_curr = Globals.cannon_current

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

        pygame.quit()
        Globals.logger.save()



if __name__ == '__main__':
    game = Game()
    game.run()
