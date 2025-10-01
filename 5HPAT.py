from src.overwatch import *

class player(player_parent):
    hasMoved = None
    angle = None
    BouncePadCooldown = None
    BotCooldown = None
    ToggleHUD = None
    BotKind = None
    MoveSpeed = None
    BotTargetpos = None
    ClosePlayer = None
    Punch = None
    aimSpeed = None
    BallScore = None
    MinigameScore = None
    MinigameDeaths = None

ALL_PLAYERS.adopt([player() for _ in range(12)])
ALL_PLAYERS: list[player]
event_player = cast(player, event_player)

class Global:
	SlotOfTargetedPlayer = None
	SlotOfPreviousTargetedPlayer = None
	BallSpeed = None
	BallPosition = None
	BallSpawnCountdown = None
	BallIsOut = None
	RoundInProgress = None
	SubPlayer = None
	OnlyPlayer = None
	MatchPlayer = None
	IsInFinalDuel = None
	BouncePadDistance = None
	BouncePad1 = None
	BouncePad2 = None
	BouncePad3 = None
	BouncePad4 = None
	deathSphere = None
	deathSphereRad = None
	IsEnoughPlayersToStart = None
	CenterOffLimitsSize = None
	CircleCenter = None
	HighestScore = None
	Overtime = None
	deathSpherePos = None
	deathBeam = None
	BallDirection = None
	BallCollisionSurfaceNormal = None
	PrevBallPos = None
	PrevBallPos2 = None
	number_p = None
	TargetBot = None
	Distance = None
	BotName = None
	SetColor = None
	True_or_False = None


@ongoing_global
def init_global_variables():
    Global.foo = custom_string("bar")

@ongoing_each_player(ALL_TEAMS, ALL)
@rules(
    is_button_held(event_player, button(MELEE)),
    compare(
        count_of(
            filtered_array(
                all_players(ALL_TEAMS), 
                CURRENT_ARRAY_ELEMENT.hasMoved
            )
        ), 
        ">", 
        1
    )
)
def let_player_minigame():
    event_player.Punch = True

if __name__ == "__main__":
    print(bool(compare(1,">",0)))
