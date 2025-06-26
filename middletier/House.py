from middletier.Pit import Pit


class House(Pit):
    def __init__(self, owner: 'PlayerNumber', seeds: int):
        super().__init__(owner, seeds, is_sowable=True)

    def take(self) -> int:
        seeds = self.seeds
        self.seeds = 0
        return seeds

    def __str__(self) -> str:
        return f"House(seeds={self.seeds}, owner={self.owner})"
