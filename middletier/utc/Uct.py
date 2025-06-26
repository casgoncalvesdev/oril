import time
import random
from middletier.utc.UctNode import UctNode

class Uct:
    def __init__(self):
        pass

    def get_action_info(self, board, max_iterations, max_time, max_depth_simulation, max_lookahead):
        result = None
        root = UctNode(parent=None, board=board, action=None)

        if len(root.unexamined) > 1:
            start_time = time.time()
            time_limit = start_time + (max_time / 1000.0)  # convert ms to seconds
            block_size = 50
            nodes_visited = 0

            iterations = 0
            while iterations < max_iterations and time.time() < time_limit:
                for _ in range(block_size):
                    node = root
                    variant_board = board.copy()
                    lookahead = max_lookahead

                    # Selection
                    while not node.unexamined and node.children and lookahead > 0:
                        node = node.select_child()
                        variant_board.do_action(node.action)
                        lookahead -= 1

                    # Expansion
                    if node.unexamined:
                        j = random.randrange(len(node.unexamined))
                        action = node.unexamined[j]
                        variant_board.do_action(action)
                        node = node.add_child(variant_board, j)

                    # Simulation
                    actions = variant_board.get_actions()
                    depth = max_depth_simulation
                    while actions and depth > 0 and lookahead > 0:
                        action = random.choice(actions)
                        variant_board.do_action(action)
                        nodes_visited += 1
                        actions = variant_board.get_actions()
                        depth -= 1
                        lookahead -= 1

                    # Backpropagation
                    simulation_result = variant_board.get_result()
                    while node:
                        node.update(simulation_result)
                        node = node.parent

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