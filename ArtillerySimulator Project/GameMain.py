import pygame, random
from GlobalVariables import Globals
from ImageLoader import ImageLoader
from GameClasses.Cannon import Cannon
from GameClasses.Coin import Coin
from GameClasses.Sprite import Sprite

class Game:
    def __init__(self):
        pass

    def load_sprites(self):
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
                                   ('cannon_2_pl',  'cannon_2_pl.png')])


    def run(self):
        pygame.init()

        self.load_sprites()
        gl = Globals()

        all_sprites = pygame.sprite.Group()

        # coin = Coin(100, 100, 'skbvks', 10, all_sprites)

        # cannon = Cannon(0, 0)
        # cannon.pl_rect.x = 10
        # cannon.pl_rect.y = gl.scr_height - self.ground.get_rect().height - cannon.pl_rect.height  +15

        #all_sprites.add(cannon)

        background = Sprite(0, 0, 'background', all_sprites)
        ground = Sprite(0, 0, 'ground', all_sprites)
        grass =  Sprite(0, 0, 'ground_grass', all_sprites)

        ground.set_pos(0, gl.scr_height - ground.rect.height)
        grass.set_pos(0, ground.rect.y - grass.rect.height)

        running = True
        while running:
            gl.input.update()
            if pygame.K_ESCAPE in gl.input.k_pressed:
                running = False
                gl.input.quit = True
            elif gl.input.quit:
                running = False
            pygame.display.update()

            # gl.screen.blit(background, (0, 0))
            # gl.screen.blit(ground, (0, gl.scr_height - ground.get_rect().height))
            # gl.screen.blit(grass, (0, gl.scr_height - ground.get_rect().height - grass.get_rect().height))

            for sp_group in gl.sprites_groups:
                sp_group.update()
                sp_group.draw(gl.screen)

            # cannon.update()
            # cannon.draw(gl.screen)
            all_sprites.update()
            all_sprites.draw(gl.screen)

            gl.clock.tick(gl.fps)

        pygame.quit()
        gl.logger.save()



if __name__ == '__main__':
    game = Game()
    game.run()
