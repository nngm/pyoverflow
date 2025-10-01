import operator
from src.DSL.constants import *
from src.DSL.auto_array import *
from typing import Final

null: Final = None
Null: Final = None
NULL: Final = None
string: TypeAlias = str
number: TypeAlias = float
ValueLike: TypeAlias = Union[Any, Callable[[], Any]]

OPS: Final = {
    "==": operator.eq,
    "!=": operator.ne,
    "<": operator.lt,
    "<=": operator.le,
    ">": operator.gt,
    ">=": operator.ge,
}


class player_parent(mettaclass=WorkshopVarMeta):
    def __init__(self):
        self.TEAM: Team = None
        self.SLOT: Player = None
        self.HERO: Player = None
        self.is_melee: bool = False
        self.Punch: bool = True
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
