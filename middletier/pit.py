"""
    Pit class:
    This class defines the basic structure and behavior of a pit on the game board,
    which may represent either a house or a store depending on subclass implementation.
    It maintains seed count, links to adjacent pits, and information about sowability.
    Designed for extension by more specific pit types like House and Store.

    Key responsibilities include:
    - Holding and modifying the number of seeds in the pit.
    - Managing links to the next and previous pits for circular traversal.
    - Indicating whether the pit can be sown into during a move.

    Dependencies:
    - PlayerNumber: Enum used to identify the pit's owner.
"""

from middletier import player_number


class Pit:
    def __init__(self, owner: 'player_number', seeds: int, is_sowable: bool):
        self.owner: player_number = owner
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
