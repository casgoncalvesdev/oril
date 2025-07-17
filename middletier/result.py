"""
    Result class:
    This class encapsulates the outcome of a single move in the game, including the game status,
    which player's turn is next, and the current state of the board. It also provides utilities
    to retrieve scores and compare result states.

    Key responsibilities include:
    - Holding the result state after a move: game status, next player, and board.
    - Providing access to player scores via `get_result()`.
    - Supporting comparison and hashing for result objects (useful for testing or AI logic).

    Dependencies:
    - PlayerNumber: Enum identifying players.
    - Status: Enum representing game state (e.g., ACTIVE, WIN, DRAW).
    - Board: Represents the current layout and state of the game.
"""
from middletier.player_number import PlayerNumber

class Result:
    def __init__(self, status: 'Status', next_player: 'PlayerNumber', board: 'Board'):
        """Initialize a Result instance with game status, next player, and board state."""
        self.status = status
        self.next = next_player
        self.board = board

    def get_status(self) -> 'Status':
        """Return the current status of the game."""
        return self.status

    def get_next(self) -> 'PlayerNumber':
        """Return the next player to move."""
        return self.next

    def get_board(self) -> 'Board':
        """Return the current game board."""
        return self.board

    def get_result(self):
        """
        Compute and return the scores of both players.

        Returns:
            dict: Mapping of PlayerNumber to their respective scores.
        """
        p1_score = self.board.get_players().get_player1().score()
        p2_score = self.board.get_players().get_player2().score()
        return {PlayerNumber.ONE: p1_score, PlayerNumber.TWO: p2_score}

    def __eq__(self, other) -> bool:
        """
        Compare two Result instances for equality.

        Args:
            other (Result): The other Result instance to compare.

        Returns:
            bool: True if all attributes match, False otherwise.
        """
        if not isinstance(other, Result):
            return False
        return (
            self.status == other.status and
            self.next == other.next and
            self.board == other.board
        )

    def __hash__(self) -> int:
        """Return a hash based on the status, next player, and board."""
        return hash((self.status, self.next, self.board))

    def __str__(self) -> str:
        """Return a string representation of the Result."""
        return f"Result(status={self.status}, next={self.next}, board={self.board})"
