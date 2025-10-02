from src.DSL.ctx_init import _ctx
from src.DSL.ctx_cur_arr_elem import CURRENT_ARRAY_ELEMENT
from src.DSL.owglobals import *
from src.DSL.owtyping import *
from DSL.rule import *
import math
import random


def _resolve(x: ValueLike) -> Any:
    return x() if callable(x) else x


def _as_bool(x: Union[bool, Condition, ValueLike]) -> bool:
    return bool(_resolve(x))


def count_of(a: Iterable[Any]):
    return Expr(lambda: len(list(a)))


def button(BUTTON: Buttons):
    return BUTTON


def all_players(team: Team):
    if team == ALL_TEAMS:
        return ALL_PLAYERS
    return filtered_array(ALL_PLAYERS, compare(CURRENT_ARRAY_ELEMENT.TEAM, "==", team))


def all_living_players(team: Team):
    # No death simulation; treat same as all_players for now.
    return all_players(team)


def team(TEAM: Team):
    return TEAM


def custom_string(STRING: str, ZERO: Any = "", ONE: Any = "", TWO: Any = "") -> string:
    return STRING.format(ZERO, ONE, TWO)


def array(*args):
    return list(args)


def filtered_array(
    ARRAY: Iterable[Any],
    CONDITION: Union[bool, Condition, ValueLike],
) -> List[Any]:
    out: List[Any] = []
    prev = getattr(_ctx, "cur_arr_elem", None)
    try:
        for elem in ARRAY:
            _ctx.cur_arr_elem = elem
            if _as_bool(CONDITION):
                out.append(elem)
    finally:
        _ctx.cur_arr_elem = prev
    return out


def workshop_setting_integer(
    category: string, name: string, default: int, min: int, max: int, sort_order: int
) -> int:
    return default


def workshop_setting_toggle(
    category: string, name: string, default: bool, sort_order: int
) -> bool:
    return default


def workshop_setting_combo(
    category: string, name: string, default: int, options: List[Any], sort_order: int
) -> Any:
    return options[default]


def first_of(ARRAY: Iterable[Any]) -> Any:
    for elem in ARRAY:
        return elem
    return 0


# Lightweight math/vector helpers used by decompiled rules. These are placeholders.
def eye_position(p: Any) -> Any:
    return getattr(p, "position", vector(0, 0, 0))


def facing_direction_of(p: Any) -> Any:
    return getattr(p, "facing", vector(1, 0, 0))


def direction_towards(a: Any, b: Any) -> Any:
    if isinstance(a, vector) and isinstance(b, vector):
        return vector(b.x - a.x, b.y - a.y, b.z - a.z)
    return vector(0, 0, 0)


def angle_between_vectors(a: Any, b: Any) -> float:
    def dot(u: vector, v: vector) -> float:
        return u.x * v.x + u.y * v.y + u.z * v.z

    def mag(u: vector) -> float:
        return math.sqrt(u.x * u.x + u.y * u.y + u.z * u.z) or 1.0

    if isinstance(a, vector) and isinstance(b, vector):
        cosang = max(-1.0, min(1.0, dot(a, b) / (mag(a) * mag(b))))
        return math.degrees(math.acos(cosang))
    return 0.0


def sorted_array(arr: Iterable[Any], key: Any) -> list:
    try:
        # key can be a callable; resolve if our DSL Expr
        k = key if callable(key) else (lambda x: key)
        return sorted(list(arr), key=k)
    except Exception:
        return list(arr)


def is_game_in_progress() -> Expr:
    return Expr(lambda: True)


def number_of_players(team: Team) -> int:
    return len(list(all_players(team)))


def is_alive(p: Any) -> Expr:
    return Expr(lambda: not getattr(p, "is_dead", False))


def is_dead(p: Any) -> Expr:
    return Expr(lambda: bool(getattr(p, "is_dead", False)))


def entity_exists(e: Any) -> Expr:
    return Expr(lambda: e is not None)


def has_spawned(p: Any) -> Expr:
    # Defer to runtime; treat as spawned by default in this stub.
    return Expr(lambda: True)


def is_dummy_bot(p: Any) -> Expr:
    return Expr(lambda: bool(getattr(p, "is_bot", False)))


def is_on_wall(p: Any) -> bool:
    return False


def distance_between(a: Any, b: Any) -> float:
    if isinstance(a, vector) and isinstance(b, vector):
        dx, dy, dz = a.x - b.x, a.y - b.y, a.z - b.z
        return math.sqrt(dx * dx + dy * dy + dz * dz)
    return 0.0


def x_component_of(v: Any) -> float:
    return getattr(v, "x", 0.0)


def y_component_of(v: Any) -> float:
    return getattr(v, "y", 0.0)


def z_component_of(v: Any) -> float:
    return getattr(v, "z", 0.0)


def magnitude_of(v: Any) -> float:
    if isinstance(v, vector):
        return math.sqrt(v.x * v.x + v.y * v.y + v.z * v.z)
    return float(v) if isinstance(v, (int, float)) else 0.0


def dot_product(a: Any, b: Any) -> float:
    if isinstance(a, vector) and isinstance(b, vector):
        return a.x * b.x + a.y * b.y + a.z * b.z
    return 0.0


def min_(a: Any, b: Any) -> Any:
    return a if a <= b else b


def max_(a: Any, b: Any) -> Any:
    return a if a >= b else b


def random_integer(a: int, b: int) -> int:
    return random.randint(a, b)


def random_real(a: float, b: float) -> float:
    return random.uniform(a, b)


def world_vector_of(v: vector, p: Any, rotation: Any) -> vector:
    return v


def round_to_integer(v: float, mode: str) -> int:
    if mode.lower() == "up":
        return math.ceil(v)
    if mode.lower() == "down":
        return math.floor(v)
    return round(v)


def empty_array() -> list:
    return []


def append_to_array(arr: Iterable[Any], val: Any) -> list:
    out = list(arr)
    out.append(val)
    return out


def random_value_in_array(arr: Iterable[Any]) -> Any:
    arr = list(arr)
    return arr[0] if arr else None


def host_player() -> Any:
    return first_of(all_players(ALL_TEAMS))


def last_of(arr: Iterable[Any]) -> Any:
    arr = list(arr)
    return arr[-1] if arr else None


def score_of(p: Any) -> int:
    return getattr(p, "score", 0)


def color(name: str) -> str:
    return name


def icon_string(s: str) -> str:
    return s


def input_binding_string(button: Buttons) -> str:
    return str(button)


def string(fmt: str, *args) -> str:
    return fmt.format(*args)


def update_every_frame(value: Any) -> Any:
    return value


def ray_cast_hit_position(start: vector, end: vector, a=None, b=None, c=None) -> vector:
    return end


def ray_cast_hit_normal(start: vector, end: vector, a=None, b=None, c=None) -> vector:
    return vector(0, 1, 0)


def players_in_view_angle(player: Any, team: Team, angle: float) -> bool:
    return True


def player_closest_to_reticle(player: Any, team: Team) -> Any:
    return first_of(all_players(team))
