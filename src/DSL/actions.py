from typing import Any, Iterable, Optional
from .values import *

# Simple action placeholders used by decompiled Workshop rules.
# These are no-ops or lightweight state mutations so Python code can run.

_LAST_CREATED_ENTITY: Any = None


def set_move_speed(player: Any, value: float) -> None:
    try:
        player.MoveSpeed = value
    except Exception:
        pass


def set_gravity(player: Any, value: float) -> None:
    try:
        player.Gravity = value
    except Exception:
        pass


def wait(seconds: float, ignore_condition: bool = True) -> None:
    # No real-time waiting by default to keep runs fast.
    return None


def chase_player_variable_at_rate(
    players: Iterable[Any], attr: str, destination: Any, rate: float
) -> None:
    for p in getattr(players, "view", lambda: players)():
        try:
            setattr(p, attr, destination)
        except Exception:
            continue


def chase_global_variable_at_rate(name: str, destination: Any, rate: float) -> None:
    import src.DSL.owglobals as og

    try:
        setattr(og, name, destination)
    except Exception:
        pass


def chase_global_variable_over_time(name: str, destination: Any, duration: float) -> None:
    chase_global_variable_at_rate(name, destination, rate=0)


def stop_chasing_global_variable(name: str) -> None:
    return None


def stop_chasing_player_variable(players: Iterable[Any], attr: str) -> None:
    return None


def kill(victim: Any, killer: Optional[Any] = None) -> None:
    # Placeholder: could set a flag if needed.
    setattr(victim, "is_dead", True)


def set_status(target: Any, other: Any, status: str, duration: float) -> None:
    # Placeholder to record status effect.
    try:
        target._status = (status, duration)
    except Exception:
        pass


def teleport(target: Any, position: Any) -> None:
    try:
        target.position = position
    except Exception:
        pass


def create_effect(viewers: Any, effect: str, color: Any, position: Any, size: float) -> Any:
    global _LAST_CREATED_ENTITY
    _LAST_CREATED_ENTITY = {"type": "effect", "effect": effect, "pos": position, "size": size, "color": color}
    return _LAST_CREATED_ENTITY


def create_beam_effect(viewers: Any, beam: str, start: Any, end: Any, color: Any) -> Any:
    global _LAST_CREATED_ENTITY
    _LAST_CREATED_ENTITY = {"type": "beam", "beam": beam, "start": start, "end": end, "color": color}
    return _LAST_CREATED_ENTITY


def destroy_effect(entity: Any) -> None:
    return None


def last_created_entity() -> Any:
    return _LAST_CREATED_ENTITY


def play_effect(viewers: Any, effect: str, color: Any, position: Any, size: float) -> None:
    return None


# Additional no-op or light state actions used by 5HPAT
def create_hud_text(viewers: Any, header: Any, subheader: Any, text: str, align=None, sort_order=None, color1=None, color2=None, color3=None, visibility=None, visibility2=None) -> Any:
    return None


def create_in_world_text(viewers: Any, text: str, position: Any, size: float, clip=None, visibility=None, color=None, visibility2=None) -> Any:
    return None


def create_progress_bar_in_world_text(viewers: Any, value: float, max_value: Optional[float], position: Any, size: float, clip=None, color1=None, color2=None, visibility=None, visibility2=None) -> Any:
    return None


def wait_until(condition: bool, timeout: float) -> None:
    return None


def set_match_time(value: float) -> None:
    return None


def pause_match_time() -> None:
    return None


def unpause_match_time() -> None:
    return None


def restart_match() -> None:
    return None


def set_player_score(players: Iterable[Any], value: int) -> None:
    for p in getattr(players, "view", lambda: players)():
        setattr(p, "score", value)


def modify_player_score(players: Iterable[Any], delta: int) -> None:
    for p in getattr(players, "view", lambda: players)():
        setattr(p, "score", getattr(p, "score", 0) + delta)


def enable_game_mode_hud(player: Any) -> None:
    return None


def disable_game_mode_hud(player: Any) -> None:
    return None


def set_jump_vertical_speed(players: Iterable[Any] | Any, value: float) -> None:
    if isinstance(players, list) or hasattr(players, "view"):
        iterable = getattr(players, "view", lambda: players)()
    else:
        iterable = [players]
    for p in iterable:
        setattr(p, "jump_vertical_speed", value)


def set_aim_speed(player: Any, value: float) -> None:
    setattr(player, "aim_speed", value)


def enable_death_spectate_all_players(player: Any) -> None:
    return None


def enable_death_spectate_target_hud(player: Any) -> None:
    return None


def disable_built_in_game_mode_respawning(player: Any) -> None:
    return None


def disable_built_in_game_mode_scoring() -> None:
    return None


def disable_built_in_game_mode_completion() -> None:
    return None


def disable_built_in_game_mode_music() -> None:
    return None


def disable_built_in_game_mode_announcer() -> None:
    return None


def disable_inspector_recording() -> None:
    return None


def set_damage_dealt(player: Any, value: float) -> None:
    setattr(player, "damage_dealt", value)


def set_melee_enabled(players: Iterable[Any] | Any, enabled: bool) -> None:
    if isinstance(players, list) or hasattr(players, "view"):
        iterable = getattr(players, "view", lambda: players)()
    else:
        iterable = [players]
    for p in iterable:
        setattr(p, "melee_enabled", enabled)


def clear_status(player: Any, status: str) -> None:
    setattr(player, "_status", None)


def heal(players: Iterable[Any] | Any, healer: Any, amount: float) -> None:
    if isinstance(players, list) or hasattr(players, "view"):
        iterable = getattr(players, "view", lambda: players)()
    else:
        iterable = [players]
    for p in iterable:
        setattr(p, "health", min(200, getattr(p, "health", 200) + amount))


def resurrect(players: Iterable[Any] | Any) -> None:
    if isinstance(players, list) or hasattr(players, "view"):
        iterable = getattr(players, "view", lambda: players)()
    else:
        iterable = [players]
    for p in iterable:
        setattr(p, "is_dead", False)


def remove_player(players: Iterable[Any]) -> None:
    return None


def big_message(viewers: Any, text: str) -> None:
    return None


def small_message(viewers: Any, text: str) -> None:
    return None


def start_camera(player: Any, pos: Any, target: Any, fov: float) -> None:
    return None


def stop_camera(player: Any) -> None:
    return None


def apply_impulse(player: Any, direction: vector, magnitude: float, to_world: Any = None, mode: Any = None) -> None:
    return None


def set_ability_enabled(player: Any, index: int, enabled: bool) -> None:
    setattr(player, f"ability{index}_enabled", enabled)


def set_ability1_enabled(player: Any, enabled: bool) -> None:
    set_ability_enabled(player, 1, enabled)


def set_ability2_enabled(player: Any, enabled: bool) -> None:
    set_ability_enabled(player, 2, enabled)


def press_button(player: Any, button: Buttons) -> None:
    # No-op placeholder; could set flags mapped in rules.is_button_held
    return None


def communicate(player: Any, kind: Any) -> None:
    return None


def start_throttle_in_direction(player: Any, direction: vector, magnitude: float, to_world=None, replace_existing=None, mode=None) -> None:
    return None


def stop_throttle_in_direction(player: Any) -> None:
    return None


def start_facing(player: Any, direction: vector, rate: float, to_world=None, mode=None) -> None:
    player.facing = direction


def set_facing(player: Any, direction: vector, to_world=None) -> None:
    player.facing = direction


def start_forcing_player_position(player: Any, position: Any, force: bool) -> None:
    player.position = getattr(position, "position", position)
