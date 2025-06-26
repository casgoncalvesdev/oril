from middletier.Pit import Pit


class Store(Pit):
    def __init__(self, owner: 'PlayerNumber', seeds: int):
        super().__init__(owner, seeds, is_sowable=False)

    def sow(self, i: int) -> None:
        self.seeds += i

    def __str__(self) -> str:
        return f"Store(seeds={self.seeds}, owner={self.owner})"