from overflow.DSL.owtyping import *

global_functions = []
each_player_functions = []

class PlayerArray:
    def __init__(self):
        self._real = []
    def view(self):
        return self._real
    def adopt(self, iterable) -> None:
        self._real = list(iterable)
    def __iter__(self):
        return iter(self._real)

ALL_PLAYERS = PlayerArray()
