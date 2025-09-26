from src.DSL.owtyping import *

global_functions = []
each_player_functions = []

class PlayerArray:
    def __init__(self):
        self._real = []
    def view(self):
        return self._real
    def adopt(self, iterable) -> None:
        self._real = list(iterable)

ALL_PLAYERS = PlayerArray()
