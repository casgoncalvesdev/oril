"""
    Store class:
    This class represents a player's store (or scoring pit) in the game.
    It inherits from Pit but is specialized to accumulate captured or sown seeds.
    Unlike houses, stores are not sowable by default during regular moves.

    Key responsibilities include:
    - Holding seeds captured or accumulated during gameplay.
    - Providing functionality to add seeds (via sow).

    Dependencies:
    - Pit: Base class for all pits (houses and stores), providing shared linking and seed logic.
    - PlayerNumber: Enum identifying the owner of the store.
"""
from middletier.pit import Pit


class Store(Pit):
    def __init__(self, owner: 'PlayerNumber', seeds: int):
        """Initialize a Store with an owner and initial seed count. Store pits are not sowable."""
        super().__init__(owner, seeds, is_sowable=False)

    def sow(self, seeds: int) -> None:
        """Add a specified number of seeds to the store.

        Args:
            seeds (int): Number of seeds to add.
        """
        self.seeds += seeds

    def __str__(self) -> str:
        """Return a string representation of the Store."""
        return f"Store(seeds={self.seeds}, owner={self.owner})"
