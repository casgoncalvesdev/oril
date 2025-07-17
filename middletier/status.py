"""
    Status enum:
    This enumeration defines the possible states of the game at any given moment.
    It is used to track the game's progress and outcome.

    Key responsibilities include:
    - Representing whether the game is ongoing or has ended.
    - Indicating the result of the game when completed (win, loss, or draw).

    Values:
    - ACTIVE: The game is still in progress.
    - PLAYER_ONE_WIN: Player One has won the game.
    - PLAYER_TWO_WIN: Player Two has won the game.
    - DRAW: The game ended in a tie.
"""
from enum import Enum

class Status(Enum):
    ACTIVE = "ACTIVE"
    PLAYER_ONE_WIN = "PLAYER_ONE_WIN"
    PLAYER_TWO_WIN = "PLAYER_TWO_WIN"
    DRAW = "DRAW"
