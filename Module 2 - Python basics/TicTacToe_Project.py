import re
import random

def initialize_board(rows, cols):
    return [[0 for _ in range(cols)] for _ in range(rows)]

def draw_board(current_board):
    formatted_rows = []
    for row in current_board:
        formatted_row = "| "
        for cell in row:
            if cell == 0:
                formatted_row += "_ | "
            elif cell == 1:
                formatted_row += "X | "
            elif cell == 2:
                formatted_row += "O | "
        formatted_rows.append(formatted_row.strip())
    return "\n----------\n".join(formatted_rows)

def input_cell(current_board, symbol, player_name):
    while True:
        current_input = input(f"{player_name}'s turn ({symbol}): Enter location (row space column) or type 'exit' to quit: ").strip()
        if current_input.lower() == 'exit':
            return 'exit'
        if re.match(r"^\d \d$", current_input):
            row, col = map(int, current_input.split())
            row -= 1
            col -= 1
            if 0 <= row < len(current_board) and 0 <= col < len(current_board[0]):
                if current_board[row][col] == 0:
                    current_board[row][col] = 1 if symbol == "X" else 2
                    return current_board
                else:
                    print(f"This cell is already filled with {'X' if current_board[row][col] == 1 else 'O'}.")
            else:
                print("Invalid location.")
        else:
            print("Invalid input format.")

def check_win(current_board):
    rows = len(current_board)
    cols = len(current_board[0])

    # Checking horizontal
    for row in current_board:
        if row[0] != 0 and all(cell == row[0] for cell in row):
            return "X" if row[0] == 1 else "O"

    # Checking vertical
    for col in range(cols):
        if current_board[0][col] != 0 and all(current_board[row][col] == current_board[0][col] for row in range(rows)):
            return "X" if current_board[0][col] == 1 else "O"

    # Checking diagonals
    if rows == cols:  # Diagonals only exist for square boards
        if current_board[0][0] != 0 and all(current_board[i][i] == current_board[0][0] for i in range(rows)):
            return "X" if current_board[0][0] == 1 else "O"
        if current_board[0][cols - 1] != 0 and all(current_board[i][cols - 1 - i] == current_board[0][cols - 1] for i in range(rows)):
            return "X" if current_board[0][cols - 1] == 1 else "O"

    return None

def check_tie(current_board):
    return all(cell != 0 for row in current_board for cell in row)

def computer_move(current_board):
    empty_cells = [(row, col) for row in range(len(current_board)) for col in range(len(current_board[0])) if current_board[row][col] == 0]
    if empty_cells:
        row, col = random.choice(empty_cells)
        current_board[row][col] = 2
    return current_board

def get_player_info():
    player1_name = input("Player 1, enter your name: ")
    player2_name = input("Player 2, enter your name (or type 'computer' to play against the computer): ")
    player1_symbol = input(f"{player1_name}, choose your symbol (X or O): ").strip().upper()
    while player1_symbol not in ["X", "O"]:
        player1_symbol = input("Invalid choice. Please choose X or O: ").strip().upper()
    player2_symbol = "O" if player1_symbol == "X" else "X"
    return (player1_name, player1_symbol), (player2_name, player2_symbol)

def play_game_init(current_board, vs_computer, player1, player2):
    print("Tic Tac Toe Game begins!")
    turn = True  # True for player 1's turn, False for player 2 or computer's turn
    while True:
        print(draw_board(current_board))
        if vs_computer and not turn:
            print(f"{player2[0]}'s turn (computer).")
            current_board = computer_move(current_board)
        else:
            current_player = player1 if turn else player2
            result = input_cell(current_board, current_player[1], current_player[0])
            if result == 'exit':
                return 'exit'
            current_board = result

        winner = check_win(current_board)
        if winner:
            print(draw_board(current_board))
            winner_name = player1[0] if winner == player1[1] else player2[0]
            print(f"{winner_name} wins!")
            break
        if check_tie(current_board):
            print(draw_board(current_board))
            print("It's a tie!")
            break
        turn = not turn
    return current_board

def play_game():
    while True:
        try:
            rows = int(input("Enter the number of rows for the board: "))
            cols = int(input("Enter the number of columns for the board: "))
            if rows < 3 or cols < 3:
                print("The board must be at least 3x3. Please try again.")
                continue
            current_board = initialize_board(rows, cols)
        except ValueError:
            print("Invalid input")
            continue

        player1, player2 = get_player_info()
        vs_computer = player2[0].lower() == "computer"

        result = play_game_init(current_board, vs_computer, player1, player2)
        if result == 'exit':
            print("Returning to main menu...")
            continue

        if input("Do you want to play again? (yes/no): ").strip().lower() not in ["yes", "y"]:
            print("Thanks for playing!")
            break

play_game()
