from frontend.Print import Print
from middletier.Board import Board
from middletier.Game import Game


def main():
    # # Test scenario: capture 2 seeds from opposite pit
    # board = Board.from_seeds(
    #     [0, 0, 0, 0, 2, 0],
    #     22,
    #     [1, 0, 0, 0, 0, 0],
    #     23
    # )

    # # Test scenario: capture seeds from tow consecutive pits
    # board = Board.from_seeds(
    #     [0, 0, 0, 0, 3, 0],
    #     21,
    #     [1, 1, 0, 0, 0, 0],
    #     21
    # )

    # # Test scenario: capture seeds from none consecutive pits
    board = Board.from_seeds(
        [0, 0, 0, 0, 4, 0],
        20,
        [1, 0, 1, 0, 0, 0],
        22
    )

    # # Test scenario: capture seeds from 2 pits partially none consecutive
    # board = Board.from_seeds(
    #     [0, 0, 0, 0, 5, 0],
    #     19,
    #     [1, 0, 1, 1, 0, 0],
    #     21
    # )

    # # Test scenario: capture seeds from one loop of 12 seeds
    # board = Board.from_seeds(
    #     [0, 0, 0, 0, 0, 12],
    #     18,
    #     [0, 0, 0, 0, 0, 0],
    #     18
    # )

    # # Test scenario: terminate game with player one as winner
    # board = Board.from_seeds(
    #     [0, 0, 0, 0, 0, 1],
    #     23,
    #     [1, 0, 0, 0, 0, 0],
    #     23
    # )

    # # Test scenario: terminate game with a draw
    # board = Board.from_seeds(
    #     [0, 0, 0, 0, 0, 1],
    #     22,
    #     [1, 0, 0, 0, 0, 0],
    #     24
    # )

    print(Print.board(board))

    game = Game.create(board)
    Print.play(game)

    Print.play(game)


if __name__ == "__main__":
    main()