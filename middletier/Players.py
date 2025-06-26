class Players:
    def __init__(self, player1: 'Player', player2: 'Player'):
        self.player1 = player1
        self.player2 = player2

    def get_player1(self) -> 'Player':
        return self.player1

    def get_player2(self) -> 'Player':
        return self.player2

    def __eq__(self, other) -> bool:
        if not isinstance(other, Players):
            return False
        return self.player1 == other.player1 and self.player2 == other.player2

    def __hash__(self) -> int:
        return hash((self.player1, self.player2))

    def __str__(self) -> str:
        return f"Players(player1={self.player1}, player2={self.player2})"
