"""
    Main script:
    Initializes a default game board using the Board factory method,
    then prints the initial board layout to the console using the Print utility.

    This script serves as a simple entry point to visualize the starting state
    of the game without any player interaction or moves.

    Dependencies:
    - Board: For creating the game board with default settings.
    - Print: For rendering the board state in a human-readable format.
"""
from frontend.print import Print
from middletier.board import Board


def main():
    board = Board.create()
    view = Print.board(board)
    print(view)

if __name__ == "__main__":
    main()