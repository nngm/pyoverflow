import yaml
from typing import *

_language = yaml.safe_load(open("config.yaml"))["language"]

MELEE = "MELEE"
Buttons = Literal[
    "MELEE",
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
