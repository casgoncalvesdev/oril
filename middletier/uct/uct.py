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
            max_lookahead):
        """
            Runs a UCT (Upper Confidence Trees) search to select the best action from the current game state.

            The method performs a Monte Carlo Tree Search (MCTS) using the UCT algorithm. It repeatedly
            selects, expands, simulates, and backpropagates game states to evaluate available actions
            from the root node (current board state). The process stops when the time or iteration
            limit is reached, and the most visited child node's action is returned.

            Args:
                player (Player): The player whose turn it is to act.
                board (Board): The current board state.
                max_iterations (int): The maximum number of iterations to perform.
                max_time (int): Maximum time (in milliseconds) allowed for the search.
                max_depth_simulation (int): Maximum depth to simulate during rollouts.
                max_lookahead (int): Number of game steps to look ahead in tree traversal.

            Returns:
                dict: A dictionary with the selected action and additional info:
                    {
                        "action": int or None,  # the selected action index (0-based), or None if no action
                        "info": str             # description of the decision context or performance stats
                    }

            Notes:
                - If only one unexamined action exists, it's selected without running MCTS.
                - If no actions are available, the result will contain `None` for the action.
        """
        result = None

        # Create the root node for UCT with the current game state
        root = UctNode(player=player, parent=None, action=None)

        if len(root.unexamined) > 1:
            start_time = time.time()
            # convert ms to seconds
            # Convert ms to seconds
            time_limit = start_time + (max_time / 1000.0)
            block_size = 50  # Number of simulations per batch
            nodes_visited = 0
            iterations = 0

            # Main UCT loop
            while iterations < max_iterations and time.time() < time_limit:
                for _ in range(block_size):
                    node = root
                    # Copy the board for simulation
                    variant_board = deepcopy(board)
                    players = variant_board.get_players()
                    player = players.get_player1() if player.get_num(
                    ) == PlayerNumber.ONE else players.get_player2()
                    lookahead = max_lookahead

                    # Selection
                    # Traverse tree down to a leaf node using best UCT children
                    while node.unexamined == [] and node.children and lookahead > 0:
                        node = node.select_child()
                        player.turn(node.action + 1)
                        players = variant_board.get_players()
                        player = players.get_player1() if player.get_num(
                        ) == PlayerNumber.ONE else players.get_player2()
                        lookahead -= 1

                    # Expansion
                    # Expand a new child from the unexamined actions
                    if node.unexamined:
                        action = random.choice(node.unexamined)
                        player.turn(action + 1)
                        node = node.add_child(
                            player, variant_board, node.unexamined.index(action))
                        players = variant_board.get_players()
                        player = players.get_player1() if player.get_num(
                        ) == PlayerNumber.ONE else players.get_player2()

                    # Simulation
                    # Run a random simulation from this new node
                    players = variant_board.get_players()
                    player = players.get_player1() if player.get_num(
                    ) == PlayerNumber.ONE else players.get_player2()
                    actions = player.get_actions()
                    depth = max_depth_simulation
                    while len(actions) > 0 and depth > 0 and lookahead > 0:
                        move = random.choice(player.get_actions())
                        player.turn(move + 1, True)
                        nodes_visited += 1
                        players = variant_board.get_players()
                        player = players.get_player1() if player.get_num(
                        ) == PlayerNumber.ONE else players.get_player2()
                        actions = player.get_actions()
                        depth -= 1
                        lookahead -= 1

                    # Backpropagation
                    # Use the result of simulation to update node statistics
                    result = {
                        PlayerNumber.ONE: variant_board.get_players().get_player1().score(),
                        PlayerNumber.TWO: variant_board.get_players().get_player2().score()}

                iterations += block_size

            # Select the best child node (most visited) as the final decision
            duration = time.time() - start_time
            speed = int(nodes_visited / duration)
            best_child = root.most_visited_child()
            result = {
                "action": best_child.action,
                "info": f"{speed} nodes/sec examined."
            }

        elif len(root.unexamined) == 1:
            # Only one move available — return it immediately
            result = {
                "action": root.unexamined[0],
                "info": "Just 1 action available."
            }
        else:
            # No moves available — probably game over
            result = {
                "action": None,
                "info": "No action available."
            }

        return result
