from a2_partb import GameTree

class PlayerOne:

    def __init__(self, name = "P1 Bot"):
        self.name = name
        self.search_depth = 2

    def set_difficulty(self, difficulty):
        self.search_depth = difficulty

    def get_name(self):
        return self.name

    def get_play(self, board):
        game_tree = GameTree(board, 1, tree_height=self.search_depth)
        return game_tree.get_move()