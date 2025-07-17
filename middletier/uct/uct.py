"""
    Uct class:
    Implements the Upper Confidence bound applied to Trees (UCT) algorithm,
    a key component of Monte Carlo Tree Search (MCTS) used to select optimal moves
    in the game by balancing exploration and exploitation during simulations.

    Key responsibilities include:
    - Performing tree search with selection, expansion, simulation, and backpropagation phases.
    - Managing search parameters such as maximum iterations, time, simulation depth, and lookahead.
    - Returning the best action found along with performance metrics.

    Dependencies:
    - PlayerNumber: Enum to identify players.
    - UctNode: Represents nodes in the search tree.
    - deepcopy: Used to simulate moves on independent board copies.

    Usage notes:
    - The main method get_action_info runs iterative simulations until
      constraints on time or iterations are met, then returns the best move.
"""

import time
import random

from copy import deepcopy
from middletier.player_number import PlayerNumber
from middletier.uct.uct_node import UctNode


class Uct:
    def __init__(self):
        pass

    def get_action_info(
        self,
        player,
        board,
        max_iterations,
        max_time,
        max_depth_simulation,
        max_lookahead
    ):
        def get_current_player(variant_board, current_player):
            players = variant_board.get_players()
            if current_player.get_num() == PlayerNumber.ONE:
                return players.get_player1()
            return players.get_player2()

        # Create the root node for UCT with the current game state
        root = UctNode(player=player, parent=None, action=None)
        result = None

        if len(root.unexamined) > 1:
            start_time = time.time()
            time_limit = start_time + (max_time / 1000.0)
            block_size = 50
            nodes_visited = 0
            iterations = 0

            while iterations < max_iterations and time.time() < time_limit:
                for _ in range(block_size):
                    node = root
                    variant_board = deepcopy(board)
                    current_player = get_current_player(variant_board, player)
                    lookahead = max_lookahead

                    # Selection: traverse down tree to leaf node
                    while not node.unexamined and node.children and lookahead > 0:
                        node = node.select_child()
                        current_player.turn(node.action + 1)
                        current_player = get_current_player(variant_board, current_player)
                        lookahead -= 1

                    # Expansion: expand new child if unexamined actions exist
                    if node.unexamined:
                        action = random.choice(node.unexamined)
                        current_player.turn(action + 1)
                        child_index = node.unexamined.index(action)
                        node = node.add_child(current_player, child_index)
                        current_player = get_current_player(variant_board, current_player)

                    # Simulation: run rollout from this node
                    current_player = get_current_player(variant_board, current_player)
                    actions = current_player.get_actions()
                    depth = max_depth_simulation

                    while actions and depth > 0 and lookahead > 0:
                        move = random.choice(actions)
                        current_player.turn(move + 1, sim=True)
                        nodes_visited += 1
                        current_player = get_current_player(variant_board, current_player)
                        actions = current_player.get_actions()
                        depth -= 1
                        lookahead -= 1

                    # Backpropagation: update node statistics based on simulation result
                    result = {
                        PlayerNumber.ONE: variant_board.get_players().get_player1().score(),
                        PlayerNumber.TWO: variant_board.get_players().get_player2().score()
                    }

                iterations += block_size

            duration = time.time() - start_time
            speed = int(nodes_visited / duration) if duration > 0 else 0
            best_child = root.most_visited_child()
            result = {
                "action": best_child.action,
                "info": f"{speed} nodes/sec examined."
            }

        elif len(root.unexamined) == 1:
            # Only one action possible
            result = {
                "action": root.unexamined[0],
                "info": "Just 1 action available."
            }
        else:
            # No moves available (probably game over)
            result = {
                "action": None,
                "info": "No action available."
            }

        return result
