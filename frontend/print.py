"""
    Print class:
    Provides utility methods for displaying the game board and gameplay progress
    in a human-readable format on the console.

    Key responsibilities include:
    - Rendering the current board state in a formatted text layout.
    - Displaying an initial empty or default board.
    - Facilitating a simple looped play display alternating between players.
    - Generating board views after moves for each player.

    Dependencies:
    - Board: Represents the game board with pits and stores.
    - PlayerNumber: Enum to identify players (Player One or Player Two).

    Usage notes:
    - The board layout aligns pits visually with Player Two’s houses reversed at the top,
      stores in the middle, and Player One’s houses at the bottom.
    - The play method alternates turns and displays the game until a player completes their moves.
"""
from middletier.board import Board
from middletier.game import Game
from middletier.player_number import PlayerNumber


class Print:
    # A string template to format the game board
    TEMPLATE = """
                       Player Two
             | {:02d} | {:02d} | {:02d} | {:02d} | {:02d} | {:02d} |
        ({:02d})                                 ({:02d})
             | {:02d} | {:02d} | {:02d} | {:02d} | {:02d} | {:02d} |
                       Player One
    """

    @staticmethod
    def board(board: 'Board') -> str:
        """Generates a string representation of the current board.

        Args:
            board (Board): The board object containing the players' data and pits.

        Returns:
            str: A formatted string representing the current game board with pit counts.
        """
        # Retrieve player 1 and player 2 objects
        player1 = board.get_players().get_player1()
        player2 = board.get_players().get_player2()

        # Reverse the list of houses for player 2 (to match board layout)
        p2_rev = list(reversed(player2.get_houses()))

        # Concatenate the pits: Player 2 houses, Player 2 store, Player 1
        # store, Player 1 houses.
        pits = p2_rev + [player2.get_store(),
                         player1.get_store()] + player1.get_houses()

        # Collect the count of each pit
        counts = [pit.count() for pit in pits]

        # Return the formatted board as a string
        return Print.TEMPLATE.format(*counts)

    @staticmethod
    def initial_board():
        """Prints the initial board setup for a new game."""
        # Create the board and print the initial game view
        board = Board.create()
        print(Print.board(board))

    @staticmethod
    def play(game: 'Game'):
        """Handles the main game loop, alternating between two players.

        Args:
            game (Game): The game object that controls the flow of the game.
        """
        turn = False  # Player One starts (False = Player One, True = Player Two)

        # Continue the game until the active player has completed their turn
        while not game.get_active_player().complete():
            # Print the game view based on the current player
            if turn:
                view = Print.get_view(game, PlayerNumber.TWO)
            else:
                view = Print.get_view(game, PlayerNumber.ONE)
            print(view)
            # Switch turn
            turn = not turn

    @staticmethod
    def get_view(game: 'Game', num: 'PlayerNumber') -> str:
        """Gets the current view of the game for a specific player.

        Args:
            game (Game): The game object.
            num (PlayerNumber): The player number to get the view for.

        Returns:
            str: A string representing the current board and player status.
        """
        # Get the result of the move for the current player
        result = game.move(num)

        # Print the status of the move (e.g., whether it was successful or not)
        print("Status:", result.get_status())

        # Return the board state after the move
        return Print.board(result.get_board())
