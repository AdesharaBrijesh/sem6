# class StateNode:
#     def __init__(self):
#         self.board = [[0, 0, 0],
#                       [0, 0, 0],
#                       [0, 0, 0]]

#     def print_board(self):
#         print("   1  2  3")
#         for i in range(3):
#             print(f"{i+1} ", end="")
#             for j in range(3):
#                 if self.board[i][j] == 1:
#                     print(" X ", end="")
#                 elif self.board[i][j] == -1:
#                     print(" O ", end="")
#                 else:
#                     print("   ", end="")
#                 if j < 2:
#                     print("|", end="")
#             print()

#     def user_move(self, symbol):
#         while True:
#             try:
#                 move = int(input("Enter your move (1-9): "))
#                 if 1 <= move <= 9:
#                     row = (move - 1) // 3
#                     col = (move - 1) % 3
#                     if self.board[row][col] == 0:
#                         self.board[row][col] = symbol
#                         break
#                     else:
#                         print("Position already taken. Try again.")
#                 else:
#                     print("Invalid input. Enter a number between 1 and 9.")
#             except ValueError:
#                 print("Invalid input. Enter a number.")

#     def isWin(self, symbol):
#         winning_patterns = [
#             [(0, 0), (0, 1), (0, 2)],  # Row 1
#             [(1, 0), (1, 1), (1, 2)],  # Row 2
#             [(2, 0), (2, 1), (2, 2)],  # Row 3
#             [(0, 0), (1, 0), (2, 0)],  # Column 1
#             [(0, 1), (1, 1), (2, 1)],  # Column 2
#             [(0, 2), (1, 2), (2, 2)],  # Column 3
#             [(0, 0), (1, 1), (2, 2)],  # Diagonal 1
#             [(0, 2), (1, 1), (2, 0)]   # Diagonal 2
#         ]
#         for pattern in winning_patterns:
#             if all(self.board[row][col] == symbol for row, col in pattern):
#                 return True
#         return False

#     def getScoreValue(self):
#         if self.isWin(-1):
#             return -1  # Player 2 (AI) wins
#         elif self.isWin(1):
#             return 1   # Player 1 (User) wins
#         elif self.isGameOver():
#             return 0   # Draw
#         else:
#             return None

#     def getEmptyCells(self):
#         empty_cells = []
#         for i in range(3):
#             for j in range(3):
#                 if self.board[i][j] == 0:
#                     empty_cells.append((i, j))
#         return empty_cells

#     def isGameOver(self):
#         empty_cells = self.getEmptyCells()
#         return len(empty_cells) == 0


# def TicTacToe():
#     game = StateNode()
#     print("Welcome to Tic Tac Toe!")
#     while True:
#         user_symbol = int(input("Choose Your Symbol X = 1 / O = -1 : "))
#         if user_symbol == 1:
#             ai_symbol = -1
#             print("User: X, AI: O")
#             break
#         elif user_symbol == -1:
#             ai_symbol = 1
#             print("User: O, AI: X")
#             break
#         else:
#             print("Invalid input. Please choose 1 or -1.")


#     while True:
#         game.print_board()
#         game.user_move(user_symbol)  # Player 1 (User) move
#         game.print_board()
#         score_value = game.getScoreValue()
#         if score_value is not None:
#             if score_value == 1:
#                 print("Congratulations! You win!")
#             elif score_value == -1:
#                 print("Sorry, you lose!")
#             else:
#                 print("It's a draw!")
#             break

#         game.user_move(ai_symbol)  # Player 2 (User) move
#         game.print_board()
#         score_value = game.getScoreValue()
#         if score_value is not None:
#             if score_value == 1:
#                 print("Congratulations! You win!")
#             elif score_value == -1:
#                 print("Sorry, you lose!")
#             else:
#                 print("It's a draw!")
#             break


# TicTacToe()



