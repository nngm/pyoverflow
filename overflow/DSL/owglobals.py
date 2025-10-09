from overflow.DSL.owtyping import *

global_functions = []
each_player_functions = []

class PlayerArray(List[player_parent]):
    def view(self):
        return self
    def adopt(self, iterable) -> None:
        self.clear()
        self.extend(iterable)

ALL_PLAYERS = PlayerArray()
