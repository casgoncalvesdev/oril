"""
    UctNode class:
    Represents a node in the Monte Carlo Tree Search (MCTS) tree used by the UCT algorithm.
    Each node corresponds to a game state resulting from an action taken by a player.

    Key responsibilities include:
    - Tracking visits and cumulative wins for computing UCT values.
    - Managing children nodes and the list of unexplored actions.
    - Selecting child nodes based on the UCT formula to balance exploration and exploitation.
    - Adding new child nodes during the expansion phase.
    - Updating node statistics during backpropagation.
    - Providing the most visited child, typically used to choose the best move after simulations.

    Attributes:
    - action: The move that led to this node.
    - parent: Reference to the parent UctNode.
    - children: List of child UctNodes.
    - wins: Accumulated score for the active player at this node.
    - visits: Number of times this node has been visited.
    - active_player: The player who is to move at this node.
    - unexamined: Actions from this state yet to be tried.

    Dependencies:
    - math: For logarithm and square root calculations.

    Usage notes:
    - select_child implements the UCT formula.
    - add_child removes the chosen action from unexamined and appends the new child.
    - update increments visit count and updates wins based on simulation results.
"""

import math
import random

class UctNode:
    def __init__(self, player, parent, board, action):
        self.verbose = False
        self.action = action                   # Action that led to this node
        self.parent = parent                   # Parent UctNode
        self.children = []                     # Child UctNodes
        self.wins = 0                          # Total score (for active player)
        self.visits = 0                        # Number of times node visited
        self.active_player = player.get_num()  # Actions not yet tried
        self.unexamined = player.get_actions() # Who is to move

    def add_child(self, player, board, index):
        action = self.unexamined[index]
        child = UctNode(player=player, parent=self, board=board, action=action)
        del self.unexamined[index]
        self.children.append(child)
        return child

    def select_child(self):
        best_value = float('-inf')
        selected = None

        for child in self.children:
            if child.visits == 0:
                # Fallback: prefer exploring unvisited child first
                return child
            uct_value = (child.wins / child.visits) + \
                        math.sqrt(2 * math.log(self.visits) / child.visits)
            if uct_value > best_value:
                best_value = uct_value
                selected = child

        return selected

    def update(self, result):
        self.visits += 1
        self.wins += result[self.active_player]

    def most_visited_child(self):
        if self.verbose:
            for child in self.children:
                print(f"{child.action} ({child.wins:.2f}/{child.visits})")

        return max(self.children, key=lambda c: c.visits)