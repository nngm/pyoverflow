from src.overwatch import *

class player(player_parent):
    def __init__(self):
        super().__init__()
        self.hasMoved = False

ALL_PLAYERS.adopt([player() for _ in range(12)])

class Global:
    foo = None


@ongoing_global
def init_global_variables():
    Global.foo = custom_string("bar")

@ongoing_each_player(ALL_TEAMS, ALL)
@rules(
    is_button_held(event_player, button(MELEE)),
    compare(
        count_of(
            filtered_array(
                all_players(ALL_TEAMS), 
                CURRENT_ARRAY_ELEMENT.hasMoved
            )
        ), 
        ">", 
        1
    )
)
def let_player_minigame():
    event_player.Punch = True

if __name__ == "__main__":
    print(bool(compare(1,">",0)))
