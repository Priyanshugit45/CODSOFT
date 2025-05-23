def print_board(board):
    for row in board:
        print("|".join(row))
        print("-"*5)

def check_winner(board, player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    return board[0][0] == board[1][1] == board[2][2] == player or board[0][2] == board[1][1] == board[2][0] == player

def is_full(board):
    return all(cell != " " for row in board for cell in row)

def get_empty(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]

def minimax(board, is_max):
    if check_winner(board, "O"): return 1
    if check_winner(board, "X"): return -1
    if is_full(board): return 0

    if is_max:
        best = -float("inf")
        for i, j in get_empty(board):
            board[i][j] = "O"
            score = minimax(board, False)
            board[i][j] = " "
            best = max(best, score)
        return best
    else:
        best = float("inf")
        for i, j in get_empty(board):
            board[i][j] = "X"
            score = minimax(board, True)
            board[i][j] = " "
            best = min(best, score)
        return best

def ai_move(board):
    best_score = -float("inf")
    move = None
    for i, j in get_empty(board):
        board[i][j] = "O"
        score = minimax(board, False)
        board[i][j] = " "
        if score > best_score:
            best_score = score
            move = (i, j)
    return move

def play():
    board = [[" "]*3 for _ in range(3)]
    print("Tic-Tac-Toe: You're X, AI is O. Enter row col (0-2, e.g., '1 1').")
    
    while True:
        print_board(board)
        try:
            row, col = map(int, input("Move: ").split())
            if 0 <= row <= 2 and 0 <= col <= 2 and board[row][col] == " ":
                board[row][col] = "X"
            else:
                print("Invalid move!")
                continue
        except:
            print("Enter 'row col' (e.g., '1 1')")
            continue

        if check_winner(board, "X"):
            print_board(board)
            print("You win!")
            break
        if is_full(board):
            print_board(board)
            print("Tie!")
            break

        row, col = ai_move(board)
        board[row][col] = "O"
        print(f"AI moves to ({row}, {col})")

        if check_winner(board, "O"):
            print_board(board)
            print("AI wins!")
            break
        if is_full(board):
            print_board(board)
            print("Tie!")
            break

if __name__ == "__main__":
    play()