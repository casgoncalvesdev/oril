"""
    PlayerNumber enum:
    This enumeration is used to uniquely identify the two players in the game.
    It simplifies logic by providing clear symbolic names instead of using raw integers.

    Key responsibilities include:
    - Providing a stable reference for Player One and Player Two.
    - Supporting comparisons and assignments involving player ownership and turn logic.

    Values:
    - ONE: Represents Player One.
    - TWO: Represents Player Two.
"""
from enum import Enum

class PlayerNumber(Enum):
    ONE = 1
    TWO = 2

