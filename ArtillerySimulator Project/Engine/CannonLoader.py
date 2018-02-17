import pygame, json
from GameClasses.Cannon import Cannon


class CannonLoader:
    def __init__(self):
        pass

    def load(self, filenames):
        all_cannons = []
        for json_file in filenames:
            params = json.load(json_file)
            cannon = Cannon(params)
            all_cannons.append(cannon)
        return all_cannons