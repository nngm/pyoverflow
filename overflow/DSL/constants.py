from enum import StrEnum
from pathlib import Path
from typing import *
try:
    import yaml  # optional
except Exception:  # ModuleNotFoundError or others
    yaml = None

ROOT = Path(__file__).resolve().parents[2]
CONFIG_PATH = ROOT / "config.yaml"

_language = "en"
try:
    with open(CONFIG_PATH, encoding="utf-8") as f:
        if yaml is not None:
            config = yaml.safe_load(f)
            _language = config.get("language", "en")
except FileNotFoundError:
    pass


class Button(StrEnum):
    MELEE = "MELEE"
    PRIMARY_FIRE = "PRIMARY_FIRE"
    SECONDARY_FIRE = "SECONDARY_FIRE"
    ABILITY_1 = "ABILITY_1"
    ABILITY_2 = "ABILITY_2"
    JUMP = "JUMP"
    INTERACT = "INTERACT"
    ULTIMATE = "ULTIMATE"
    RELOAD = "RELOAD"
    CROUCH = "CROUCH"


Buttons = Button

MELEE: Final[Button] = Button.MELEE
PRIMARY_FIRE: Final[Button] = Button.PRIMARY_FIRE
SECONDARY_FIRE: Final[Button] = Button.SECONDARY_FIRE
ABILITY_1: Final[Button] = Button.ABILITY_1
ABILITY_2: Final[Button] = Button.ABILITY_2
JUMP: Final[Button] = Button.JUMP
INTERACT: Final[Button] = Button.INTERACT
ULTIMATE: Final[Button] = Button.ULTIMATE
RELOAD: Final[Button] = Button.RELOAD
CROUCH: Final[Button] = Button.CROUCH

class TeamId(StrEnum):
    ALL_TEAMS = "ALL"
    TEAM_1 = "TEAM 1"
    TEAM_2 = "TEAM 2"


Team = TeamId

ALL_TEAMS: Final[TeamId] = TeamId.ALL_TEAMS
TEAM_1: Final[TeamId] = TeamId.TEAM_1
TEAM_2: Final[TeamId] = TeamId.TEAM_2


class PlayerSlot(StrEnum):
    ALL = "ALL"
    SLOT_0 = "SLOT 0"
    SLOT_1 = "SLOT 1"
    SLOT_2 = "SLOT 2"
    SLOT_3 = "SLOT 3"
    SLOT_4 = "SLOT 4"
    SLOT_5 = "SLOT 5"
    SLOT_6 = "SLOT 6"
    SLOT_7 = "SLOT 7"
    SLOT_8 = "SLOT 8"
    SLOT_9 = "SLOT 9"
    SLOT_10 = "SLOT 10"
    SLOT_11 = "SLOT 11"
    TRACER = "TRACER"
    HELLO = "HELLO"


ALL: Final[PlayerSlot] = PlayerSlot.ALL
SLOT_0: Final[PlayerSlot] = PlayerSlot.SLOT_0
SLOT_1: Final[PlayerSlot] = PlayerSlot.SLOT_1
SLOT_2: Final[PlayerSlot] = PlayerSlot.SLOT_2
SLOT_3: Final[PlayerSlot] = PlayerSlot.SLOT_3
SLOT_4: Final[PlayerSlot] = PlayerSlot.SLOT_4
SLOT_5: Final[PlayerSlot] = PlayerSlot.SLOT_5
SLOT_6: Final[PlayerSlot] = PlayerSlot.SLOT_6
SLOT_7: Final[PlayerSlot] = PlayerSlot.SLOT_7
SLOT_8: Final[PlayerSlot] = PlayerSlot.SLOT_8
SLOT_9: Final[PlayerSlot] = PlayerSlot.SLOT_9
SLOT_10: Final[PlayerSlot] = PlayerSlot.SLOT_10
SLOT_11: Final[PlayerSlot] = PlayerSlot.SLOT_11
TRACER: Final[PlayerSlot] = PlayerSlot.TRACER
HELLO: Final[PlayerSlot] = PlayerSlot.HELLO

if _language in ["en"]:
    CONDITIONS_NAME = "conditions"
    ACTIONS_NAME = "actions"
elif _language in ["ko"]:
    CONDITIONS_NAME = "condition"
    ACTIONS_NAME = "action"


class Reevaluation(StrEnum):
    VISIBLE_TO_AND_STRING = "Visible to and String"
    STRING = "String"
    VISIBLE_TO_SORT_ORDER_STRING = "Visible to, Sort Order, String"
    SORT_ORDER_AND_STRING = "Sort Order and String"
    VISIBLE_TO_AND_SORT_ORDER = "Visible to and Sort Order"
    VISIBLE_TO = "Visible to"
    SORT_ORDER = "Sort Order"
    NONE = "None"
    VISIBLE_TO_SORT_ORDER_STRING_AND_COLOR = "Visible to, Sort Order, String and Color"
    SORT_ORDER_STRING_AND_COLOR = "Sort Order, String and Color"
    VISIBLE_TO_SORT_ORDER_AND_COLOR = "Visible to, Sort Order and Color"
    VISIBLE_TO_AND_COLOR = "Visible to and Color"
    SORT_ORDER_AND_COLOR = "Sort Order and Color"
    COLOR = "Color"


VISIBLE_TO_AND_STRING: Final[Reevaluation] = Reevaluation.VISIBLE_TO_AND_STRING
STRING: Final[Reevaluation] = Reevaluation.STRING
VISIBLE_TO_SORT_ORDER_STRING: Final[Reevaluation] = Reevaluation.VISIBLE_TO_SORT_ORDER_STRING
SORT_ORDER_AND_STRING: Final[Reevaluation] = Reevaluation.SORT_ORDER_AND_STRING
VISIBLE_TO_AND_SORT_ORDER: Final[Reevaluation] = Reevaluation.VISIBLE_TO_AND_SORT_ORDER
VISIBLE_TO: Final[Reevaluation] = Reevaluation.VISIBLE_TO
SORT_ORDER: Final[Reevaluation] = Reevaluation.SORT_ORDER
NONE: Final[Reevaluation] = Reevaluation.NONE
VISIBLE_TO_SORT_ORDER_STRING_AND_COLOR: Final[Reevaluation] = Reevaluation.VISIBLE_TO_SORTER_STRING_AND_COLOR
SORT_ORDER_STRING_AND_COLOR: Final[Reevaluation] = Reevaluation.SORT_ORDER_STRING_AND_COLOR
VISIBLE_TO_SORT_ORDER_AND_COLOR: Final[Reevaluation] = Reevaluation.VISIBLE_TO_SORT_ORDER_AND_COLOR
VISIBLE_TO_AND_COLOR: Final[Reevaluation] = Reevaluation.VISIBLE_TO_AND_COLOR
SORT_ORDER_AND_COLOR: Final[Reevaluation] = Reevaluation.SORT_ORDER_AND_COLOR
COLOR: Final[Reevaluation] = Reevaluation.COLOR


class Non_team_spectators(StrEnum):
    DEFAULT_VISIBILITY = "Default Visibility"
    VISIBLE_ALWAYS = "Visible Always"
    VISIBLE_NEVER = "Visible Never"


DEFAULT_VISIBILITY: Final[Non_team_spectators] = Non_team_spectators.DEFAULT_VISIBILITY
VISIBLE_ALWAYS: Final[Non_team_spectators] = Non_team_spectators.VISIBLE_ALWAYS
VISIBLE_NEVER: Final[Non_team_spectators] = Non_team_spectators.VISIBLE


class Status(StrEnum):
    STUNNED = "Stunned"
    INVINCIBLE = "Invincible"
    FROZEN = "Frozen"


STUNNED: Final[Status] = Status.STUNNED
INVINCIBLE: Final[Status] = Status.INVINCIBLE
FROZEN: Final[Status] = Status.FROZEN


class EffectName(StrEnum):
    BAD_BEAM = "Bad Beam"
    SPHERE = "Sphere"
    RING = "Ring"
    GOOD_EXPLOSION = "Good Explosion"
    RING_EXPLOSION = "Ring Explosion"
    RING_EXPLOSION_SOUND = "Ring Explosion Sound"
    EXPLOSION_SOUND = "Explosion Sound"
    GOOD_PICKUP_EFFECT = "Good Pickup Effect"
    RING_EXPLOSION_SLASH = "Ring/Explosion"
    BAD_EXPLOSION = "Bad Explosion"


BAD_BEAM: Final[EffectName] = EffectName.BAD_BEAM
SPHERE: Final[EffectName] = EffectName.SPHERE
RING: Final[EffectName] = EffectName.RING
GOOD_EXPLOSION: Final[EffectName] = EffectName.GOOD_EXPLOSION
RING_EXPLOSION: Final[EffectName] = EffectName.RING_EXPLOSION
RING_EXPLOSION_SOUND: Final[EffectName] = EffectName.RING_EXPLOSION_SOUND
EXPLOSION_SOUND: Final[EffectName] = EffectName.EXPLOSION_SOUND
GOOD_PICKUP_EFFECT: Final[EffectName] = EffectName.GOOD_PICKUP_EFFECT
RING_EXPLOSION_SLASH: Final[EffectName] = EffectName.RING_EXPLOSION_SLASH
BAD_EXPLOSION: Final[EffectName] = EffectName.BAD_EXPLOSION


class Color(StrEnum):
    RED = "Red"
    GREEN = "Green"
    BLUE = "Blue"
    WHITE = "White"
    SKY_BLUE = "Sky Blue"
    PURPLE = "Purple"
    BLACK = "Black"


RED: Final[Color] = Color.RED
GREEN: Final[Color] = Color.GREEN
BLUE: Final[Color] = Color.BLUE
WHITE: Final[Color] = Color.WHITE
SKY_BLUE: Final[Color] = Color.SKY_BLUE
PURPLE: Final[Color] = Color.PURPLE
BLACK: Final[Color] = Color.BLACK


class HudTextAlign(StrEnum):
    LEFT = "Left"
    TOP = "Top"
    RIGHT = "Right"


LEFT: Final[HudTextAlign] = HudTextAlign.LEFT
TOP: Final[HudTextAlign] = HudTextAlign.TOP
RIGHT: Final[HudTextAlign] = HudTextAlign.RIGHT


__all__ = [
    "ROOT",
    "CONFIG_PATH",
    "Button",
    "Buttons",
    *Button.__members__.keys(),
    "TeamId",
    "Team",
    *TeamId.__members__.keys(),
    "PlayerSlot",
    "Player",
    *PlayerSlot.__members__.keys(),
    "CONDITIONS_NAME",
    "ACTIONS_NAME",
    "Status",
    *Status.__members__.keys(),
    "EffectName",
    *EffectName.__members__.keys(),
    "Color",
    *Color.__members__.keys(),
    "HudTextAlign",
    *HudTextAlign.__members__.keys(),
]
