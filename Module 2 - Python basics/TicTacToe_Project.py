import re

dict_board: dict = {
    'board': [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
    ]
}
# row - rows of board
# col - columns of board
# cell - each cell in a specific row


def draw_board(current_board: dict[str, list[list[int]]]) -> str:
    formatted_rows = []
    for row in current_board["board"]:
        formatted_row = "| "
        for cell in row:
            if cell == 0:
                formatted_row += "_ | "
            elif cell == 1:
                formatted_row += "X | "
            elif cell == 2:
                formatted_row += "O | "
            else:
                raise ValueError("Something went wrong") # probably would never get here, but if so, raise an error so that I know
        formatted_rows.append(formatted_row.strip())
    return "\n----------\n".join(formatted_rows) # joining everything up to make it look pretty

def input_cell(turn):
    while True:
        current_input = input(f'Enter location for {"X" if turn else "O"} (row space column): ')
        if re.match(r"^\d \d$", current_input):
            row, col = map(int, current_input.split())
            row -= 1
            col -= 1
            if 0 <= row < len(dict_board["board"]) and 0 <= col < len(dict_board["board"][0]):
                if dict_board["board"][row][col] == 0:
                    dict_board["board"][row][col] = 1 if turn else 2
                    break
                else:
                    print(f"This cell is filled already with {dict_board["board"][row][col]}")
            else:
                print("Location is not available in this board.")
        else:
            print("Invalid input formatting.")

def check_horizontal(current_board):
    for row in current_board:
        if row[0] != 0 and all(cell == row[0] for cell in row):
            return "X" if row[0] == 1 else "O"
    return False


def check_win(current_board):
    pass

def check_tie(current_board):
    for row in current_board:
        if 0 in row:
            return False
    else:
        return True

def play_game_init(current_board, vs_computer: bool, turn: bool = True):

    turn = not turn



input_cell(True)
print(draw_board(dict_board))
