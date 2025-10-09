from typing import *
from overflow.DSL.ctx_init import _ctx

_ctx.cur_arr_elem = None


class _CurrentElementProxy:
    def __getattr__(self, name: str) -> Callable[[], Any]:
        def getter():
            return getattr(_ctx.cur_arr_elem, name)

        return getter

    def __getitem__(self, key: Any) -> Callable[[], Any]:
        def getter():
            return _ctx.cur_arr_elem[key]

        return getter


CURRENT_ARRAY_ELEMENT = _CurrentElementProxy()
