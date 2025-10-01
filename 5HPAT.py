from src.overwatch import *

class player(player_parent):
    hasMoved = Null
    angle = Null
    BouncePadCooldown = Null
    BotCooldown = Null
    ToggleHUD = Null
    BotKind = Null
    MoveSpeed = Null
    BotTargetpos = Null
    ClosePlayer = Null
    Punch = Null
    aimSpeed = Null
    BallScore = Null
    MinigameScore = Null
    MinigameDeaths = Null

ALL_PLAYERS.adopt([player() for _ in range(12)])
ALL_PLAYERS: list[player]
event_player = cast(player, event_player)

class Global:
	SlotOfTargetedPlayer = Null
	SlotOfPreviousTargetedPlayer = Null
	BallSpeed = Null
	BallPosition = Null
	BallSpawnCountdown = Null
	BallIsOut = Null
	RoundInProgress = Null
	SubPlayer = Null
	OnlyPlayer = Null
	MatchPlayer = Null
	IsInFinalDuel = Null
	BouncePadDistance = Null
	BouncePad1 = Null
	BouncePad2 = Null
	BouncePad3 = Null
	BouncePad4 = Null
	deathSphere = Null
	deathSphereRad = Null
	IsEnoughPlayersToStart = Null
	CenterOffLimitsSize = Null
	CircleCenter = Null
	HighestScore = Null
	Overtime = Null
	deathSpherePos = Null
	deathBeam = Null
	BallDirection = Null
	BallCollisionSurfaceNormal = Null
	PrevBallPos = Null
	PrevBallPos2 = Null
	number_p = Null
	TargetBot = Null
	Distance = Null
	BotName = Null
	SetColor = Null
	True_or_False = Null


@ongoing_global
def workshop_setting():
    """Made by MAZAWATH"""
    Global.number_p[0] = workshop_setting_integer("볼", "기본 속도", 40, 20, 100, 0)
    Global.number_p[1] = workshop_setting_integer("볼", "최대 속도 (기본 속도 이상)", 60, 20, 300, 1)
    Global.number_p[1] = max(first_of(Global.number_p), Global.number_p[1])
    Global.number_p[4] = workshop_setting_integer("게임", "경기 시간", 1200, 30, 1200, 0)
    Global.True_or_False[3] = workshop_setting_toggle("게임", "자동 경기 재시작", True, 1)
    Global.True_or_False[9] = workshop_setting_toggle("게임", "워크샵 인스펙터 로그 (허용 시 서버 부하량 증가)", False, 2)
    Global.True_or_False[7] = workshop_setting_combo("게임", "미니게임", 0, array("비활성화",
        "겐지 주먹전"), 3)
    Global.True_or_False[0] = workshop_setting_combo("게임", "겐지 주먹전에서 아래로 떨어지면", 0, array(
        "즉사시켜 게임 관전 (겐지 주먹전 재입장 가능)", "다시 겐지 주먹전 진입"), 4)
    Global.number_p[6] = workshop_setting_integer("봇", "최대 수", 1, 1, 11, 0)
    Global.True_or_False[2] = workshop_setting_toggle("봇", "무빙 (비활성화 시 생성 버튼을 누른 자리에서 봇이 생성됩니다)", True,
        1)
    Global.True_or_False[5] = workshop_setting_toggle("봇", "에임 (비활성화 시 생성 버튼을 누른 시점의 에임으로 봇의 에임이 고정됩니다)",
        True, 2)
    Global.True_or_False[6] = workshop_setting_toggle("봇", "이름에 생성 번호 매기기", False, 3)

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
