print('21012011072_Divy Patel')

class StateNode:
    def __init__(self):
        self.board = [0 for _ in range(9)]
        self.player_symbol = -1  # Default player symbol (X)
        self.computer_symbol = 1  # Default computer symbol (O)

    def draw_board(self):
        symbols = {0: '_', -1: 'X', +1: 'O'}
        for row in range(3):
            print('|'.join(symbols[self.board[row * 3 + col]] for col in range(3)))

    def set_move(self, cell, player):
        if self.is_valid_move(cell):
            self.board[cell] = player
            return True
        return False

    def is_valid_move(self, cell):
        return self.board[cell] == 0

    def get_empty_cells(self):
        return [i for i, x in enumerate(self.board) if x == 0]

    def is_game_over(self):
        return self.is_win(self.player_symbol) or self.is_win(self.computer_symbol) or len(self.get_empty_cells()) == 0

    def is_win(self, player):
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]
        ]
        for combo in winning_combinations:
            if all(self.board[pos] == player for pos in combo):
                return True
        return False

    def get_score_value(self, depth):
        if self.is_win(self.computer_symbol):
            return 10 - depth
        elif self.is_win(self.player_symbol):
            return depth - 10
        else:
            return 0


class TicTacToe:
    def __init__(self):
        self.state = StateNode()

    def start_game(self):
        self.setup_game()
        current_player = self.state.player_symbol
        while True:
            self.state.draw_board()
            if self.state.is_game_over():
                self.print_result()
                break

            if current_player == self.state.player_symbol:
                self.player_move()
            else:
                self.computer_move()
            current_player *= -1
            print('-' * 20)  # Add line between moves

    def setup_game(self):
        symbol_choice = input("Choose your symbol [O/X]: ").upper()
        if symbol_choice not in ["O", "X"]:
            print("Invalid choice. Defaulting to X.")
            symbol_choice = "X"

        if symbol_choice == "O":
            self.state.player_symbol, self.state.computer_symbol = 1, -1
        else:
            self.state.player_symbol, self.state.computer_symbol = -1, 1

    def player_move(self):
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            if move < 0 or move > 8 or not self.state.set_move(move, self.state.player_symbol):
                print("Invalid move. Try again.")
                self.player_move()
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")
            self.player_move()

    def computer_move(self):
        _, move = self.minimax(True)
        self.state.set_move(move, self.state.computer_symbol)

    def minimax(self, is_maximizing, depth=0):
        if self.state.is_game_over():
            return self.state.get_score_value(depth), None

        best_score = float('-inf') if is_maximizing else float('inf')
        best_move = None

        for move in self.state.get_empty_cells():
            self.state.board[move] = self.state.computer_symbol if is_maximizing else self.state.player_symbol
            score, _ = self.minimax(not is_maximizing, depth + 1)
            self.state.board[move] = 0  # Reset the move

            if is_maximizing:
                if score > best_score:
                    best_score, best_move = score, move
            else:
                if score < best_score:
                    best_score, best_move = score, move

        return best_score, best_move

    def print_result(self):
        if self.state.is_win(self.state.player_symbol):
            print("Player wins!")
        elif self.state.is_win(self.state.computer_symbol):
            print("Computer wins!")
        else:
            print("It's a tie!")


game = TicTacToe()
game.start_game()