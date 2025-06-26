from middletier.Board import Board
from middletier.PlayerNumber import PlayerNumber


class Print:
    TEMPLATE = """
                       Player Two        
             | {:02d} | {:02d} | {:02d} | {:02d} | {:02d} | {:02d} |
        ({:02d})                                 ({:02d})
             | {:02d} | {:02d} | {:02d} | {:02d} | {:02d} | {:02d} |
                       Player One
    """

    @staticmethod
    def board(board: 'Board') -> str:
        player1 = board.get_players().get_player1()
        player2 = board.get_players().get_player2()

        p2_rev = list(reversed(player2.get_houses()))

        pits = p2_rev + [player2.get_store(), player1.get_store()] + player1.get_houses()
        counts = [pit.count() for pit in pits]

        return Print.TEMPLATE.format(*counts)

    @staticmethod
    def initial_board():
        board = Board.create()
        print(Print.board(board))

    @staticmethod
    def play(game: 'Game'):
        turn = False
        while not game.get_active_player().complete():
            if turn:
                view = Print.get_view(game, PlayerNumber.TWO)
            else:
                view = Print.get_view(game, PlayerNumber.ONE)
            print(view)
            turn = not turn

    @staticmethod
    def get_view(game: 'Game', num: 'PlayerNumber') -> str:
        result = game.move(num)
        print("Status:", result.get_status())
        return Print.board(result.get_board())
