import math
import copy
import pathlib
from typing import Any, Iterator, Iterable, Optional, Tuple
# ==========================================================
# 2) Dunder ("__double_underscore__") Showcase
#    This section gives runnable, bite-sized examples of almost
#    every special method you can implement in pure Python.
#    Grouped by category for teaching. Many simply delegate to a
#    backing value to stay compact.
# ==========================================================

# ---- Numeric conversions & truthiness ----
class NumberBox:
    """Wraps an int and implements many numeric/bit operations.
    Useful to demo __int__, arithmetic pairs (normal/reflected/in-place),
    and unary ops. Not every op does domain checks (kept short)."""

    def __init__(self, value: int):
        self.value = int(value)

    # Representations
    def __repr__(self) -> str:
        return f"NumberBox({self.value!r})"

    def __str__(self) -> str:
        return f"nb[{self.value}]"

    # Conversions
    def __bool__(self) -> bool:
        return self.value != 0

    def __int__(self) -> int:
        return int(self.value)

    def __float__(self) -> float:
        return float(self.value)

    def __complex__(self) -> complex:
        return complex(self.value)

    def __index__(self) -> int:  # allows use in slicing and low-level ops
        return int(self.value)

    def __round__(self, ndigits: Optional[int] = None):
        return round(self.value, ndigits) if ndigits is not None else round(self.value)

    def __floor__(self):
        return math.floor(self.value)

    def __ceil__(self):
        return math.ceil(self.value)

    def __trunc__(self):
        return math.trunc(self.value)

    # Unary numerical ops
    def __neg__(self):
        return NumberBox(-self.value)

    def __pos__(self):
        return NumberBox(+self.value)

    def __abs__(self):
        return NumberBox(abs(self.value))

    def __invert__(self):  # bitwise not
        return NumberBox(~self.value)

    # Comparison (again here, to show reuse)
    def __eq__(self, other: object) -> bool:
        if isinstance(other, NumberBox):
            return self.value == other.value
        if isinstance(other, int):
            return self.value == other
        return NotImplemented

    def __lt__(self, other: object) -> bool:
        if isinstance(other, NumberBox):
            return self.value < other.value
        if isinstance(other, int):
            return self.value < other
        return NotImplemented

    def __hash__(self) -> int:
        return hash(self.value)


# ---- String/bytes/format/path-like ----
class Printable:
    def __init__(self, name: str):
        self.name = name

    def __repr__(self) -> str:
        return f"Printable(name={self.name!r})"

    def __str__(self) -> str:
        return self.name

    def __format__(self, spec: str) -> str:
        return f"<{self.name}:{spec}>"

    def __bytes__(self) -> bytes:
        return self.name.encode()


# ---- Attribute access hooks ----
class AttrDemo:
    def __init__(self):
        # Use __setattr__ safely by writing directly to __dict__ to avoid recursion
        self.__dict__["existing"] = 123

    def __getattribute__(self, name: str) -> Any:
        if name == "always":
            return "present via __getattribute__"
        return super().__getattribute__(name)

    def __getattr__(self, name: str) -> Any:
        # Only called if normal lookup fails
        return f"<dynamic:{name}>"

    def __setattr__(self, name: str, value: Any) -> None:
        # Example: forbid setting names starting with 'x_'
        if name.startswith("x_"):
            raise AttributeError("x_* attributes are read-only")
        self.__dict__[name] = value

    def __delattr__(self, name: str) -> None:
        self.__dict__.pop(name, None)

    def __dir__(self) -> Iterable[str]:
        return sorted(set(list(self.__dict__.keys()) + ["always", "virtual"]))



# ---- Containers / sequences / iterators ----
class Bag:
    def __init__(self, items: Iterable[Any] = ()):  # simple mutable container
        self._data = list(items)

    def __len__(self) -> int:
        return len(self._data)

    def __length_hint__(self) -> int:
        return len(self._data)

    def __iter__(self) -> Iterator[Any]:
        return iter(self._data)

    def __reversed__(self) -> Iterator[Any]:
        return reversed(self._data)

    def __contains__(self, item: Any) -> bool:
        return item in self._data

    def __getitem__(self, idx):
        return self._data[idx]

    def __setitem__(self, idx, value):
        self._data[idx] = value

    def __delitem__(self, idx):
        del self._data[idx]


# ---- Object lifecycle ----
class Lifecycle:
    def __new__(cls, *args, **kwargs):
        obj = super().__new__(cls)
        return obj

    def __init__(self, name: str):
        self.name = name

    def __del__(self):  # NOTE: timing is implementation-dependent
        # avoid heavy work here; shown only for completeness
        return None


# Manual testing exmaples
if __name__ == "__main__":
    # Comparison/hash
    g1, g2 = NumberBox(1), NumberBox(2)
    assert g1 < g2 and hash(g1) != 0

    # NumberBox arithmetic
    nb = NumberBox(10)
    nb += 5
    assert int(nb) == 15
    _q, _r = divmod(nb, 4)

    # Printable/bytes/format
    p = Printable("hello")
    assert bytes(p) == b"hello"
    assert f"{p:upper}" == "<hello:upper>"

    # Attr hooks
    ad = AttrDemo()
    assert ad.always == "present via __getattribute__"
    assert ad.missing == "<dynamic:missing>"

    # Container
    bag = Bag([1, 2, 3])
    assert 2 in bag and bag[0] == 1

    print("Dunder showcase sanity checks passed.")
