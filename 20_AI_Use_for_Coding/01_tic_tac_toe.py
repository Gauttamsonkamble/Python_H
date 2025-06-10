# write a code to play tic-tac-toe
import random

def greet():
    print("Welcome to Tic-Tac-Toe!")
    print("You are 'X' and the computer is 'O'.")
    print("Enter your move as a number from 1 to 9, corresponding to the board positions:")
    print(" 1 | 2 | 3 ")
    print("-----------")

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    # Check rows, columns and diagonals
    for i in range(3):
        if all([cell == player for cell in board[i]]):
            return True
        if all([board[j][i] == player for j in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]):
        return True
    if all([board[i][2-i] == player for i in range(3)]):
        return True
    return False

def is_full(board):
    return all(cell != " " for row in board for cell in row)

def player_move(board):
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            row, col = divmod(move, 3)
            if board[row][col] == " ":
                board[row][col] = "X"
                break
            else:
                print("Cell already taken. Try again.")
        except (ValueError, IndexError):
            print("Invalid move. Enter a number from 1 to 9.")

def computer_move(board):
    empty = [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]
    if empty:
        row, col = random.choice(empty)
        board[row][col] = "O"

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    greet()
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)
    while True:
        player_move(board)
        print_board(board)
        if check_winner(board, "X"):
            print("Congratulations! You win!")
            break
        if is_full(board):
            print("It's a tie!")
            break
        print("Computer's move:")
        computer_move(board)
        print_board(board)
        if check_winner(board, "O"):
            print("Computer wins!")
            break
        if is_full(board):
            print("It's a tie!")
            break

if __name__ == "__main__":
    main()
