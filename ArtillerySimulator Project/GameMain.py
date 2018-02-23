import pygame
import Constants
from GlobalVariables import Globals
from Scenes.Game import Game
from Scenes.Menu import Menu
from Scenes.HowToPlay import HowToPlayScene
from Scenes.StartScreen import StartScreen


class ScenesManager:
    def __init__(self):
        self.curr_scene = None
        pygame.init()

    def on_new_scene(self):
        Globals.score = 0
        Globals.money = 0
        Globals.spr_alive.empty()
        Globals.spr_particles.empty()
        Globals.spr_targets.empty()
        Globals.spr_coins.empty()
        Globals.ui.clear()

    def start(self):
        curr_scene = StartScreen()
        exit_code = curr_scene.run()
        if exit_code == 1:
            return
        elif exit_code == 2:
            self.run()

    def run_scene(self, scene):
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
    game.run()
    pygame.quit()
