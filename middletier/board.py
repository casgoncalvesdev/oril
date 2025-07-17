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
from typing import List

from middletier.house import House
from middletier.player import Player
from middletier.player_number import PlayerNumber
from middletier.players import Players
from middletier.store import Store


class Board:
    def __init__(self):
        self.houses: List[House] = []
        self.stores: List[Store] = []
        self.players: Players = None

    @staticmethod
    def create(number_of_seeds: int = 4, length: int = 6) -> 'Board':
        seeds = [number_of_seeds] * length
        return Board.from_seeds(seeds, 0, seeds, 0)

    @staticmethod
    def from_seeds(p1_seeds: List[int], p1_store: int,
                   p2_seeds: List[int], p2_store: int) -> 'Board':
        houses_one = Board.build_houses(PlayerNumber.ONE, p1_seeds)
        houses_two = Board.build_houses(PlayerNumber.TWO, p2_seeds)

        store_one = Store(PlayerNumber.ONE, p1_store)
        store_two = Store(PlayerNumber.TWO, p2_store)

        Board.circular(houses_one, store_one, houses_two, store_two)

        player_one = Player(PlayerNumber.ONE, houses_one, store_one)
        player_two = Player(PlayerNumber.TWO, houses_two, store_two)

        board = Board()
        board.houses = houses_one + houses_two
        board.stores = [store_one, store_two]
        board.players = Players(player_one, player_two)
        return board

    @staticmethod
    def build_houses(player_number: 'player_number.py', seeds: List[int]) -> List['House']:
        houses = []
        for seed_count in seeds:
            house = House(player_number, seed_count)
            if houses:
                houses[-1].set_next(house)
                house.set_previous(houses[-1])
            houses.append(house)
        return houses

    @staticmethod
    def circular(houses_one: List['House'], store_one: 'Store',
                 houses_two: List['House'], store_two: 'Store') -> None:
        houses_one[-1].set_next(store_one)
        store_one.set_next(houses_two[0])
        houses_two[-1].set_next(store_two)
        store_two.set_next(houses_one[0])

    def get_houses(self):
        return self.houses

    def get_stores(self):
        return self.stores

    def get_players(self):
        return self.players

    def __str__(self) -> str:
        return f"Board(houses={self.houses}, stores={self.stores}, players={self.players})"
