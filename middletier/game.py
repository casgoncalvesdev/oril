"""
    Game class:
    This class manages the flow and state of a two-player board game.
    It coordinates player turns, handles move execution, checks for game completion,
    and determines the winner. The class uses several supporting modules:
    - Board: Represents the game board and its state.
    - Player: Encapsulates player actions and scoring.
    - PlayerNumber: Enum for identifying Player One or Two.
    - Result: Wraps the result of a move, including game status and active player.
    - Status: Enum representing the game's current status (active, won, draw).
    - Uct: (Optional) Implements UCT logic from Monte Carlo Tree Search for AI moves.
"""

import random

from middletier.board import Board
from middletier.player import Player
from middletier.player_number import PlayerNumber
from middletier.result import Result
from middletier.status import Status
from middletier.uct.uct import Uct


class Game:
    def __init__(self):
        self.board: Board = None
        self.player: Player = None
        self.status: Status = None

    @staticmethod
    def create(board: 'Board') -> 'Game':
        game = Game()
        game.board = board
        game.player = board.get_players().get_player1()
        game.status = Status.ACTIVE
        return game

    def move(self, num: 'PlayerNumber', house: int = None) -> 'Result':
        if self.player.get_num() != num:
            raise ValueError(f"Player {num} cannot take their turn yet")

        # Interactive input only if house not provided (fallback)
        if house is None:
            if num == PlayerNumber.ONE:
                try:
                    house = int(input("Wähle eine Grube: "))
                except ValueError:
                    raise ValueError("Invalid input. Please enter a number.")
            else:
                # # RandomRollout Simulation
                #house = random.randint(1, 5)

                ##  UCT (Upper Confidence bound applied to Trees) from Monte Carlo Tree Search (MCTS)
                uct = Uct()
                actionInfo = uct.get_action_info(self.player, self.board, 300000, 5000, 50, 70)
                house = actionInfo.get('action') + 1

        landed = self.player.turn(house)

        if self.player.complete():
            self.other_player().finish()
            self.status = self._declare_winner()

        self.player = self.other_player()

        return Result(self.status, self.player.get_num(), self.board)

    def _declare_winner(self) -> 'Status':
        players = self.board.get_players()
        score1 = players.get_player1().score()
        score2 = players.get_player2().score()

        if score1 > score2:
            return Status.PLAYER_ONE_WIN
        elif score2 > score1:
            return Status.PLAYER_TWO_WIN
        else:
            return Status.DRAW

    def other_player(self) -> 'Player':
        players = self.board.get_players()
        if self.player.get_num() == PlayerNumber.ONE:
            return players.get_player2()
        else:
            return players.get_player1()

    def get_active_player(self) -> 'Player':
        return self.player

    def __str__(self) -> str:
        return f"Game(board={self.board}, player={self.player}, status={self.status})"