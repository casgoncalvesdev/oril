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