from enum import Enum, auto


class ChangesEnum(Enum):
    ADDED = auto()
    REMOVED = auto()
    INTACT = auto()
    ALTERED = auto()
    NESTED = auto()
