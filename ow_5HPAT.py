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

class Global(metaclass=WorkshopVarMeta):
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


def RP():
    """Respawn Players (subroutine)"""
    pass


def BallDR():
    """Ball Despawn/Respawn (subroutine)"""
    _ball_delete_requested()


def CoolDeathEffects():
    """Kill Targeted Player"""
    # Subroutine body roughly translated from Workshop actions.
    set_status(Global.SlotOfTargetedPlayer, Global.SlotOfPreviousTargetedPlayer, "Stunned", 1)
    create_beam_effect(all_players(ALL_TEAMS), "Bad Beam", Global.SlotOfPreviousTargetedPlayer, Global.SlotOfTargetedPlayer, "Red")
    Global.deathBeam = last_created_entity()
    Global.deathSpherePos = eye_position(Global.SlotOfTargetedPlayer)
    Global.deathSphereRad = 30
    chase_global_variable_over_time("deathSphereRad", 0, 0.250)
    play_effect(all_players(ALL_TEAMS), "Ring Explosion Sound", "White", Global.deathSpherePos, 40)
    create_effect(all_players(ALL_TEAMS), "Sphere", "Red", Global.deathSpherePos, Global.deathSphereRad)
    Global.deathSphere = last_created_entity()
    play_effect(all_players(ALL_TEAMS), "Good Explosion", "White", Global.deathSpherePos, 5)
    wait(0.250)
    destroy_effect(Global.deathSphere)
    play_effect(all_players(ALL_TEAMS), "Ring Explosion", "Red", Global.deathSpherePos, 45)
    play_effect(all_players(ALL_TEAMS), "Explosion Sound", "White", Global.deathSpherePos, 40)
    destroy_effect(Global.deathBeam)
    Global.SlotOfTargetedPlayer.BouncePadCooldown = 0
    # If one player left, just stagger; else kill and mark moved
    if count_of(all_players(ALL_TEAMS)) == 1:
        set_status(Global.SlotOfTargetedPlayer, None, "Stunned", 0.2)
    else:
        kill(Global.SlotOfTargetedPlayer, Global.SlotOfPreviousTargetedPlayer)
        Global.SlotOfTargetedPlayer.hasMoved = False
    BallDR()


@ongoing_each_player(ALL_TEAMS, ALL)
def init_player_variables(event_player: player):
    """Init Player Variables"""
    set_status(event_player, None, "Invincible", 9999)
    disable_built_in_game_mode_respawning(event_player)
    enable_death_spectate_all_players(event_player)
    enable_death_spectate_target_hud(event_player)
    event_player.BouncePadCooldown = 5
    set_damage_dealt(event_player, 0.030)


@ongoing_global
def init_global_variables():
    """Init Global Variables"""
    Global.SlotOfTargetedPlayer = -1
    Global.SlotOfPreviousTargetedPlayer = -1
    disable_built_in_game_mode_scoring()
    disable_built_in_game_mode_completion()
    disable_built_in_game_mode_music()
    disable_built_in_game_mode_announcer()
    Global.BallSpeed = first_of(Global.number_p)
    Global.CenterOffLimitsSize = 3.500
    Global.IsInFinalDuel = False
    Global.BallPosition = vector(0, -1, 0)
    Global.CircleCenter = vector(0, 1.199, 0)
    Global.BallSpawnCountdown = 5
    if not Global.True_or_False[9]:
        disable_inspector_recording()
    Global.BotName = "신라면봇"
    Global.BouncePadDistance = 12
    Global.BouncePad1 = Global.CircleCenter.value + vector(float(Global.BouncePadDistance), 0, 0)
    Global.BouncePad2 = Global.CircleCenter.value - vector(float(Global.BouncePadDistance), 0, 0)
    Global.BouncePad3 = Global.CircleCenter.value + vector(0, 0, float(Global.BouncePadDistance))
    Global.BouncePad4 = Global.CircleCenter.value - vector(0, 0, float(Global.BouncePadDistance))


@ongoing_global
def create_world_and_hud():
    """Create ( Bounce Pads & Global HUD & Ball Countdown HUD & Sphere & Ball & Effects )"""
    # Jump pads
    create_effect(filtered_array(all_players(ALL_TEAMS), compare(CURRENT_ARRAY_ELEMENT.BouncePadCooldown, "==", 0)), "Ring", "Green", Global.BouncePad1, 2)
    create_effect(filtered_array(all_players(ALL_TEAMS), compare(CURRENT_ARRAY_ELEMENT.BouncePadCooldown, "==", 0)), "Ring", "Green", Global.BouncePad2, 2)
    create_effect(filtered_array(all_players(ALL_TEAMS), compare(CURRENT_ARRAY_ELEMENT.BouncePadCooldown, "==", 0)), "Ring", "Green", Global.BouncePad3, 2)
    create_effect(filtered_array(all_players(ALL_TEAMS), compare(CURRENT_ARRAY_ELEMENT.BouncePadCooldown, "==", 0)), "Ring", "Green", Global.BouncePad4, 2)
    create_effect(filtered_array(all_players(ALL_TEAMS), compare(CURRENT_ARRAY_ELEMENT.BouncePadCooldown, ">", 0)), "Ring", "Red", Global.BouncePad1, 2)
    create_effect(filtered_array(all_players(ALL_TEAMS), compare(CURRENT_ARRAY_ELEMENT.BouncePadCooldown, ">", 0)), "Ring", "Red", Global.BouncePad2, 2)
    create_effect(filtered_array(all_players(ALL_TEAMS), compare(CURRENT_ARRAY_ELEMENT.BouncePadCooldown, ">", 0)), "Ring", "Red", Global.BouncePad3, 2)
    create_effect(filtered_array(all_players(ALL_TEAMS), compare(CURRENT_ARRAY_ELEMENT.BouncePadCooldown, ">", 0)), "Ring", "Red", Global.BouncePad4, 2)
    # HUDs
    create_hud_text(all_players(ALL_TEAMS), None, None, f"공이 시속 {Global.BallSpeed}KM로 날아가고 있습니다!", "Left")
    # Center sphere and countdown
    create_effect(all_players(ALL_TEAMS), "Sphere", "Sky Blue", Global.CircleCenter.value, Global.CenterOffLimitsSize)


@ongoing_each_player(ALL_TEAMS, ALL)
@rules(is_button_held(event_player, PRIMARY_FIRE))
def press_button_1():
    """Press Button 1"""
    press_button(event_player(), ABILITY_1)


@ongoing_each_player(ALL_TEAMS, ALL)
@rules(is_button_held(event_player, SECONDARY_FIRE))
def press_button_2():
    """Press Button 2"""
    press_button(event_player(), ABILITY_2)


@ongoing_global
@rules(
    wrap(lambda: number_of_players(ALL_TEAMS)) == 1,
    is_game_in_progress() == True,
)
def check_number_of_players_eq_1():
    """Check for Number of Players == 1"""
    resurrect(all_players(ALL_TEAMS))
    Global.IsInFinalDuel = False
    Global.IsEnoughPlayersToStart = False
    stop_chasing_global_variable("BallSpawnCountdown")
    if Global.RoundInProgress:
        BallDR()
    Global.RoundInProgress = False
    pause_match_time()
    set_player_score(all_players(ALL_TEAMS), 0)
    small_message(all_players(ALL_TEAMS), "재장전으로 연습 가능")


@ongoing_global
@rules(
    wrap(lambda: Global.IsEnoughPlayersToStart) == False,
    wrap(lambda: number_of_players(ALL_TEAMS)) > 1,
)
def wait_for_more_players():
    """Wait for More Players"""
    wait(3)
    if number_of_players(ALL_TEAMS) < 2:
        return
    RP()
    unpause_match_time()
    Global.IsEnoughPlayersToStart = True
    Global.SlotOfTargetedPlayer = -1
    Global.SlotOfPreviousTargetedPlayer = -1


@ongoing_each_player(ALL_TEAMS, ALL)
@rules(has_spawned(event_player) == True)
def player_joins_game():
    """Player Joins Game"""
    if Global.True_or_False[2] and is_dummy_bot(event_player()):
        teleport(event_player(), Global.CircleCenter.value + vector(random_integer(-10, 10), 8, random_integer(-10, 10)))
    if Global.RoundInProgress and is_game_in_progress():
        kill(event_player(), None)
    else:
        event_player.hasMoved = True
    start_camera(event_player(), ray_cast_hit_position(eye_position(event_player()), eye_position(event_player()) + world_vector_of(vector(0, 0, 0), event_player(), "Rotation") + facing_direction_of(event_player()) * -3.780, None, event_player(), False), event_player() + facing_direction_of(event_player()) * 1000, 65)
    if number_of_players(ALL_TEAMS) <= 2:
        BallDR()
        for p in ALL_PLAYERS:
            p.BouncePadCooldown = 5
        stop_chasing_player_variable(all_players(ALL_TEAMS), "BouncePadCooldown")
    # HUD help text (simplified)
    if not event_player.ToggleHUD:
        create_hud_text([event_player()], None, None, "매뉴얼 끄기: …", "Left")


@ongoing_each_player(ALL_TEAMS, ALL)
@rules(
    is_using_ability(event_player, 2),
    wrap(lambda: getattr(event_player(), "is_ultimate", False)) == False,
)
def shorten_deflect_length():
    """Shorten Deflect Length"""
    wait(0.300)
    set_ability2_enabled(event_player(), False)
    set_ability1_enabled(event_player(), False)
    wait(0.500)
    set_ability1_enabled(event_player(), True)
    set_ability2_enabled(event_player(), True)


@ongoing_global
@rules(
    wrap(lambda: Global.SlotOfTargetedPlayer) == -1,
    is_game_in_progress() == True,
)
def target_random_player():
    """Target Random Player"""
    Global.SlotOfTargetedPlayer = first_of(filtered_array(all_players(ALL_TEAMS), CURRENT_ARRAY_ELEMENT.hasMoved))


@ongoing_each_player(ALL_TEAMS, ALL)
@rules(
    wrap(lambda: distance_between(eye_position(event_player()), vector(x_component_of(Global.CircleCenter.value), y_component_of(eye_position(event_player())), z_component_of(Global.CircleCenter.value)))) > 40
)
def push_to_circle():
    """Push to Circle"""
    apply_impulse(event_player(), direction_towards(eye_position(event_player()), Global.CircleCenter.value) * vector(1, 0, 1), 6)
    apply_impulse(event_player(), vector(0, 1, 0), 3)


@ongoing_each_player(ALL_TEAMS, ALL)
@rules(wrap(lambda: distance_between(eye_position(event_player()), Global.CircleCenter.value)) < wrap(lambda: float(Global.CenterOffLimitsSize) + 0.5))
def put_out_center():
    """Put out Center"""
    apply_impulse(event_player(), direction_towards(Global.CircleCenter.value, event_player()), 10)
    apply_impulse(event_player(), vector(0, 1, 0), 1.5)


@ongoing_each_player(ALL_TEAMS, ALL)
@rules(
    is_button_held(event_player, JUMP),
    is_alive(event_player) == True,
    wrap(event_player.getter("BouncePadCooldown")) == 0,
)
def bounce_when_near_pad():
    """Bounce When Near Pad"""
    near = any(
        distance_between(bp.value, eye_position(event_player())) <= 2.75
        for bp in [Global.BouncePad1, Global.BouncePad2, Global.BouncePad3, Global.BouncePad4]
    )
    if not near:
        return
    play_effect(all_players(ALL_TEAMS), "Ring Explosion Sound", "White", eye_position(event_player()) * vector(1, 0, 1), 25)
    play_effect(all_players(ALL_TEAMS), "Good Pickup Effect", "White", eye_position(event_player()) * vector(1, 0, 1), 2)
    apply_impulse(event_player(), vector(0, 1, 0), 25)
    event_player.BouncePadCooldown = 5


def _ball_delete_requested():
    """Ball Delete Requested (Subroutine BallDR)"""
    Global.SlotOfTargetedPlayer = -1
    Global.BallIsOut = False
    stop_chasing_global_variable("BallDirection")
    stop_chasing_global_variable("BallPosition")
    stop_chasing_global_variable("BallSpeed")
    Global.BallSpawnCountdown = 5
    Global.BallPosition = vector(0, -1, 0)
    Global.BallDirection = vector(0, 0, 0)
    Global.SlotOfPreviousTargetedPlayer = -1
    Global.PrevBallPos = vector(0, 0, 0)
    Global.PrevBallPos2 = vector(0, 0, 0)


@ongoing_global
@rules(
    wrap(lambda: Global.IsEnoughPlayersToStart) == True,
    is_game_in_progress() == True,
)
def start_round():
    """Start Round"""
    Global.BallSpawnCountdown = 5
    for p in ALL_PLAYERS:
        p.hasMoved = True
    chase_global_variable_at_rate("BallSpawnCountdown", 0, 1)
    Global.RoundInProgress = True
    chase_player_variable_at_rate(all_players(ALL_TEAMS), "BouncePadCooldown", 0, 1)


@ongoing_global
@rules(
    is_game_in_progress() == True,
)
def spawn_ball():
    """Spawn Ball"""
    if (not Global.BallSpawnCountdown and Global.IsEnoughPlayersToStart) or (
        is_button_held(first_of(all_players(ALL_TEAMS)), RELOAD) and number_of_players(ALL_TEAMS) == 1
    ):
        if number_of_players(ALL_TEAMS) <= 1:
            if Global.BallIsOut:
                return
            Global.SlotOfTargetedPlayer.BouncePadCooldown = 0
            chase_player_variable_at_rate(all_players(ALL_TEAMS), "BouncePadCooldown", 0, 1)
        Global.BallIsOut = True
        Global.BallPosition = Global.CircleCenter.value
        Global.BallDirection = direction_towards(Global.BallPosition.value, Global.SlotOfTargetedPlayer)
        Global.BallSpeed = first_of(Global.number_p)


@ongoing_global
@rules(
    count_of(filtered_array(all_living_players(ALL_TEAMS), CURRENT_ARRAY_ELEMENT.hasMoved)) == 2,
    wrap(lambda: Global.IsInFinalDuel) == False,
    wrap(lambda: Global.IsEnoughPlayersToStart) == True,
)
def final_duel():
    """Final Duel"""
    if Global.BallIsOut:
        BallDR()
    Global.IsInFinalDuel = True


@ongoing_global
@rules(
    count_of(filtered_array(all_living_players(ALL_TEAMS), CURRENT_ARRAY_ELEMENT.hasMoved)) == 1,
    wrap(lambda: Global.IsEnoughPlayersToStart) == True,
)
def player_win():
    """Player Win"""
    Global.IsInFinalDuel = False
    winners = filtered_array(all_living_players(ALL_TEAMS), CURRENT_ARRAY_ELEMENT.hasMoved)
    modify_player_score(winners, 1)
    stop_chasing_global_variable("BallSpawnCountdown")
    stop_chasing_player_variable(all_players(ALL_TEAMS), "BouncePadCooldown")
    big_message(all_players(ALL_TEAMS), f"{first_of(winners)} 승리!")
    wait(2)
    RP()
    if not Global.Overtime and not getattr(Global, "MatchTime", 0):
        if Global.True_or_False[3]:
            wait(2)
            restart_match()
            return
    Global.RoundInProgress = False
    for p in ALL_PLAYERS:
        p.BouncePadCooldown = 5
    Global.SlotOfTargetedPlayer = -1
    chase_global_variable_at_rate("BallSpawnCountdown", 0, 1)
    chase_player_variable_at_rate(all_players(ALL_TEAMS), "BouncePadCooldown", 0, 1)
    Global.RoundInProgress = True


@ongoing_global
@rules(wrap(lambda: Global.BallIsOut) == True)
def ball_motion():
    """Ball Motion (Has to Be Done Weird Due to Chase Vector Variable Bugs)"""
    Global.PrevBallPos2 = Global.PrevBallPos
    Global.PrevBallPos = Global.BallPosition
    chase_global_variable_at_rate("BallPosition", Global.BallPosition.value + Global.BallDirection.value * float(Global.BallSpeed), float(Global.BallSpeed))
    chase_global_variable_at_rate("BallDirection", direction_towards(Global.BallPosition.value, eye_position(Global.SlotOfTargetedPlayer)), 1.75)
    chase_global_variable_at_rate("BallSpeed", 100, 0.1)


@ongoing_global
@rules(wrap(lambda: Global.BallIsOut) == True)
def ball_reaches_player():
    """Ball Reaches Player"""
    # Simplified proximity check
    if distance_between(Global.BallPosition.value, eye_position(Global.SlotOfTargetedPlayer)) > 1.9:
        return
    # Effects and scoring simplified
    if not (getattr(Global.SlotOfTargetedPlayer, "is_ability1", False) or getattr(Global.SlotOfTargetedPlayer, "is_ability2", False)):
        CoolDeathEffects()
        return
    set_status(Global.SlotOfTargetedPlayer, None, "Stunned", 1)
    if number_of_players(ALL_TEAMS) != 1:
        teleport(Global.SlotOfTargetedPlayer, Global.BallPosition.value)
    play_effect(all_players(ALL_TEAMS), "Ring/Explosion", "White", Global.BallPosition, 2)
    Global.SlotOfTargetedPlayer.BallScore = (Global.SlotOfTargetedPlayer.BallScore or 0) + 1
    Global.SlotOfPreviousTargetedPlayer = Global.SlotOfTargetedPlayer
    current_speed = Global.BallSpeed.value or first_of(Global.number_p)
    Global.BallSpeed = min(Global.number_p[1], current_speed * 1.04)
    stop_chasing_global_variable("BallDirection")
    Global.BallDirection = facing_direction_of(Global.SlotOfTargetedPlayer)


@ongoing_global
@rules(
    wrap(lambda: Global.BallIsOut) == True,
)
def ball_bounce_off_surface():
    """Ball Bounce off Surface"""
    # Reflect direction against a fake normal
    n = ray_cast_hit_normal(Global.BallPosition.value, Global.BallPosition.value + Global.BallDirection.value * float(Global.BallSpeed) * 0.033)
    v = Global.BallDirection.value
    dp = 2 * dot_product(v, n) / max(0.0001, dot_product(n, n))
    Global.BallDirection = v - n * dp


@ongoing_global
@rules(wrap(lambda: Global.BallIsOut) == True)
def ball_no_down_when_y_below():
    """Ball No Down When y < -0.5"""
    if y_component_of(Global.BallPosition.value) < -0.5 and y_component_of(Global.BallDirection.value) < 0:
        Global.BallDirection = Global.BallDirection.value * vector(1, 0, 1)
        play_effect(all_players(ALL_TEAMS), "Ring Explosion", "White", Global.BallPosition.value, 2)


@ongoing_global
@rules(wrap(lambda: Global.BallIsOut) == True)
def chamber_x_collision():
    """Chamber x Collision"""
    if abs(x_component_of(Global.BallPosition.value)) + 0.4 >= 20:
        if x_component_of(Global.BallPosition.value) * x_component_of(Global.BallDirection.value) > 0:
            Global.BallDirection = vector(-x_component_of(Global.BallDirection.value), y_component_of(Global.BallDirection.value), z_component_of(Global.BallDirection.value))
            play_effect(all_players(ALL_TEAMS), "Bad Explosion", "White", Global.BallPosition.value, 1)


@ongoing_global
@rules(compare(Global.BallIsOut, "==", True))
def chamber_y_collision():
    """Chamber y Collision"""
    y = y_component_of(Global.BallPosition.value)
    if (y >= 39.6 or y < 0.4):
        if ((y + 0.4 >= 40 and y_component_of(Global.BallDirection.value) > 0) or (y - 0.4 <= 0 and y_component_of(Global.BallDirection.value) < 0)):
            Global.BallDirection = vector(x_component_of(Global.BallDirection.value), -y_component_of(Global.BallDirection.value), z_component_of(Global.BallDirection.value))
            play_effect(all_players(ALL_TEAMS), "Bad Explosion", "White", Global.BallPosition.value, 1)


@ongoing_global
@rules(compare(Global.BallIsOut, "==", True))
def chamber_z_collision():
    """Chamber z Collision"""
    if abs(z_component_of(Global.BallPosition.value)) + 0.4 >= 20:
        if z_component_of(Global.BallPosition.value) * z_component_of(Global.BallDirection.value) > 0:
            Global.BallDirection = vector(x_component_of(Global.BallDirection.value), y_component_of(Global.BallDirection.value), -z_component_of(Global.BallDirection.value))
            play_effect(all_players(ALL_TEAMS), "Bad Explosion", "White", Global.BallPosition.value, 1)


@ongoing_each_player(ALL_TEAMS, ALL)
@rules(is_button_held(event_player, INTERACT), is_button_held(event_player, CROUCH))
def set_player_vision():
    """Set Player Vision"""
    if getattr(event_player(), "angle", False):
        start_camera(event_player(), ray_cast_hit_position(eye_position(event_player()), eye_position(event_player()) + world_vector_of(vector(0, 0, 0), event_player(), "Rotation") + facing_direction_of(event_player()) * -3.780, None, event_player(), False), event_player() + facing_direction_of(event_player()) * 1000, 65)
        event_player.angle = False
    else:
        stop_camera(event_player())
        event_player.angle = True


@ongoing_each_player(ALL_TEAMS, ALL)
@rules(is_button_held(event_player, MELEE), is_button_held(event_player, INTERACT))
def set_player_aim_speed():
    """Set Player aim speed"""
    if getattr(event_player(), "aimSpeed", False):
        set_aim_speed(event_player(), 100)
        small_message(event_player(), "감도 × 1.0")
        event_player.aimSpeed = False
    else:
        set_aim_speed(event_player(), 200)
        small_message(event_player(), "감도 × 2.0")
        event_player.aimSpeed = True


@ongoing_each_player(ALL_TEAMS, ALL)
@rules(is_button_held(event_player, ULTIMATE))
def score_board_toggle():
    """Score Board On/Off"""
    if event_player.ToggleHUD is True:
        enable_game_mode_hud(event_player())
        event_player.ToggleHUD = False
    else:
        disable_game_mode_hud(event_player())
        event_player.ToggleHUD = True


def RP():
    """Reset Players (subroutine)"""
    Global.SubPlayer = (
        filtered_array(all_players(ALL_TEAMS), compare(score_of(CURRENT_ARRAY_ELEMENT), "==", Global.HighestScore))
        if Global.Overtime
        else all_players(ALL_TEAMS)
    )
    resurrect(Global.SubPlayer)
    for p in Global.SubPlayer:
        p.hasMoved = True
    set_melee_enabled(Global.SubPlayer, False)
    set_status(Global.SubPlayer, None, "Invincible", 9999)
    clear_status(Global.SubPlayer, "Frozen")
    teleport(filtered_array(Global.SubPlayer, CURRENT_ARRAY_ELEMENT.Punch), vector(0, 5, 0))
    set_jump_vertical_speed(Global.SubPlayer, 100)
    for p in Global.SubPlayer:
        p.Punch = False
    heal(Global.SubPlayer, None, 200)


@ongoing_each_player(ALL_TEAMS, ALL)
@rules(
    compare(lambda: is_button_held(event_player, MELEE) and is_button_held(event_player, JUMP), "==", True),
    compare(lambda: Global.True_or_False[7], "==", True),
    compare(event_player.getter("hasMoved"), "==", False),
)
def let_player_play_minigame():
    """Let Player Play to Mini Game #"""
    resurrect(event_player())
    teleport(event_player(), vector(random_real(-15, 15), 47, random_real(-15, 15)))
    if event_player.Punch:
        return
    event_player.Punch = True
    set_melee_enabled(event_player(), True)
    clear_status(event_player(), "Invincible")
    set_jump_vertical_speed(event_player(), 81.3)


@ongoing_each_player(ALL_TEAMS, ALL)
def when_player_falls():
    """When Player Falls #"""
    if y_component_of(eye_position(event_player())) < -0.1:
        if first_of(Global.True_or_False):
            kill(event_player(), None)
        else:
            set_status(event_player(), None, "Frozen", 3)
            small_message(all_players(ALL_TEAMS), f"-> {event_player()}")
            teleport(event_player(), vector(random_real(-15, 15), 45, random_real(-15, 15)))


@ongoing_each_player(ALL_TEAMS, ALL)
@rules(entity_exists(Global.SlotOfTargetedPlayer) != True)
def when_target_player_leaves():
    """When Target Player Leaves"""
    BallDR()


@ongoing_global
def color_red():
    """Red"""
    bs = Global.BallSpeed.value or 0
    if Global.SetColor != "Red" and abs(bs - 47) <= 7:
        Global.SetColor = "Red"


@ongoing_global
def color_purple():
    """Purple"""
    bs = Global.BallSpeed.value or 0
    if Global.SetColor != "Purple" and abs(bs - 67) < 13:
        Global.SetColor = "Purple"


@ongoing_global
def color_black():
    """Black"""
    bs = Global.BallSpeed.value or 0
    if Global.SetColor != "Black" and bs >= 80:
        Global.SetColor = "Black"


@ongoing_global
def spawn_destroy_bot():
    """Spawn & Destroy Bot (simplified)"""
    # Placeholder for bot spawn/destroy controls
    return None


@ongoing_global
def after_bot_use_ability2():
    """After Bot Use Ability 2 (simplified)"""
    return None


@ongoing_each_player(ALL_TEAMS, ALL)
@rules(
    wrap(lambda: Global.True_or_False[5]) == True,
    is_dummy_bot(event_player) == True,
)
def bot_facing():
    """Bot Facing"""
    if distance_between(event_player(), Global.BallPosition) <= first_of(Global.Distance or [0]):
        # Face ball or nearest player
        dir1 = direction_towards(eye_position(event_player()), Global.BallPosition)
        set_facing(event_player(), dir1)


@ongoing_each_player(ALL_TEAMS, ALL)
@rules(is_game_in_progress() == True, is_dummy_bot(event_player) == True)
def bot_move():
    """Bot Move"""
    if Global.True_or_False[2]:
        event_player.BotTargetpos = vector(random_real(-15, 15), 0, random_real(-15, 15))
        start_throttle_in_direction(event_player(), direction_towards(event_player(), event_player.BotTargetpos) + (Global.BallDirection or vector(0,0,0)) * vector(-7, 0, 0), 1)
    else:
        start_forcing_player_position(event_player(), event_player(), True)


def windmill():
    """Bot Move 2"""
    # Subroutine: move in a spinning pattern towards target
    d = facing_direction_of(event_player())
    event_player.D = d
    start_throttle_in_direction(event_player(), d, 1)


@ongoing_global
@rules(
    count_of(filtered_array(all_living_players(ALL_TEAMS), CURRENT_ARRAY_ELEMENT.hasMoved)) == 0,
    is_game_in_progress() == True,
)
def all_players_dead_failsafe():
    """All Players Dead Failsafe"""
    RP()
    Global.IsInFinalDuel = False
    if Global.BallIsOut:
        BallDR()
    Global.RoundInProgress = False
    stop_chasing_global_variable("BallSpawnCountdown")
    stop_chasing_player_variable(all_players(ALL_TEAMS), "BouncePadCooldown")
    for p in ALL_PLAYERS:
        p.BouncePadCooldown = 5
    Global.BallSpawnCountdown = 5
    wait(1)
    # Loop while waiting for enough players
    wait(1)
    if not Global.IsEnoughPlayersToStart:
        return
    chase_player_variable_at_rate(all_players(ALL_TEAMS), "BouncePadCooldown", 0, 1)
    chase_global_variable_at_rate("BallSpawnCountdown", 0, 1)
    Global.RoundInProgress = True
    Global.BallPosition = vector(0, -1, 0)


@ongoing_each_player(ALL_TEAMS, ALL)
@rules(is_using_ability(event_player, 1))
def dash_slow():
    """Dash Slow"""
    event_player.MoveSpeed = 0
    # Approximate chase by setting towards 100
    rate = max(event_player.MoveSpeed or 0, 16) ** 1.250
    chase_player_variable_at_rate([event_player()], "MoveSpeed", 100, rate)
    # Simulate incremental application
    guard = 0
    while (event_player.MoveSpeed != 100) and guard < 20:
        set_move_speed(event_player(), event_player.MoveSpeed)
        set_gravity(event_player(), event_player.MoveSpeed)
        wait(0.1)
        guard += 1
    set_move_speed(event_player(), 100)
    set_gravity(event_player(), 100)


if __name__ == "__main__":
    print(bool(compare(1,">",0)))
