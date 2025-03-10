#   Author: Catherine Leung
#   This is the game that you will code the bots to play.  You can also play against your bot
#   To run the game you will need pygames installed.  See: https://pypi.org/project/pygame/
#   Once you have pygames, you can run the game by using the command:
#   python game.py
#   
#   the gem images used are from opengameart.org by qubodup
#   https://opengameart.org/content/rotating-crystal-animation-8-step,
#   https://creativecommons.org/licenses/by/3.0/

import pygame
import sys
import math

from a1_partd import overflow
from a1_partc import Queue
from a1_partc import Stack # Use stack to record historical boards
from player1 import PlayerOne
from player2 import PlayerTwo 

# Extended HistoryStack class for managing game history
class HistoryStack:
    def __init__(self):
        self.history = Stack()  # Use the original Stack to store history

    # Push a copy of the board onto the stack.
    def push(self, board):
        self.history.push([row.copy() for row in board])

    # Pop the previous board state from the stack
    def pop(self):
        if not self.history.is_empty():
            return self.history.pop()
        return None

    # Get the board state at the top of the stack
    def get_top(self):
        return self.history.get_top()

    # Check if the stack is empty.
    def is_empty(self):
        return self.history.is_empty()

class Dropdown:
    def __init__(self, x, y, width, height, options):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.options = options
        self.current_option = 0

    def draw(self, window):
        pygame.draw.rect(window, BLACK, (self.x, self.y, self.width, self.height), 2)
        font = pygame.font.Font(None, 36)
        text = font.render(self.options[self.current_option], 1, BLACK)
        window.blit(text, (self.x + 5, self.y + 5))

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if self.x < x < self.x + self.width and self.y < y < self.y + self.height:
                self.current_option = (self.current_option + 1) % len(self.options)

    def get_choice(self):
        return self.current_option

class Board:
    def __init__(self,width,height, p1_sprites, p2_sprites):
        self.width = width
        self.height = height
        self.board = [[0 for _ in range(width)] for _ in range(height)]
        self.p1_sprites = p1_sprites
        self.p2_sprites = p2_sprites
        self.board[0][0] = 1
        self.board[self.height-1][self.width-1] = -1
        self.turn = 0

    def get_board(self):
        current_board = []
        for i in range(self.height):
            current_board.append(self.board[i].copy())
        return current_board

    def valid_move(self, row,col,player):
        if row >= 0  and row < self.height and col >= 0 and col < self.width and (self.board[row][col]==0 or self.board[row][col]/abs(self.board[row][col]) == player):
            return True
        return False

    def add_piece(self, row, col, player):
        if self.valid_move(row, col, player):
            self.board[row][col] += player
            self.turn += 1
            return True
        return False

    def check_win(self):
        if(self.turn > 0):
            num_p1 = 0
            num_p2 = 0
            for i in range(self.height):
                for j in range(self.width):
                    if(self.board[i][j] > 0):
                        if num_p2 > 0:
                            return 0
                        num_p1 += 1
                    elif(self.board[i][j] < 0):
                        if num_p1 > 0:
                            return 0
                        num_p2 += 1
            if(num_p1 == 0):
                return -1
            if(num_p2== 0):
                return 1
        return 0

    def do_overflow(self,q):
        oldboard = []
        for i in range(self.height):
            oldboard.append(self.board[i].copy())
        numsteps = overflow(self.board, q)
        if(numsteps != 0):
            self.set(oldboard)
        return numsteps
    
    def set(self, newboard):
        for row in range(self.height):
            for col in range(self.width):
                self.board[row][col] = newboard[row][col]

    def draw(self, window, frame):
        for row in range(GRID_SIZE[0]):
            for col in range(GRID_SIZE[1]):
                rect = pygame.Rect(col * CELL_SIZE + X_OFFSET, row * CELL_SIZE+Y_OFFSET, CELL_SIZE, CELL_SIZE)
                pygame.draw.rect(window, BLACK, rect, 1)
        for row in range(self.height):
            for col in range(self.width):
                if self.board[row][col] != 0:
                    rpos = row * CELL_SIZE + Y_OFFSET
                    cpos = col * CELL_SIZE + X_OFFSET
                    if self.board[row][col] > 0:
                        sprite = p1_sprites
                    else:
                        sprite = p2_sprites
                    if abs(self.board[row][col]) == 1:
                        cpos += CELL_SIZE //2 - 16
                        rpos += CELL_SIZE //2 - 16
                        window.blit(sprite[math.floor(frame)], (cpos, rpos))
                    elif abs(self.board[row][col]) == 2:
                        cpos += CELL_SIZE //2 - 32
                        rpos += CELL_SIZE //2 - 16
                        window.blit(sprite[math.floor(frame)], (cpos, rpos))
                        cpos += 32
                        window.blit(sprite[math.floor(frame)], (cpos, rpos))

                    elif abs(self.board[row][col]) == 3:
                        cpos += CELL_SIZE //2 - 16
                        rpos += 8
                        window.blit(sprite[math.floor(frame)], (cpos, rpos))
                        cpos = col * CELL_SIZE + X_OFFSET + CELL_SIZE //2 - 32
                        rpos += CELL_SIZE //2
                        window.blit(sprite[math.floor(frame)], (cpos, rpos))
                        cpos += 32
                        window.blit(sprite[math.floor(frame)], (cpos, rpos))
                    elif abs(self.board[row][col]) == 4:
                        cpos += CELL_SIZE //2 - 32
                        rpos += 8
                        window.blit(sprite[math.floor(frame)], (cpos, rpos))
                        rpos += CELL_SIZE //2
                        window.blit(sprite[math.floor(frame)], (cpos, rpos))
                        cpos += 32
                        window.blit(sprite[math.floor(frame)], (cpos, rpos))
                        rpos -= CELL_SIZE //2
                        window.blit(sprite[math.floor(frame)], (cpos, rpos))
    def undo_last_move(self, steps):
        # Make sure to undo the correct number of steps
        for _ in range(steps):
            if not self.history.is_empty():
                self.board = self.history.pop()  # Undo a step
                self.turn -= 1  # Decrease turn count
            else:
                print("No more moves to undo")  # Unable to undo further steps
                break

# Extended for Board with undo button
class BoardWithUndo(Board):
    def __init__(self, width, height, p1_sprites, p2_sprites):
        super().__init__(width, height, p1_sprites, p2_sprites)
        self.history = HistoryStack()  # Add history functionality
        self.history.push(self.board)  # Save the initial board state at initialization
    
    # Player makes a move and saves the board history.
    def add_piece(self, row, col, player,is_human):
        self.history.push(self.board)  # Save the current board state
        super().add_piece(row, col, player)  # Use parent class logic
    
    # Undo the last move.
    def undo_last_move(self, steps):
        for _ in range(steps):
            previous_state = self.history.pop()
            if previous_state:
                self.board = previous_state
                self.turn -= 1  # Decrease turn count
            else:
                print("No more moves to undo!")
                break

    # Display the board
    def display_board(self):
        for row in self.board:
            print(row)
        print()  


# Constants
GRID_SIZE = (5, 6)
CELL_SIZE = 100
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
X_OFFSET = 0
Y_OFFSET = 100
FULL_DELAY = 5

# hate the colours?  there are other options.  Just change the lines below to another colour's file name.  
# the following are available blue, pink, yellow, orange, grey, green
p1spritesheet = pygame.image.load('blue.png')
p2spritesheet = pygame.image.load('pink.png')
p1_sprites = []
p2_sprites = []


player_id = [1 , -1]


for i in range(8):
    curr_sprite = pygame.Rect(32*i,0,32,32)
    p1_sprites.append(p1spritesheet.subsurface(curr_sprite))
    p2_sprites.append(p2spritesheet.subsurface(curr_sprite))    


frame = 0

# Initialize Pygame
pygame.init()
window = pygame.display.set_mode((1200,800))

pygame.font.init()
font = pygame.font.Font(None, 36)  # Change the size as needed
bigfont = pygame.font.Font(None, 108)

# undo bottom
undo_button = pygame.Rect(900, 250, 200, 50)

# Create the game board
# board = [[0 for _ in range(GRID_SIZE[0])] for _ in range(GRID_SIZE[1])]
player1_dropdown = Dropdown(900, 50, 200, 50, ['Human', 'AI'])
player2_dropdown = Dropdown(900, 110, 200, 50, ['Human', 'AI'])

# Second function
# Difficulty dropdown 
difficulty_dropdown = Dropdown(900, 170, 200, 50, ['Easy', 'Medium', 'Hard'])


status=["",""]
current_player = 0
board = BoardWithUndo(GRID_SIZE[1], GRID_SIZE[0], p1_sprites, p2_sprites)


# Game loop
running = True
overflow_boards = Queue()
overflowing = False
numsteps = 0
has_winner = False
bots = [PlayerOne(), PlayerTwo()]

# Initialization difficulty
bot_difficulty = 2  # set to "Easy"
bots[0].set_difficulty(bot_difficulty)
bots[1].set_difficulty(bot_difficulty)

grid_col = -1
grid_row = -1
choice = [None, None]
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # press the undo bottom
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if undo_button.collidepoint(x, y):
                # Restrictions: The game is not over and the current player is Human
                if not has_winner and choice[current_player] == 0:  # Only human players can undo
                    steps_to_undo = 1
                    if choice[(current_player + 1) % 2] == 1:  # If the opponent is AI
                        steps_to_undo = 2  # Skip 2 versions per undo (full turn)
                    if not board.history.is_empty() and len(board.history.history) >= steps_to_undo:
                        board.undo_last_move(steps_to_undo)  # Undo specified number of steps數
                        # Update current_player
                        current_player = (current_player - steps_to_undo * 2) % 2  
                    else:
                        print("Not enough versions to undo")
    
            else:
                player1_dropdown.handle_event(event)
                player2_dropdown.handle_event(event)
                difficulty_dropdown.handle_event(event) # Added difficulty menu event processing

                choice[0] = player1_dropdown.get_choice()
                choice[1] = player2_dropdown.get_choice()
                difficulty_choice = difficulty_dropdown.get_choice() # Get difficulty selection
                    
                if difficulty_choice == 0:  # Easy
                    bot_difficulty = 2
                elif difficulty_choice == 1:  # Medium
                    bot_difficulty = 4
                else:  # Hard
                    bot_difficulty = 6

                # update AI    
                bots[0].set_difficulty(bot_difficulty)
                bots[1].set_difficulty(bot_difficulty)
                

        if event.type == pygame.MOUSEBUTTONDOWN:
            x,y = event.pos
            row = y - Y_OFFSET
            col = x - X_OFFSET    
            grid_row, grid_col = row // CELL_SIZE, col // CELL_SIZE

    win = board.check_win()
    if win != 0:
        winner = 1
        if win == -1:
            winner = 2
        has_winner = True

    if not has_winner:
        if overflowing:
            status[0] = "Overflowing"
            if not overflow_boards.is_empty():
                if repeat_step == FULL_DELAY:
                    next = overflow_boards.dequeue()
                    board.set(next)
                    repeat_step = 0
                else:
                    repeat_step += 1
            else:
                overflowing = False

                # goes between 0 and 1
                current_player = (current_player + 1) % 2

        else:
            status[0] = "Player " + str(current_player + 1) + "'s turn"
            make_move = False

            if choice[current_player] == 1:
                (grid_row,grid_col) = bots[current_player].get_play(board.get_board())
                status[1] = "Bot chose row {}, col {}".format(grid_row, grid_col)
                if not board.valid_move(grid_row, grid_col, player_id[current_player]):
                       has_winner = True
                       # if p1 makes an invalid move, p2 wins.  if p2 makes an invalid move p1 wins
                       winner = ((current_player + 1) % 2) + 1 
                else:
                    make_move = True
            else:
                if board.valid_move(grid_row, grid_col, player_id[current_player]):
                    make_move = True

        if make_move:
            board.add_piece(grid_row, grid_col, player_id[current_player],choice[current_player] == 0)
            numsteps = board.do_overflow(overflow_boards)
            if numsteps != 0:
                overflowing = True
                repeat_step = 0
            else:
                current_player = (current_player + 1) % 2
            grid_row = -1
            grid_col = -1

    # Draw the game board
    window.fill(WHITE)
    board.draw(window,frame)
    # Draw the undo bottom
    pygame.draw.rect(window, BLACK, undo_button)  
    text = font.render("Undo", True, WHITE)
    window.blit(text, (undo_button.x + 50, undo_button.y + 10)) 

    player1_dropdown.draw(window)
    player2_dropdown.draw(window)

    difficulty_dropdown.draw(window)

    # Add status reminder
    if has_winner:
        status[1] = "Undo not allowed: Game over"
    elif choice[current_player] == 1:
        status[1] = "Undo not allowed: AI turn"
    elif board.history.is_empty():
        status[1] = "Undo not allowed: No move to undo"
    else:
        status[1] = "Undo available"

    window.blit(p1_sprites[math.floor(frame)], (850, 60))
    window.blit(p2_sprites[math.floor(frame)], (850, 120))
    frame = (frame + 0.5) % 8


    if not has_winner:  
        text = font.render(status[0], True, (0, 0, 0))  # Black color
        window.blit(text, (X_OFFSET, 750 ))
        text = font.render(status[1], True, (0, 0, 0))  # Black color
        window.blit(text, (X_OFFSET,  700 ))
    else:
        text = bigfont.render("Player " + str(winner)  + " wins!", True, (0, 0, 0))  # Black color
        window.blit(text, (300, 250))



    pygame.display.update()
    pygame.time.delay(100)

pygame.quit()
sys.exit()