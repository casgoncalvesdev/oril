"""
    Player class:
    This class encapsulates the logic and state for a single player in the game.
    It manages a player's houses and store, determines valid moves, executes turns,
    and calculates scores based on the game's rules.

    Key responsibilities include:
    - Managing access to the player's pits (houses and store).
    - Performing a player's move, including sowing and potential captures.
    - Checking game completion and computing the final score.
    - Providing legal move options (actions) for AI or manual play.

    Dependencies:
    - PlayerNumber: Enum identifying the player (e.g., Player One or Two).
    - House: Represents one of the player's sowable pits.
    - Store: Represents the player's scoring pit.
    - Pit: The base class for both House and Store.
"""


class Player:
    def __init__(self, num: 'PlayerNumber', houses: list['House'], store: 'Store'):
        """
        Initialize a Player with a player number, houses, and a store.

        Args:
            num (PlayerNumber): The player's identifier.
            houses (list[House]): List of houses owned by the player.
            store (Store): The player's store.
        """
        self.num = num
        self.houses = houses
        self.store = store

    def get_num(self) -> 'PlayerNumber':
        """Return the player's number."""
        return self.num

    def get_houses(self) -> list['House']:
        """Return the list of houses owned by the player."""
        return self.houses

    def get_store(self) -> 'Store':
        """Return the player's store."""
        return self.store

    def turn(self, house_num: int, sim: False = False) -> 'Pit':
        """
        Execute a turn by selecting a house and sowing seeds.

        Args:
            house_num (int): The number of the house to play.
            sim (bool, optional): Whether this is a simulation (default False).

        Returns:
            Pit: The pit where the last seed was sown.
        """
        house = self._get_house(house_num)
        self._check_has_seeds(house, sim)
        pit = self._take_turn(house)

        while self._should_capture(house, pit):
            self.store.sow(pit.take())
            pit = pit.get_previous()

        return pit

    def complete(self) -> bool:
        """Check if the player has no seeds left in any houses."""
        return all(house.is_empty() for house in self.houses)

    def finish(self) -> None:
        """Collect all remaining seeds from the houses into the store."""
        for house in self.houses:
            self.store.sow(house.take())

    def score(self) -> int:
        """Return the player's current score from the store."""
        return self.store.count()

    def _should_capture(self, house: 'House', pit: 'Pit') -> bool:
        """
        Determine whether seeds should be captured from a pit.

        Args:
            house (House): The house from which the turn started.
            pit (Pit): The pit being evaluated for capture.

        Returns:
            bool: True if capture conditions are met, False otherwise.
        """
        return (pit is not None and
                house.owner != pit.owner and
                pit.count() in (2, 3))

    def _check_has_seeds(self, house: 'House', sim: 'bool' = False) -> None:
        """
        Check if the selected house has seeds before taking a turn.

        Args:
            house (House): The house to check.
            sim (bool, optional): Whether this is a simulation (default False).

        Raises:
            ValueError: If not a simulation and the house is empty.
        """
        if not sim and house.is_empty():
            raise ValueError("House must have seeds to take turn")

    def _take_turn(self, house: 'House') -> 'Pit':
        """
        Perform the seed sowing for the turn starting from the selected house.

        Args:
            house (House): The house to start sowing from.

        Returns:
            Pit: The pit where the last seed was sown.
        """
        seeds = house.take()
        house.set_sowable(False)
        pit = house

        while seeds > 0:
            pit = pit.get_next()
            if pit.is_sowable_pit():
                seeds -= 1
                pit.sow()

        house.set_sowable(True)
        return pit

    def _get_house(self, house_num: int) -> 'House':
        """
        Retrieve the house object by its number.

        Args:
            house_num (int): The house number to retrieve.

        Returns:
            House: The corresponding house object.

        Raises:
            ValueError: If house_num is out of valid range.
        """
        if house_num < 1 or house_num > len(self.houses):
            raise ValueError(f"House number must be between 1 and {len(self.houses)}")
        return self.houses[house_num - 1]

    def get_actions(self) -> list[int]:
        """
        Get a list of valid action indices based on houses with seeds.

        Returns:
            list[int]: List of indices of houses with seeds that can be played.
        """
        actions = []
        singles = []

        for i, house in enumerate(self.houses):
            seeds = house.count()
            # Assuming Oware rules prefer seeds > 1
            if seeds > 1:
                actions.append(i)
            elif seeds == 1:
                singles.append(i)

        return actions if actions else singles

    def __str__(self) -> str:
        """Return string representation of the Player."""
        return f"Player(num={self.num}, houses={self.houses}, store={self.store})"
