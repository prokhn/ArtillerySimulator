import pygame, random
from GlobalVariables import Globals
from ImageLoader import ImageLoader
from GameClasses.Cannon import Cannon
from GameClasses.Coin import Coin

class Game:
    def __init__(self):
        pass

    def load_sprites(self):
        self.background = pygame.image.load('sprites/background_1280x720.png')
        self.ground = pygame.image.load('sprites/ground_smaller.png').convert_alpha()
        self.ground_grass = pygame.image.load('sprites/ground_grass.png').convert_alpha()

        iml = ImageLoader()
        spr_path = 'sprites/'
        Globals.images = iml.load([('basic', spr_path + '_basic.png')])


    def run(self):
        pygame.init()

        self.load_sprites()
        gl = Globals()
        print(gl.images)
        all_sprites = pygame.sprite.Group()

        coin = Coin(100, 100, 'skbvks', 10, all_sprites)

        cannon = Cannon(0, 0)
        cannon.pl_rect.x = 10
        cannon.pl_rect.y = gl.scr_height - self.ground.get_rect().height - cannon.pl_rect.height  +15

        #all_sprites.add(cannon)

        running = True
        while running:
            gl.input.update()
            if gl.input.quit:
                running = False
            pygame.display.update()

            gl.screen.blit(self.background, (0, 0))
            gl.screen.blit(self.ground, (0, gl.scr_height - self.ground.get_rect().height))
            gl.screen.blit(self.ground_grass, (0, gl.scr_height - self.ground.get_rect().height - self.ground_grass.get_rect().height))
            # gl.screen.blit(self.cannon, (10, gl.scr_height - self.ground.get_rect().height - self.cannon.get_rect().height))
            # curr_target = pygame.transform.scale(self.target, (100, 100))
            #gl.screen.blit(curr_target, (random.randint(500, 1100), random.randint(100, 500)))
            # gl.screen.blit(curr_target, (1000, 200))
            for sp_group in gl.sprites_groups:
                sp_group.update()
                sp_group.draw(gl.screen)

            cannon.update()
            cannon.draw(gl.screen)
            all_sprites.update()
            all_sprites.draw(gl.screen)

            gl.clock.tick(gl.fps)

        pygame.quit()
        gl.logger.save()



if __name__ == '__main__':
    game = Game()
    game.run()
