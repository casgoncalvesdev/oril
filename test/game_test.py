"""
    Main script:
    Sets up and runs test scenarios for the seed-sowing game, demonstrating different board
    states and game outcomes. This script initializes the board with various seed configurations
    to test capturing mechanics and game termination conditions.

    Key responsibilities:
    - Create custom boards with specific seed distributions for testing.
    - Display the initial board state using the Print utility.
    - Create a Game instance based on the board and execute gameplay with turn-by-turn display.
    - Support multiple sequential playthroughs for demonstration.

    Usage notes:
    - Multiple test scenarios are provided as commented blocks; uncomment to switch scenarios.
    - The default scenario tests capture of 2 seeds from an opposite pit.
    - The script runs a text-based interactive display of the game in the console.

    Dependencies:
    - Print: Frontend utility for displaying board and game state.
    - Board: Core board representation and factory methods.
    - Game: Game logic, player turns, and status management.
"""
from frontend.print import Print

from middletier.board import Board
from middletier.game import Game


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
    # board = Board.from_seeds(
    #     [0, 0, 0, 0, 4, 0],
    #     20,
    #     [1, 0, 1, 0, 0, 0],
    #     22
    # )

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

    board = Board.create()

    print(Print.board(board))

    game = Game.create(board)
    Print.play(game)

    Print.play(game)


if __name__ == "__main__":
    main()