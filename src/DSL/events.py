from functools import wraps
from src.DSL.owglobals import *
from src.DSL.ctx_event_player import *


def ongoing_global(func):
    cond = []

    @wraps(func)
    def wrapper(*conditions):
        nonlocal cond
        cond = conditions
        if all(conditions):
            func()

    wrapper._func = func
    wrapper._conditions = cond
    global_functions.append(wrapper)

    return wrapper


def ongoing_each_player(TEAM: Team, PLAYER: Player):
    def real_decorator(func):
        cond = []

        @wraps(func)
        def wrapper(*conditions):
            nonlocal cond
            cond = conditions
            for player in ALL_PLAYERS:
                if TEAM == ALL or player.TEAM == TEAM:
                    if PLAYER == ALL or player.SLOT == PLAYER or player.HERO == PLAYER:
                        with with_event_player(player):
                            if all(conditions):
                                func(player)

        wrapper._func = func
        wrapper._team = TEAM
        wrapper._player = PLAYER
        wrapper._conditions = cond
        each_player_functions.append(wrapper)
        return wrapper

    return real_decorator
