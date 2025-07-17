"""
    Board class:
    This class represents the complete game board setup for a two-player seed-sowing game
    (e.g., Mancala or similar). It handles initialization, board structure, and player linkage.
    Key responsibilities include:
    - Creating houses and stores for each player with a specified number of seeds.
    - Linking houses and stores in a circular fashion to facilitate turn logic.
    - Constructing and maintaining references to Player and Players objects.

    Dependencies:
    - House: Represents a single pit or house that holds seeds.
    - Store: Represents a player's scoring pit (store).
    - Player: Represents a single player's state and actions.
    - PlayerNumber: Enum used to differentiate between Player One and Player Two.
    - Players: Container for accessing both Player instances.
"""

from middletier.pit import Pit


class House(Pit):
    def __init__(self, owner: 'PlayerNumber', seeds: int):
        super().__init__(owner, seeds, is_sowable=True)

    def take(self) -> int:
        seeds = self.seeds
        self.seeds = 0
        return seeds

    def __str__(self) -> str:
        return f"House(seeds={self.seeds}, owner={self.owner})"
