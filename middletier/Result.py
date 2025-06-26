class Result:
    def __init__(self, status: 'Status', next_player: 'PlayerNumber', board: 'Board'):
        self.status = status
        self.next = next_player
        self.board = board

    def get_status(self) -> 'Status':
        return self.status

    def get_next(self) -> 'PlayerNumber':
        return self.next

    def get_board(self) -> 'Board':
        return self.board

    def __eq__(self, other) -> bool:
        if not isinstance(other, Result):
            return False
        return (
            self.status == other.status and
            self.next == other.next and
            self.board == other.board
        )

    def __hash__(self) -> int:
        return hash((self.status, self.next, self.board))

    def __str__(self) -> str:
        return f"Result(status={self.status}, next={self.next}, board={self.board})"
