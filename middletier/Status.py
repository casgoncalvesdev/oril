from enum import Enum

class Status(Enum):
    ACTIVE = "ACTIVE"
    PLAYER_ONE_WIN = "PLAYER_ONE_WIN"
    PLAYER_TWO_WIN = "PLAYER_TWO_WIN"
    DRAW = "DRAW"