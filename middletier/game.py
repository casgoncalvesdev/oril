"""
    Game class:
    This class manages the flow and state of a two-player board game.
    It coordinates player turns, handles move execution, checks for game completion,
    determines the winner, and allows moves either interactively or via an AI-based
    UCT (Upper Confidence bound applied to Trees) strategy for Player Two.
    The class uses several supporting modules:
    - Board: Represents the game board and its state.
    - Player: Encapsulates player actions and scoring.
    - PlayerNumber: Enum for identifying Player One or Two.
    - Result: Wraps the result of a move, including game status and active player.
    - Status: Enum representing the game's current status (active, won, draw).
    - Uct: (Optional) Implements UCT logic from Monte Carlo Tree Search for AI moves.
"""

from middletier.board import Board
from middletier.player import Player
from middletier.player_number import PlayerNumber
from middletier.result import Result
from middletier.status import Status
from middletier.uct.uct import Uct


class Game:
    def __init__(self):
        """
            Initializes an empty Game instance.
            Use the `create()` method to properly initialize the game with a board.
        """
        self.board: Board = None
        self.player: Player = None
        self.status: Status = None

    @staticmethod
    def create(board: 'Board') -> 'Game':
        """
            Creates and returns a new Game with the given board and Player One starting.

            Args:
                board (Board): The initialized game board.

            Returns:
                Game: A new game instance with players and status initialized.
        """
        game = Game()
        game.board = board
        game.player = board.get_players().get_player1()
        game.status = Status.ACTIVE
        return game

    def move(self, num: 'PlayerNumber', house: int = None) -> 'Result':
        """
           Executes a move for the given player.

           If no house is provided, prompts the user (Player One) for input or selects a move
           using UCT strategy (Player Two). Updates game state, switches active player, and
           checks for end-game conditions.

           Args:
               num (PlayerNumber): The number of the player making the move.
               house (int, optional): The index of the house to play (1-based).
               If None, defaults to interactive or AI move.

           Returns:
               Result: The result of the move, including updated board and game status.

           Raises:
               ValueError: If the wrong player tries to move or input is invalid.
       """
        if self.player.get_num() != num:
            raise ValueError(f"Player {num} cannot take their turn yet")

        # Interactive input only if house not provided (fallback)
        if house is None:
            if num == PlayerNumber.ONE:
                try:
                    house = int(input("Wähle eine Grube: "))
                except ValueError as exc:
                    raise ValueError("Invalid input. Please enter a number.") from exc
            else:
                # # RandomRollout Simulation
                # house = random.randint(1, 5)

                ##  UCT (Upper Confidence bound applied to Trees) from Monte Carlo Tree Search (MCTS)
                uct = Uct()
                action_info = uct.get_action_info(self.player, self.board, 300000, 5000, 50, 70)
                house = action_info.get('action') + 1

        self.player.turn(house)

        if self.player.complete():
            self.other_player().finish()
            self.status = self._declare_winner()

        self.player = self.other_player()

        return Result(self.status, self.player.get_num(), self.board)

    def _declare_winner(self) -> 'Status':
        """
            Determines the winner by comparing player scores.

            Returns:
                Status: The final game status — win for Player One, Player Two, or a draw.
        """
        players = self.board.get_players()
        score1 = players.get_player1().score()
        score2 = players.get_player2().score()

        if score1 > score2:
            return Status.PLAYER_ONE_WIN
        if score2 > score1:
            return Status.PLAYER_TWO_WIN
        return Status.DRAW

    def other_player(self) -> 'Player':
        """
            Returns the opponent of the currently active player.

            Returns:
                Player: The other player.
        """
        players = self.board.get_players()
        if self.player.get_num() == PlayerNumber.ONE:
            return players.get_player2()
        return players.get_player1()

    def get_active_player(self) -> 'Player':
        """
            Gets the currently active player.

            Returns:
                Player: The player whose turn it is.
        """
        return self.player

    def __str__(self) -> str:
        """
            Returns a string representation of the current game state.

            Returns:
                str: The string describing the game.
        """
        return f"Game(board={self.board}, player={self.player}, status={self.status})"
