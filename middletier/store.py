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
        super().__init__(owner, seeds, is_sowable=False)

    def sow(self, i: int) -> None:
        self.seeds += i

    def __str__(self) -> str:
        return f"Store(seeds={self.seeds}, owner={self.owner})"
