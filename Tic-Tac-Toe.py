import math

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def is_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def is_full(board):
    return all(cell != " " for row in board for cell in row)

def get_empty_cells(board):
    return [(row, col) for row in range(3) for col in range(3) if board[row][col] == " "]

def minimax(board, depth, is_maximizing, ai_player, human_player, alpha, beta):
    if is_winner(board, ai_player):
        return 10 - depth
    if is_winner(board, human_player):
        return depth - 10
    if is_full(board):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for row, col in get_empty_cells(board):
            board[row][col] = ai_player
            score = minimax(board, depth + 1, False, ai_player, human_player, alpha, beta)
            board[row][col] = " "
            best_score = max(best_score, score)
            alpha = max(alpha, score)
            if beta <= alpha:
                break
        return best_score
    else:
        best_score = math.inf
        for row, col in get_empty_cells(board):
            board[row][col] = human_player
            score = minimax(board, depth + 1, True, ai_player, human_player, alpha, beta)
            board[row][col] = " "
            best_score = min(best_score, score)
            beta = min(beta, score)
            if beta <= alpha:
                break
        return best_score

def best_move(board, ai_player, human_player):
    best_score = -math.inf
    move = None
    for row, col in get_empty_cells(board):
        board[row][col] = ai_player
        score = minimax(board, 0, False, ai_player, human_player, -math.inf, math.inf)
        board[row][col] = " "
        if score > best_score:
            best_score = score
            move = (row, col)
    return move

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]

    print("Welcome to Tic Tac Toe!")
    player_choice = ""
    while player_choice not in ["X", "O"]:
        player_choice = input("Do you want to be X or O? ").upper()

    human_player = player_choice
    ai_player = "O" if human_player == "X" else "X"

    player_turn = human_player == "X"

    print_board(board)

    while True:
        if player_turn:
            print("Players turn. Enter row and column (0-2):")
            try:
                row, col = map(int, input().split())
                if board[row][col] == " ":
                    board[row][col] = human_player
                    player_turn = False
                else:
                    print("Cell is already occupied! Try again.")
            except (ValueError, IndexError):
                print("Invalid input! Enter two numbers between 0 and 2.")
        else:
            print("AI's turn...")
            move = best_move(board, ai_player, human_player)
            if move:
                board[move[0]][move[1]] = ai_player
            player_turn = True

        print_board(board)

        if is_winner(board, human_player):
            print("You won! Congrats!")
            break
        if is_winner(board, ai_player):
            print("AI wins!")
            break
        if is_full(board):
            print("It's a draw!")
            break

if __name__ == "__main__":
    main()
