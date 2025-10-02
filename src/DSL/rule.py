from abc import ABC, abstractmethod
from src.DSL.constants import *
from src.DSL.owtyping import *


class Condition(ABC):
    @abstractmethod
    def __call__(self):
        pass

    def __bool__(self) -> bool:
        return self()


def rules(*conds: List[Condition]):
    def deco(func):
        if hasattr(func, "_rules"):
            func._rules.extend(conds)
        else:
            func._rules = list(conds)
        return func

    return deco


def _resolve(x: ValueLike) -> Any:
    return x() if callable(x) else x


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

    def __repr__(self):
        return f"<compare lhs={self.lhs!r} op='{self.op}' rhs={self.rhs!r}>"

    def __str__(self):
        return f"{self.lhs} {self.op} {self.rhs}"


class is_button_held(Condition):
    def __init__(self, event_player: player_parent, BUTTON: Buttons):
        self.event_player = event_player
        self.BUTTON = BUTTON

    def __call__(self):
        mapping = {
            MELEE: "is_melee",
            PRIMARY_FIRE: "is_primary_fire",
            SECONDARY_FIRE: "is_secondary_fire",
            ABILITY_1: "is_ability1",
            ABILITY_2: "is_ability2",
            JUMP: "is_jump",
            INTERACT: "is_interact",
            ULTIMATE: "is_ultimate",
            RELOAD: "is_reload",
            CROUCH: "is_crouch",
        }
        attr = mapping.get(self.BUTTON)
        return bool(getattr(self.event_player, attr, False))


class is_using_ability(Condition):
    def __init__(self, event_player: player_parent, ability_index: int):
        self.event_player = event_player
        self.ability_index = ability_index

    def __call__(self) -> bool:
        # Placeholder: rely on attributes that tests may set, e.g., is_ability1
        attr = f"is_ability{self.ability_index}"
        return bool(getattr(self.event_player, attr, False))
