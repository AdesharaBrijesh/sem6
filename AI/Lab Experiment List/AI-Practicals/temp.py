import matplotlib.pyplot as plt
import numpy as np

class StateNode:
    def __init__(self):
        self.board = [0 for _ in range(9)]  # Initialize the board
        self.fig, self.ax = plt.subplots(figsize=(5, 5))  # Create a subplot for the game
        self.ax.set_xlim(0, 3)
        self.ax.set_ylim(0, 3)
        self.ax.axis('off')

    def draw_board(self):
        self.ax.clear()  # Clear the existing plot
        # Draw grid lines
        self.ax.plot([1, 1], [0, 3], 'k')
        self.ax.plot([2, 2], [0, 3], 'k')
        self.ax.plot([0, 3], [1, 1], 'k')
        self.ax.plot([0, 3], [2, 2], 'k')
        
        # Plot X and O in their positions
        for index, player in enumerate(self.board):
            marker = 'X' if player == -1 else 'O' if player == 1 else ''
            if marker:
                self.ax.text((index % 3) + 0.5, 2 - (index // 3) + 0.5, marker, fontsize=40, ha='center', va='center')

        plt.pause(0.01)  # Pause for a short while to update the plot

    def set_move(self, cell, player):
        # Set a move on the board if the cell is empty
        if self.isValidMove(cell):
            self.board[cell] = player
            return True
        return False

    def isValidMove(self, cell):
        # Check if a move is valid (i.e., if the cell is empty)
        return self.board[cell] == 0

    def getEmptyCells(self):
        # Get a list of all empty cells on the board
        return [i for i, x in enumerate(self.board) if x == 0]

    def is_game_over(self):
        # Check if the game is over (win or tie)
        return self.isWin(-1) or self.isWin(1) or len(self.getEmptyCells()) == 0

    def isWin(self, player):
        # Check if a player has won the game
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]
        ]
        for combo in winning_combinations:
            if all(self.board[pos] == player for pos in combo):
                return True
        return False

class TicTacToe:
    def __init__(self):
        self.state = StateNode()
        plt.ion()  # Enable interactive mode

    def start_game(self):
        current_player = -1
        while True:
            if self.state.is_game_over():
                winner = self.state.is_game_over()
                if winner != 0:
                    print(f"{'X' if winner == -1 else 'O'} wins!")
                else:
                    print("It's a tie!")
                break
            
            if current_player == -1:
                self.player_move()
            else:
                self.computer_move()
                
            self.state.draw_board()
            current_player *= -1  # Switch player after each turn

    def player_move(self):
        move_valid = False
        while not move_valid:
            try:
                move = int(input("Enter your move (1-9): ")) - 1
                move_valid = self.state.set_move(move, -1)
                if not move_valid:
                    print("Invalid move. Try again.")
            except ValueError:
                print("Please enter a number between 1 and 9.")

    def computer_move(self):
        move_valid = False
        while not move_valid:
            move = int(input("Enter computer's move (1-9): ")) - 1
            move_valid = self.state.set_move(move, 1)
            if not move_valid:
                print("Invalid move. Try again.")

# Initialize and start the game
game = TicTacToe()
game.start_game()
