import pygame, importlib
from GlobalVariables import Globals
from Scenes.Game import Game
from Scenes.Menu import Menu
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

    def run(self):
        self.on_new_scene()
        curr_scene = Menu()
        exit_code = curr_scene.run()
        if exit_code == 1:
            return
        elif exit_code == 2:
            self.on_new_scene()
            curr_scene = Game()
            exit_code = curr_scene.run()
            if exit_code == 1:
                return
            elif exit_code == 2:
                self.run()

if __name__ == '__main__':
    game = ScenesManager()
    game.run()
    pygame.quit()
