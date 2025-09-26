import operator
from src.DSL.constants import *

string = str
number = float
ValueLike = Union[Any, Callable[[], Any]]

OPS = {
    "==": operator.eq,
    "!=": operator.ne,
    "<": operator.lt,
    "<=": operator.le,
    ">": operator.gt,
    ">=": operator.ge,
}


class player_parent:
    TEAM: Team = None
    SLOT: Player = None
    HERO: Player = None
    is_melee: bool = False
    Punch: bool = True

    def __init__(self):
        object.__setattr__(self, "_vars", {})

    def __getattr__(self, name: str):
        return self._vars.get(name)

    def __setattr__(self, name, value):
        if name.startswith("_") or hasattr(type(self), name):
            object.__setattr__(self, name, value)
        else:
            self._vars[name] = value


class vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        if isinstance(other, vector):
            return vector(self.x + other.x, self.y + other.y, self.z + other.z)
        raise TypeError

    def __sub__(self, other):
        if isinstance(other, vector):
            return vector(self.x - other.x, self.y - other.y, self.z - other.z)
        raise TypeError
