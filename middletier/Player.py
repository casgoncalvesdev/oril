"""

"""
class Player:
    def __init__(self, num: 'PlayerNumber', houses: list['House'], store: 'Store'):
        self.num = num
        self.houses = houses
        self.store = store

    def get_num(self) -> 'PlayerNumber':
        return self.num

    def get_houses(self) -> list['House']:
        return self.houses

    def get_store(self) -> 'Store':
        return self.store

    def turn(self, house_num: int) -> 'Pit':
        house = self._get_house(house_num)
        self._check_has_seeds(house)
        pit = self._take_turn(house)

        while self._should_capture(house, pit):
            self.store.sow(pit.take())
            pit = pit.get_previous()

        return pit

    def complete(self) -> bool:
        return all(house.is_empty() for house in self.houses)

    def finish(self) -> None:
        for house in self.houses:
            self.store.sow(house.take())

    def score(self) -> int:
        return self.store.count()

    def _should_capture(self, house: 'House', pit: 'Pit') -> bool:
        return (pit is not None and
                house.owner != pit.owner and
                pit.count() in (2, 3))

    def _check_has_seeds(self, house: 'House') -> None:
        if house.is_empty():
            raise ValueError("House must have seeds to take turn")

    def _take_turn(self, house: 'House') -> 'Pit':
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
        if house_num < 1 or house_num > len(self.houses):
            raise ValueError(f"House number must be between 1 and {len(self.houses)}")
        return self.houses[house_num - 1]

    def __str__(self) -> str:
        return f"Player(num={self.num}, houses={self.houses}, store={self.store})"
