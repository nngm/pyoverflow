class AutoArray(list):
    def __setitem__(self, idx, value):
        if isinstance(idx, int) and idx >= len(self):
            self.extend([None] * (idx - len(self) + 1))
        super().__setitem__(idx, value)


class WorkshopVar:
    __slots__ = ("name", "_value")

    def __init__(self, name: str):
        self.name = name
        self._value = None

    def __get__(self, obj, objtype=None):
        return self

    def __set__(self, obj, value):
        self._value = value

    def _ensure_array(self):
        if not isinstance(self._value, AutoArray):
            self._value = AutoArray()

    def __setitem__(self, idx, value):
        self._ensure_array()
        self._value[idx] = value

    def __getitem__(self, idx):
        if isinstance(self._value, AutoArray):
            return self._value[idx]
        raise TypeError(f"{self.name} is currently a scalar, not an array.")

    def __repr__(self):
        return f"<WorkshopVar {self.name}={self._value!r}>"

    def __int__(self):
        return int(self._value)

    def __float__(self):
        return float(self._value)

    def __bool__(self):
        return bool(self._value)

    def __iter__(self):
        if isinstance(self._value, AutoArray):
            return iter(self._value)
        raise TypeError(f"{self.name} is currently a scalar, not an array.")

    @property
    def value(self):
        return self._value


class WorkshopVarMeta(type):
    def __new__(mcls, name, bases, namespace):
        new_ns = {}
        for k, v in namespace.items():
            if v is None and not k.startswith("_"):
                new_ns[k] = WorkshopVar(k)
            else:
                new_ns[k] = v
        return super().__new__(mcls, name, bases, new_ns)
