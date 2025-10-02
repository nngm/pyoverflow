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

Buttons = Literal[
    "MELEE",
    "PRIMARY_FIRE",
    "SECONDARY_FIRE",
    "ABILITY_1",
    "ABILITY_2",
    "JUMP",
    "INTERACT",
    "ULTIMATE",
    "RELOAD",
    "CROUCH",
]

ALL_TEAMS = "ALL"
TEAM_1 = "TEAM 1"
TEAM_2 = "TEAM 2"

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

Team = Literal["ALL", "TEAM 1", "TEAM 2"]
Player = Literal[
    "ALL",
    "SLOT 0",
    "SLOT 1",
    "SLOT 2",
    "SLOT 3",
    "SLOT 4",
    "SLOT 5",
    "SLOT 6",
    "SLOT 7",
    "SLOT 8",
    "SLOT 9",
    "SLOT 10",
    "SLOT 11",
    "TRACER",
]

if _language in ["en"]:
    CONDITIONS_NAME = "conditions"
    ACTIONS_NAME = "actions"
elif _language in ["ko"]:
    CONDITIONS_NAME = "condition"
    ACTIONS_NAME = "action"
