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
        """
            Initialize a Pit with an owner, number of seeds, and sowable status.

            Args:
                owner (player_number): The owner of the pit.
                seeds (int): Initial number of seeds in the pit.
                is_sowable (bool): Whether seeds can be sown into this pit.
        """
        self.owner: player_number = owner
        self.seeds: int = seeds
        self.is_sowable: bool = is_sowable
        self.next: 'Pit' = None
        self.previous: 'Pit' = None

    def count(self) -> int:
        """Return the current number of seeds in the pit."""
        return self.seeds

    def get_next(self) -> 'Pit':
        """Return the next pit in sequence."""
        return self.next

    def set_next(self, next_pit: 'Pit') -> None:
        """
            Set the reference to the next pit.

            Args:
                next_pit (Pit): The pit to set as next.
        """
        self.next = next_pit

    def get_previous(self) -> 'Pit':
        """Return the previous pit in sequence."""
        return self.previous

    def set_previous(self, previous_pit: 'Pit') -> None:
        """
           Set the reference to the previous pit.

           Args:
               previous_pit (Pit): The pit to set as previous.
       """
        self.previous = previous_pit

    def is_sowable_pit(self) -> bool:
        """Return True if the pit can have seeds sown into it, else False."""
        return self.is_sowable

    def set_sowable(self, sowable: bool) -> None:
        """
            Set whether the pit is sowable.

            Args:
                sowable (bool): True if pit should be sowable, False otherwise.
        """
        self.is_sowable = sowable

    def sow(self, seeds: int = 1) -> None:
        """
            Add a specified number of seeds to the pit.

            Args:
            seeds (int, optional): Number of seeds to add. Defaults to 1.
        """
        self.seeds += seeds

    def is_empty(self) -> bool:
        """Return True if the pit contains no seeds."""
        return self.seeds == 0

    def take(self) -> int:
        """
            Remove and return seeds from the pit.

            Returns:
                int: Number of seeds taken (default 0; override in subclasses).
        """
        return 0  # default implementation (to be overridden)

    def __str__(self) -> str:
        """Return a string representation of the pit’s state."""
        return (f"Pit(seeds={self.seeds}, "
                f"next={type(self.next).__name__ if self.next else None}, "
                f"previous={type(self.previous).__name__ if self.previous else None}, "
                f"is_sowable={self.is_sowable}, "
                f"owner={self.owner})")
