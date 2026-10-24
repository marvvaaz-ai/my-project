def print_uc_board(board):
    for uc_row in board:
        for sub_row in range(3):
            line = []
            for uc_col in range(3):
                line.append(' '.join(board[uc_row_i][uc_col][sub_row] for uc_row_i in [uc_row]))
            print(" || ".join(line))
        print("=" * 25)

def check_win_small(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2-i] == player for i in range(3)):
        return True
    return False

def check_draw_small(board):
    for row in board:
        if any(cell == ' ' for cell in row):
            return False
    return True

def check_win_uc(small_board_status, player):
    # Player wins if they control 3 in a row of sub-boards
    for row in small_board_status:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(small_board_status[row][col] == player for row in range(3)):
            return True
    if all(small_board_status[i][i] == player for i in range(3)):
        return True
    if all(small_board_status[i][2-i] == player for i in range(3)):
        return True
    return False

def check_draw_uc(small_board_status):
    for row in small_board_status:
        if any(cell == ' ' for cell in row):
            return False
    return True

def uc_tac_toe_game():
    # Each small board is a 3x3 board
    # uc_board is a 3x3 of 3x3s
    uc_board = [[[[' ' for _ in range(3)] for _ in range(3)] for _ in range(3)] for _ in range(3)]
    # small_board_status: tracks who has won each small board ('X', 'O', 'D', or ' ')
    small_board_status = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'
    next_uc_row, next_uc_col = None, None  # None means free choice for first move

    while True:
        print("\nUltimate Tic Tac Toe Board:")
        # Pretty print all small boards
        for uc_row in range(3):
            for small_row in range(3):
                line = []
                for uc_col in range(3):
                    line.append(' '.join(uc_board[uc_row][uc_col][small_row]))
                print(" || ".join(line))
            print("=" * 25)

        # Choose which small board to play in
        free_choice = (next_uc_row is None or next_uc_col is None 
                       or small_board_status[next_uc_row][next_uc_col] != ' ')
        if free_choice:
            print(f"Player {current_player}, you can choose ANY available small board.")
        else:
            print(f"Player {current_player}, you must play in small board at ({next_uc_row+1}, {next_uc_col+1})")

        # Input: small board
        while True:
            try:
                if free_choice:
                    uc_move_str = input("Select small board (row(1-3) col(1-3)): ")
                    uc_row, uc_col = map(int, uc_move_str.strip().split())
                    uc_row -= 1
                    uc_col -= 1
                    if not (0 <= uc_row < 3 and 0 <= uc_col < 3):
                        print("Invalid sub-board coordinates. Try again.")
                        continue
                    if small_board_status[uc_row][uc_col] != ' ':
                        print("That small board is already won/drawn. Try another.")
                        continue
                    break
                else:
                    uc_row, uc_col = next_uc_row, next_uc_col
                    break
            except Exception:
                print("Please enter two numbers separated by a space.")

        # Input: cell in small board
        while True:
            try:
                small_move = input(f"Player {current_player}, enter your move in small board ({uc_row+1},{uc_col+1}) as row(1-3) col(1-3): ")
                sub_row, sub_col = map(int, small_move.strip().split())
                sub_row -= 1
                sub_col -= 1
                if not (0 <= sub_row < 3 and 0 <= sub_col < 3):
                    print("Invalid cell coordinates. Try again.")
                    continue
                if uc_board[uc_row][uc_col][sub_row][sub_col] != ' ':
                    print("Cell already taken. Try again.")
                    continue
                break
            except Exception:
                print("Please enter two numbers separated by a space.")

        # Apply move
        uc_board[uc_row][uc_col][sub_row][sub_col] = current_player

        # Check if this small board is now won/drawn
        if small_board_status[uc_row][uc_col] == ' ':
            if check_win_small(uc_board[uc_row][uc_col], current_player):
                small_board_status[uc_row][uc_col] = current_player
                print(f"Player {current_player} won small board ({uc_row+1},{uc_col+1})!")
            elif check_draw_small(uc_board[uc_row][uc_col]):
                small_board_status[uc_row][uc_col] = 'D'
                print(f"Small board ({uc_row+1},{uc_col+1}) is a draw!")

        # Check if the global game is won
        if check_win_uc(small_board_status, current_player):
            print("\nFinal Board:")
            for uc_row_print in range(3):
                for small_row in range(3):
                    line = []
                    for uc_col in range(3):
                        line.append(' '.join(uc_board[uc_row_print][uc_col][small_row]))
                    print(" || ".join(line))
                print("=" * 25)
            print(f"Player {current_player} WINS THE GAME!")
            break
        elif check_draw_uc(small_board_status):
            print("\nFinal Board:")
            for uc_row_print in range(3):
                for small_row in range(3):
                    line = []
                    for uc_col in range(3):
                        line.append(' '.join(uc_board[uc_row_print][uc_col][small_row]))
                    print(" || ".join(line))
                print("=" * 25)
            print("Ultimate Tic Tac Toe ends in a draw!")
            break

        # Determine the next small board to play on
        next_uc_row, next_uc_col = sub_row, sub_col
        if small_board_status[next_uc_row][next_uc_col] != ' ':
            # That board is full - next player chooses
            next_uc_row, next_uc_col = None, None

        # Alternate player
        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    uc_tac_toe_game()