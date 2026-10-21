def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_win(board, player):
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True
    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    # Check diagonals
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2-i] == player for i in range(3)):
        return True
    return False

def check_draw(board):
    for row in board:
        if any(cell == ' ' for cell in row):
            return False
    return True

def tiktaktok_game():
    board = [[' ']*3 for _ in range(3)]
    current_player = 'X'
    while True:
        print_board(board)
        try:
            move = input(f"Player {current_player}, enter your move (row(1-3) col(1-3)): ")
            row, col = map(int, move.strip().split())
            row -= 1
            col -= 1
            if not (0 <= row < 3 and 0 <= col < 3):
                print("Invalid position, choose again.")
                continue
            if board[row][col] != ' ':
                print("Cell already taken, choose again.")
                continue
            board[row][col] = current_player
            if check_win(board, current_player):
                print_board(board)
                print(f"Player {current_player} wins!")
                break
            if check_draw(board):
                print_board(board)
                print("It's a draw!")
                break
            current_player = 'O' if current_player == 'X' else 'X'
        except Exception:
            print("Invalid input, please enter row and column as numbers separated by space.")

if __name__ == "__main__":
    tiktaktok_game()