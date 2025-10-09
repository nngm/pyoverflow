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


def _resolve(x: ValueLike) -> Any:
    return x() if callable(x) else x


class Expr:
    """Lazy value wrapper that supports operator overloading to yield Conditions."""

    def __init__(self, v: ValueLike):
        self._v = v

    def __call__(self):
        return _resolve(self._v)

    def __eq__(self, other):
        from src.DSL.rule import compare

        return compare(self, "==", other)

    def __ne__(self, other):
        from src.DSL.rule import compare

        return compare(self, "!=", other)

    def __lt__(self, other):
        from src.DSL.rule import compare

        return compare(self, "<", other)

    def __le__(self, other):
        from src.DSL.rule import compare

        return compare(self, "<=", other)

    def __gt__(self, other):
        from src.DSL.rule import compare

        return compare(self, ">", other)

    def __ge__(self, other):
        from src.DSL.rule import compare

        return compare(self, ">=", other)


def wrap(v: ValueLike) -> Expr:
    return v if isinstance(v, Expr) else Expr(v)


class player_parent(metaclass=WorkshopVarMeta):
    def __init__(self):
        object.__setattr__(self, "_vars", {})
        self.TEAM: Team = None
        self.SLOT: Player = None
        self.HERO: Player = None
        self.is_melee: bool = False
        self.Punch: bool = True
        self._status = None

    def __getattr__(self, name: str):
        d = object.__getattribute__(self, "__dict__")
        if "_vars" in d:
            return self._vars.get(name)
        raise AttributeError(name)

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

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return vector(self.x * other, self.y * other, self.z * other)
        if isinstance(other, vector):
            return vector(self.x * other.x, self.y * other.y, self.z * other.z)
        raise TypeError

    __rmul__ = __mul__

    def __repr__(self):
        return f"vector({self.x}, {self.y}, {self.z})"
