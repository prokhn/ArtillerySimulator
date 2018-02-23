import pygame
import Constants
from GlobalVariables import Globals
from Scenes.Game import Game
from Scenes.Menu import Menu
from Scenes.HowToPlay import HowToPlayScene


class ScenesManager:
    def __init__(self):
        self.curr_scene = None
        pygame.init()

    def on_new_scene(self):
        Globals.score = 0
        Globals.money = 0
        Globals.cannon_current = 0
        Globals.spr_alive.empty()
        Globals.spr_particles.empty()
        Globals.spr_targets.empty()
        Globals.spr_coins.empty()
        Globals.ui.clear()
        Globals.logger('o', 'ScenesManager.on_new_scene() Globals was reset')

    def run_scene(self, scene):
        Globals.logger('o', 'ScenesManager.run_scene() runs %s scene' % scene.__name__)
        self.on_new_scene()
        self.curr_scene = scene
        exit_code = self.curr_scene.run()
        if exit_code == Constants.EXC_EXIT:
            return
        elif exit_code == Constants.EXC_MENU:
            self.run_scene(Menu())
        elif exit_code == Constants.EXC_ABOUT:
            self.run_scene(HowToPlayScene())
        elif exit_code == Constants.EXC_GAME:
            self.run_scene(Game())

    def run(self):
        self.run_scene(Menu())

if __name__ == '__main__':
    game = ScenesManager()
    try:
        game.run()
        Globals.logger('o', 'Game was closed without errors')
    except Exception as e:
        Globals.logger('e', 'Some error occurred during the game!!')
        Globals.logger('e', 'Args is {}'.format(e.args[0]))

    pygame.quit()
    Globals.logger('o', 'Pygame.quit() ok, saving logs and quitting the program')
    Globals.logger.save()
