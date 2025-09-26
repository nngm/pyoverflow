from contextlib import contextmanager
from src.DSL.ctx_init import _ctx


class EventPlayer:
    def __init__(self, ctx):
        object.__setattr__(self, "_ctx", ctx)

    def _require_current(self):
        cur = self._ctx.event_player
        if cur is None:
            raise RuntimeError(
                "event_player context is empty. Use inside with with_event_player(player)."
            )
        return cur

    def __call__(self):
        return self._require_current()

    def __getattr__(self, name):
        cur = self._require_current()
        return getattr(cur, name)

    def __setattr__(self, name, value):
        if name.startswith("_"):
            object.__setattr__(self, name, value)
        else:
            cur = self._require_current()
            setattr(cur, name, value)

    def __getitem__(self, key):
        cur = self._require_current()
        return cur[key]

    def __setitem__(self, key, value):
        cur = self._require_current()
        cur[key] = value

    def getter(self, name: str):
        return lambda: getattr(self._require_current(), name)


@contextmanager
def with_event_player(elem):
    prev = getattr(_ctx, "event_player", None)
    _ctx.event_player = elem
    try:
        yield
    finally:
        _ctx.event_player = prev


event_player = EventPlayer(_ctx)
