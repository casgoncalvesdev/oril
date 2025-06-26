from frontend.Print import Print
from middletier.Board import Board


def main():
    board = Board.create()
    view = Print.board(board)
    print(view)

if __name__ == "__main__":
    main()