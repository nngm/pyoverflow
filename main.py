from overwatch import *

class player(player_parent):
    pass

class _global:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(_global, cls).__new__(cls, *args, **kwargs)
        return cls._instance
    
    def __init__(self):
        self.foo = "bar"
        self.description: Final = "blah blah"
    
Global: _global = _global()

@ongoing_global
def init_global_variables():
    Global.foo = custom_string("bar")

if __name__ == "__main__":
    while True:
        for func in global_functions:
            func()