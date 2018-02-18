import pygame, json
from GlobalVariables import Globals
from GameClasses.Cannon import Cannon


class CannonLoader:
    def __init__(self, path):
        self.path = path

    def load(self, filenames) -> list:
        all_cannons = []
        for json_filename in filenames:
            with open(self.path + json_filename, encoding='utf-8') as json_file:
                params = json.load(json_file)
            try:
                cannon = Cannon(params)
                all_cannons.append(cannon)
            except Exception as e:
                Globals.logger('e', ', '.join(e.args))
        return all_cannons