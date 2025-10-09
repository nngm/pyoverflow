from overflow import *

class player(player_parent):
    hasMoved: bool

ALL_PLAYERS.adopt([player() for _ in range(12)])
event_player = cast(player, event_player)

class Global(metaclass=WorkshopVarMeta):
    foo: string
    bar: list[number]

@ongoing_global
def init_global_variables():
    Global.foo = custom_string("bar")
    Global.bar[0] = 123

@ongoing_each_player(ALL_TEAMS, ALL)
@rules(
    is_button_held(event_player, button(MELEE)),
    count_of(filtered_array(all_players(ALL_TEAMS), CURRENT_ARRAY_ELEMENT.hasMoved)) > 1,
)
def let_player_minigame(event_player: player):
    event_player.Punch = True

if __name__ == "__main__":
    print(bool(compare(1,">",0)))
