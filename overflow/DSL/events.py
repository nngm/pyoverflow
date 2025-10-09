import inspect
from functools import wraps
from overflow.DSL.owglobals import *
from overflow.DSL.ctx_event_player import *


def ongoing_global(func):
    conditions = getattr(func, "_rules", [])

    @wraps(func)
    def wrapper():
        if all(conditions):
            func()

    wrapper._func = func
    wrapper._conditions = conditions
    global_functions.append(wrapper)

    return wrapper


def ongoing_each_player(TEAM: Team, PLAYER: Player):
    def real_decorator(func):
        conditions = getattr(func, "_rules", [])

        sig = inspect.signature(func)
        required_pos = [
            p
            for p in sig.parameters.values()
            if p.kind
            in (
                inspect.Parameter.POSITIONAL_ONLY,
                inspect.Parameter.POSITIONAL_OR_KEYWORD,
            )
            and p.default is inspect._empty
        ]
        if len(required_pos) > 1:
            raise TypeError(
                f"{func.__name__} must take 0 or 1 positional parameter, got {len(required_pos)}"
            )
        takes_player_arg = len(required_pos) == 1
        # -----------------------------------------------------------

        @wraps(func)
        def wrapper():
            for player in ALL_PLAYERS:
                if TEAM == ALL or player.TEAM == TEAM:
                    if PLAYER == ALL or player.SLOT == PLAYER or player.HERO == PLAYER:
                        with with_event_player(player):
                            if all(conditions):
                                if takes_player_arg:
                                    func(player)
                                else:
                                    func()

        wrapper._func = func
        wrapper._team = TEAM
        wrapper._player = PLAYER
        wrapper._conditions = conditions
        each_player_functions.append(wrapper)
        return wrapper

    return real_decorator
