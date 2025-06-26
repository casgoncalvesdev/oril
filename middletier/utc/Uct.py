import time
import random

from middletier.PlayerNumber import PlayerNumber
from middletier.utc.UctNode import UctNode
from copy import deepcopy

class Uct:
    def __init__(self):
        pass

    def get_action_info(self, player, board, max_iterations, max_time, max_depth_simulation, max_lookahead):
        result = None
        root = UctNode(player=player, parent=None, board=board, action=None)

        if len(root.unexamined) > 1:
            start_time = time.time()
            time_limit = start_time + (max_time / 1000.0)  # convert ms to seconds
            block_size = 50
            nodes_visited = 0

            iterations = 0
            while iterations < max_iterations and time.time() < time_limit:
                for _ in range(block_size):
                    node = root
                    variant_board = deepcopy(board)
                    players = variant_board.get_players()
                    player = players.get_player1() if player.get_num() == PlayerNumber.ONE else players.get_player2()
                    lookahead = max_lookahead

                    # Selection
                    while node.unexamined == [] and node.children and lookahead > 0:
                        node = node.select_child()
                        player.turn(node.action + 1)
                        players = variant_board.get_players()
                        player = players.get_player1() if player.get_num() == PlayerNumber.ONE else players.get_player2()
                        lookahead -= 1

                    # Expansion
                    if node.unexamined:
                        action = random.choice(node.unexamined)
                        player.turn(action + 1)
                        node = node.add_child(player, variant_board, node.unexamined.index(action))
                        players = variant_board.get_players()
                        player = players.get_player1() if player.get_num() == PlayerNumber.ONE else players.get_player2()

                    # Simulation
                    players = variant_board.get_players()
                    player = players.get_player1() if player.get_num() == PlayerNumber.ONE else players.get_player2()
                    actions = player.get_actions()
                    depth = max_depth_simulation
                    while len(actions) > 0 and depth > 0 and lookahead > 0:
                        move = random.choice(player.get_actions())
                        player.turn(move + 1, True)
                        nodes_visited += 1
                        players = variant_board.get_players()
                        player = players.get_player1() if player.get_num() == PlayerNumber.ONE else players.get_player2()
                        actions = player.get_actions()
                        depth -= 1
                        lookahead -= 1

                    # Backpropagation
                    result = {
                        PlayerNumber.ONE: variant_board.get_players().get_player1().score(),
                        PlayerNumber.TWO: variant_board.get_players().get_player2().score()
                    }

                iterations += block_size

            duration = time.time() - start_time
            speed = int(nodes_visited / duration)
            best_child = root.most_visited_child()
            result = {
                "action": best_child.action,
                "info": f"{speed} nodes/sec examined."
            }

        elif len(root.unexamined) == 1:
            result = {
                "action": root.unexamined[0],
                "info": "Just 1 action available."
            }
        else:
            result = {
                "action": None,
                "info": "No action available."
            }

        return result