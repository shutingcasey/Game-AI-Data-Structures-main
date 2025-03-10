# Main Author: Christine Ang
# Main Reviewer: Hyeri Jang & Casey Hsu

from a1_partd import overflow
from a1_partc import Queue

# This function duplicates and returns the board.
def copy_board(board):
        current_board = []
        height = len(board)
        for i in range(height):
            current_board.append(board[i].copy())
        return current_board


# this function accepts: 
# board - a 2D grid with numbers, the numbers correspond to the number of game pieces in each cell
# player - represented by either +1 (player 1) or -1 (player 2)
# this function counts the number of game pieces for each player, compares and determines if is a winning, losing, non-winning and returns a score
def evaluate_board(board, player):

    rows = len(board)
    cols = len(board[0])

    player_picked = 0
    opponent = 0
    score = 0
    
    for i in range(rows):
        for j in range(cols):
            if player * board[i][j] > 0:
                player_picked += abs(board[i][j])
            elif player * board[i][j] < 0:
                opponent += abs(board[i][j])

    if opponent == 0 and player_picked > 0:
        score = 999
    elif player_picked == 0 and opponent > 0:
        score = -999
    else:
        score = player_picked - opponent

    return score


class GameTree:
    
    class Node:
        
        # this function initialises a node
        # it accepts: a board which is a 2D array representing board of the node,
        # depth, tree height and player
        def __init__(self, board, depth, player, tree_height = 4):
            
            self.depth = depth
            self.player = player
            self.tree_height = tree_height
            
            #stores score of board
            self.score = 0 
        
            #track the children
            self.children = []
            
            a_queue = Queue()
            
            #get the last board added to the queue
            overflow(board, a_queue)
            while  not a_queue.is_empty():
                board = a_queue.dequeue()
            
               
            self.board = board
                    
            self.move = (-1,-1)
            
        
    # this function initialises the GameTree object
    # it accepts a board (2D array), tree_height which is the maximum height of the tree, 
    # player who the tree is being created for
    # this function also sets the root of the node which is the current board state
    # then, it calls the function that recursively generates the children of the parent/root node
    def __init__(self, board, player, tree_height = 4):

        self.player = player
        self.board = copy_board(board)
        self.tree_height = tree_height
        
        depth = 0; 
        
        # root is the current state of the board
        self.root = self.Node(board, depth, player, tree_height)

        # call recursive function that will create children nodes
        self.create_children_nodes(self.root)

               
    # this is a recursive function that accepts a node representing the parent node
    # the function determines the next possible move on the board depending on the player and "moves" the player to the available spot creating a "new board",
    # a new node is then created with the "new board" and this node is added to the array of nodes representing the children for that parent node
    def create_children_nodes(self, parent_node):
        
        if parent_node.depth != parent_node.tree_height-1:
        
            for i in range(len(parent_node.board)):
                for j in range(len(parent_node.board[0])):
                    
                    #determine if the space is available - if empty or has player gems in it
                    if(parent_node.board[i][j]==0 or parent_node.board[i][j]/abs(parent_node.board[i][j]) == parent_node.player):
                        
                        new_board = copy_board(parent_node.board)
                        
                        # adds gem to available space depending on the player
                        new_board[i][j] += parent_node.player

                        # create a new node
                        child_node = self.Node(new_board, parent_node.depth + 1, parent_node.player * -1, self.tree_height)
                        
                        # store the move 
                        child_node.move = (i, j)
                        
                        # add children to parent 
                        parent_node.children.append(child_node)
                        
                        self.create_children_nodes(child_node)
                        
    # this function is a recursive function with the minimax algorithm
    # it accepts a node, depth, and player
    # recursion will stop if the depth reaches the max tree height or if after evaluation the board is determined to be a winning or losing board
    # the board is evaluated depending on the player then compared to a "best score"
    # the "best score" is then returned
    # this function provides a score for each board which then helps determine the best move 
    def minimax(self, node, depth, player):
        
        # determine if board is terminal state
        node.score = evaluate_board(node.board,player)
        
        # base case
        if depth == node.tree_height-1 or node.score == 999 or node.score == -999: 
            return node.score

        if player == 1:
            best_score = -999
            # loop through the children of this node until base case reached
            for child_node in node.children:
                score = self.minimax(child_node, depth + 1, player * -1)
                best_score = max(best_score, score)
                node.score = best_score
            return best_score
        else:
            best_score = 999
            for child_node in node.children:
                score = self.minimax(child_node, depth + 1, player * -1)
                best_score = min(best_score, score) 
                node.score = best_score
            return best_score
            

    # this function returns a coordinate (row, col) on the board which is the next best move
    # for every child node, the minimax algorithm is called and returns a score
    # once the child node with the best score is determined, then the next move of that node is considered the best move
    def get_move(self):

        best_score = -999
        best_move = (-1, -1)
        
        # Find and return the move with the best score
        for child_node in self.root.children:
            score = self.minimax(child_node, child_node.depth, child_node.player * -1)
            if score > best_score: 
                best_score = score
                best_move = child_node.move
        
        return best_move

    # this function calls the recursive helper function by passing the root node
    def clear_tree(self):
        
       self.clear_treeR(self.root)
    
    # recursive function that accepts a node, and recursively assigns a value of None to the nodes
    # this function destroys the game tree by unlinking all nodes in order
    def clear_treeR(self, node):
        if node != None:
            for child_node in node.children:
                self.clear_treeR(child_node)
            node.children = None