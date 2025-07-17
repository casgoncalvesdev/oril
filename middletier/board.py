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
        """
           Initializes an empty Board. Use `Board.create()` or `Board.from_seeds()` to populate it.
        """
        self.houses: List[House] = []
        self.stores: List[Store] = []
        self.players: Players = None

    @staticmethod
    def create(number_of_seeds: int = 4, length: int = 6) -> 'Board':
        """
            Creates a new board with a given number of seeds per house and number of houses.

            Args:
                number_of_seeds (int): Seeds per house (default 4).
                length (int): Number of houses per player (default 6).

            Returns:
                Board: A fully initialized Board instance.
        """
        seeds = [number_of_seeds] * length
        return Board.from_seeds(seeds, 0, seeds, 0)

    @staticmethod
    def from_seeds(p1_seeds: List[int], p1_store: int,
                   p2_seeds: List[int], p2_store: int) -> 'Board':
        """
            Creates a Board from explicit seed counts for both players.

            Args:
                p1_seeds (List[int]): Seeds in Player 1's houses.
                p1_store (int): Seeds in Player 1's store.
                p2_seeds (List[int]): Seeds in Player 2's houses.
                p2_store (int): Seeds in Player 2's store.

            Returns:
                Board: A Board initialized with the specified seed configuration.
        """
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
        """
            Builds a list of House instances for a player, linking them sequentially.

            Args:
                player_number (PlayerNumber): The player's identifier.
                seeds (List[int]): Seed counts for each house.

            Returns:
                List[House]: A list of linked House objects.
        """
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
        """
           Links all pits (houses and stores) in a circular manner.

           Args:
               houses_one (List[House]): Player 1's houses.
               store_one (Store): Player 1's store.
               houses_two (List[House]): Player 2's houses.
               store_two (Store): Player 2's store.
       """
        houses_one[-1].set_next(store_one)
        store_one.set_next(houses_two[0])
        houses_two[-1].set_next(store_two)
        store_two.set_next(houses_one[0])

    def get_houses(self):
        """
            Returns all house pits on the board.

            Returns:
                List[House]: List of all House objects.
        """
        return self.houses

    def get_stores(self):
        """
            Returns the store pits for both players.

            Returns:
                List[Store]: List containing both players' stores.
        """
        return self.stores

    def get_players(self):
        """
           Returns the Players object managing both players.

           Returns:
               Players: The game players.
       """
        return self.players

    def __str__(self) -> str:
        """
            Returns a string representation of the board.

            Returns:
                str: String describing the current board state.
        """
        return f"Board(houses={self.houses}, stores={self.stores}, players={self.players})"
