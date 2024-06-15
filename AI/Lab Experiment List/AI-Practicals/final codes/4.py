class StateNode:
    def __init__(self):
        self.board = [[0, 0, 0],
                      [0, 0, 0],
                      [0, 0, 0]]

    def print_board(self):
        print("   1  2  3")
        for i in range(3):
            print(f"{i+1} ", end="")
            for j in range(3):
                if self.board[i][j] == 1:
                    print(" O ", end="")
                elif self.board[i][j] == -1:
                    print(" X ", end="")
                else:
                    print("   ", end="")
                if j < 2:
                    print("|", end="")
            print()

    def user_move(self, symbol):
        while True:
            try:
                move = int(input("Enter your move (1-9): "))
                if 1 <= move <= 9:
                    row = (move - 1) // 3
                    col = (move - 1) % 3
                    if self.board[row][col] == 0:
                        self.board[row][col] = symbol
                        break
                    else:
                        print("Position already taken. Try again.")
                else:
                    print("Invalid input. Enter a number between 1 and 9.")
            except ValueError:
                print("Invalid input. Enter a number.")

    def ai_move(self, symbol):
        best_move = None
        best_score = -float('inf') if symbol == -1 else float('inf')
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == 0:
                    self.board[i][j] = symbol
                    score = self.minimax(self.board, 0, False if symbol == -1 else True)
                    self.board[i][j] = 0
                    if symbol == -1:  # AI is the maximizing player
                        if score > best_score:
                            best_score = score
                            best_move = (i, j)
                    else:  # AI is the minimizing player
                        if score < best_score:
                            best_score = score
                            best_move = (i, j)
        self.board[best_move[0]][best_move[1]] = symbol

    def minimax(self, state, depth, is_maximizing):
        score = self.getScoreValue(state)
        if score is not None:
            return score

        if is_maximizing:
            best_score = -float('inf')
            for i in range(3):
                for j in range(3):
                    if state[i][j] == 0:
                        state[i][j] = -1
                        score = self.minimax(state, depth + 1, False)
                        state[i][j] = 0
                        best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            for i in range(3):
                for j in range(3):
                    if state[i][j] == 0:
                        state[i][j] = 1
                        score = self.minimax(state, depth + 1, True)
                        state[i][j] = 0
                        best_score = min(score, best_score)
            return best_score

    def isWin(self, state, symbol):
        winning_patterns = [
            [(0, 0), (0, 1), (0, 2)],  # Row 1
            [(1, 0), (1, 1), (1, 2)],  # Row 2
            [(2, 0), (2, 1), (2, 2)],  # Row 3
            [(0, 0), (1, 0), (2, 0)],  # Column 1
            [(0, 1), (1, 1), (2, 1)],  # Column 2
            [(0, 2), (1, 2), (2, 2)],  # Column 3
            [(0, 0), (1, 1), (2, 2)],  # Diagonal 1
            [(0, 2), (1, 1), (2, 0)]   # Diagonal 2
        ]
        for pattern in winning_patterns:
            if all(state[row][col] == symbol for row, col in pattern):
                return True
        return False

    def getScoreValue(self, state):
        if self.isWin(state, -1):
            return 1  # AI wins
        elif self.isWin(state, 1):
            return -1  # Player wins
        elif self.isGameOver(state):
            return 0  # Draw
        else:
            return None

    def isGameOver(self, state):
        if self.isWin(state, 1) or self.isWin(state, -1):
            return True
        for row in state:
            if 0 in row:
                return False
        return True


def play_game():
    game = StateNode()
    print("Welcome to Tic Tac Toe!")
    user_symbol = int(input("Choose your symbol (1 for O, -1 for X): "))
    opponent = input("Choose opponent (AI/Friend): ")
    while opponent.lower() not in ['ai', 'friend']:
        print("Invalid opponent. Please choose either AI or Friend.")
        opponent = input("Choose opponent (AI/Friend): ")

    while True:
        game.print_board()
        game.user_move(user_symbol)  # Player 1 (User) move
        game.print_board()
        score_value = game.getScoreValue(game.board)
        if score_value is not None:
            if score_value == -1:
                print("Congratulations! You win!")
            elif score_value == 1:
                print("Sorry, you lose!")
            else:
                print("It's a draw!")
            break

        if opponent.lower() == 'ai':
            print("Computer move:")
            game.ai_move(-user_symbol)  # AI move
            game.print_board()  # Print the board after the AI move
        else:
            game.user_move(-user_symbol)  # Player 2 (Friend) move
            game.print_board()  # Print the board after Player 2's move

        score_value = game.getScoreValue(game.board)
        if score_value is not None:
            if score_value == -1:
                print("Congratulations! You win!")
            elif score_value == 1:
                print("Sorry, you lose!")
            else:
                print("It's a draw!")
            break


play_game()
