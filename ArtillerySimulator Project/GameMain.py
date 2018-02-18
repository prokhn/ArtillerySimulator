import pygame
from GlobalVariables import Globals
from ImageLoader import ImageLoader
from Engine.CannonLoader import CannonLoader
from GameClasses.Cannon import Cannon
from GameClasses.Coin import Coin
from GameClasses.Sprite import Sprite

class Game:
    def __init__(self):
        pass

    def on_load(self):
        # self.background = pygame.image.load('sprites/background_1280x720.png')
        # self.ground = pygame.image.load('sprites/ground_smaller.png').convert_alpha()
        # self.ground_grass = pygame.image.load('sprites/ground_grass.png').convert_alpha()

        iml = ImageLoader('sprites/')
        Globals.images = iml.load([('basic',        '_basic.png'),
                                   ('background',   'background_fullhd.png'),
                                   ('ground', 'ground.png'),
                                   ('ground_grass', 'ground_grass.png'),
                                   ('cannon_0',     'cannon_0.png'),
                                   ('cannon_0_pl',  'cannon_0_pl.png'),
                                   ('cannon_1',     'cannon_1.png'),
                                   ('cannon_1_pl',  'cannon_1_pl.png'),
                                   ('cannon_2',     'cannon_2.png'),
                                   ('cannon_2_pl',  'cannon_2_pl.png'),
                                   ('cannon_3', 'cannon_3.png'),
                                   ('cannon_3_pl', 'cannon_3_pl.png'),
                                   ('ball_0',       'ball_1.png')])
        cnl = CannonLoader('data/')
        Globals.cannons = cnl.load(['cannon_0.json',
                                    'cannon_1.json',
                                    'cannon_2.json',
                                    'cannon_3.json'])
        Globals.logger('o', 'Game.on_load() ok. Loaded {} cannons'.format(len(Globals.cannons)))



    def run(self):
        pygame.init()

        self.on_load()
        gl = Globals()

        sprg_bg = pygame.sprite.Group()     # Background sprites
        sprg_fg = pygame.sprite.Group()     # Foreground sprites

        # coin = Coin(100, 100, 'skbvks', 10, all_sprites)
        #all_sprites.add(cannon)

        background = Sprite(0, 0, 'background', sprg_bg)
        ground = Sprite(0, 0, 'ground', sprg_bg)
        grass =  Sprite(0, 0, 'ground_grass', sprg_fg)

        ground.set_pos(0, gl.scr_height - ground.rect.height)
        grass.set_pos(0, ground.rect.y - grass.rect.height)

        cannon = Globals.cannons[Globals.cannon_current]
        # cannon = Cannon(0, 0)
        # cannon.pl_rect.x = 10
        # cannon.pl_rect.y = ground.rect.y - cannon.pl_rect.height
        # print(cannon.pl_rect)


        running = True
        while running:
            gl.input.update()
            if pygame.K_ESCAPE in gl.input.k_pressed:
                running = False
                gl.input.quit = True
            elif gl.input.quit:
                running = False

            if pygame.K_EQUALS in gl.input.k_pressed:
                if Globals.cannon_current + 1 < len(Globals.cannons):
                    Globals.cannon_current += 1
                    cannon = Globals.cannons[Globals.cannon_current]
            if pygame.K_MINUS in gl.input.k_pressed:
                if Globals.cannon_current != 0:
                    Globals.cannon_current -= 1
                    cannon = Globals.cannons[Globals.cannon_current]

            pygame.display.update()

            # gl.screen.blit(background, (0, 0))
            # gl.screen.blit(ground, (0, gl.scr_height - ground.get_rect().height))
            # gl.screen.blit(grass, (0, gl.scr_height - ground.get_rect().height - grass.get_rect().height))

            sprg_bg.draw(gl.screen)

            for sp_group in gl.sprites_groups:
                sp_group.update()
                sp_group.draw(gl.screen)

            cannon.update()
            cannon.draw(gl.screen)

            sprg_fg.draw(gl.screen)

            gl.clock.tick(gl.fps)

        pygame.quit()
        gl.logger.save()



if __name__ == '__main__':
    game = Game()
    game.run()
