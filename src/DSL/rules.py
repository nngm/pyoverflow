from abc import ABC, abstractmethod
from src.DSL.constants import *
from src.DSL.owtyping import *


def rules(*conds):
    def deco(func):
        if hasattr(func, "_rules"):
            func._rules.extend(conds)
        else:
            func._rules = list(conds)
        return func

    return deco


def _resolve(x: ValueLike) -> Any:
    return x() if callable(x) else x


class Condition(ABC):
    @abstractmethod
    def __call__(self):
        pass

    def __bool__(self) -> bool:
        return self()


class compare(Condition):
    def __init__(
        self,
        lhs: ValueLike,
        op: Literal["==", "!=", "<", "<=", ">", ">="],
        rhs: ValueLike,
    ):
        self.lhs = lhs
        self.op = op
        self.rhs = rhs

    def __call__(self) -> bool:
        return OPS[self.op](_resolve(self.lhs), _resolve(self.rhs))


class is_button_held(Condition):
    event_player = None
    button = None

    def __init__(self, event_player: player_parent, button: buttons):
        self.event_player = event_player
        self.button = button

    def __call__(self):
        if self.button == MELEE:
            return self.event_player.is_melee
        raise NotImplementedError
