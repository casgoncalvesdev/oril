from middletier import PlayerNumber


class Pit:
    def __init__(self, owner: 'PlayerNumber', seeds: int, is_sowable: bool):
        self.owner: PlayerNumber = owner
        self.seeds: int = seeds
        self.is_sowable: bool = is_sowable
        self.next: 'Pit' = None
        self.previous: 'Pit' = None

    def count(self) -> int:
        return self.seeds

    def get_next(self) -> 'Pit':
        return self.next

    def set_next(self, next_pit: 'Pit') -> None:
        self.next = next_pit

    def get_previous(self) -> 'Pit':
        return self.previous

    def set_previous(self, previous_pit: 'Pit') -> None:
        self.previous = previous_pit

    def is_sowable_pit(self) -> bool:
        return self.is_sowable

    def set_sowable(self, sowable: bool) -> None:
        self.is_sowable = sowable

    def sow(self) -> None:
        self.seeds += 1

    def is_empty(self) -> bool:
        return self.seeds == 0

    def take(self) -> int:
        return 0  # default implementation (to be overridden)

    def __str__(self) -> str:
        return (f"Pit(seeds={self.seeds}, "
                f"next={type(self.next).__name__ if self.next else None}, "
                f"previous={type(self.previous).__name__ if self.previous else None}, "
                f"is_sowable={self.is_sowable}, "
                f"owner={self.owner})")
