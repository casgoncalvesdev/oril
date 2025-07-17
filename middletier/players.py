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
class Players:
    def __init__(self, player1: 'Player', player2: 'Player'):
        """Initialize Players with two Player instances."""
        self.player1 = player1
        self.player2 = player2

    def get_player1(self) -> 'Player':
        """Return the first player."""
        return self.player1

    def get_player2(self) -> 'Player':
        """Return the second player."""
        return self.player2

    def __eq__(self, other) -> bool:
        """
        Check equality with another Players instance.

        Args:
            other: The object to compare against.

        Returns:
            True if both players are equal, False otherwise.
        """
        if not isinstance(other, Players):
            return False
        return self.player1 == other.player1 and self.player2 == other.player2

    def __hash__(self) -> int:
        """Return a hash based on the two players."""
        return hash((self.player1, self.player2))

    def __str__(self) -> str:
        """Return a string representation of the Players instance."""
        return f"Players(player1={self.player1}, player2={self.player2})"
