from src.DSL.ctx_init import _ctx
from src.DSL.ctx_cur_arr_elem import CURRENT_ARRAY_ELEMENT
from src.DSL.owglobals import *
from src.DSL.owtyping import *
from src.DSL.rules import *


def count_of(a: Iterable[Any]):
    return len(a)


def button(BUTTON: Buttons):
    return BUTTON


def all_players(team: Team):
    if team == ALL_TEAMS:
        return ALL_PLAYERS
    return filtered_array(ALL_PLAYERS, compare(CURRENT_ARRAY_ELEMENT.TEAM, "==", team))


def team(TEAM: Team):
    return TEAM


def custom_string(STRING: str, ZERO: Any = "", ONE: Any = "", TWO: Any = "") -> string:
    return STRING.format(ZERO, ONE, TWO)


def array(*args):
    return list(args)


def filtered_array(ARRAY: Iterable[Any], CONDITION: Union[bool, Condition]) -> List[Any]:
    out = []
    prev = getattr(_ctx, "cur_arr_elem", None)
    try:
        for elem in ARRAY:
            _ctx.cur_arr_elem = elem
            if CONDITION:
                out.append(elem)
    finally:
        _ctx.cur_arr_elem = prev
    return out

def workshop_setting_integer(category: string, name: string, default: int, min: int, max: int, sort_order: int) -> int:
    return default

def workshop_setting_toggle(category: string, name: string, default: bool, sort_order: int) -> bool:
    return default

def workshop_setting_combo(category: string, name: string, default: int, options: List[Any], sort_order: int) -> Any:
    return options[default]
