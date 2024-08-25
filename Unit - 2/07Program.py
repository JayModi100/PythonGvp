def print_board(board):
    """Prints the Tic-Tac-Toe board."""
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 5)
    print("\n")

def check_winner(board, player):
    """Checks if the given player has won the game."""
    # Check rows and columns
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or \
           all(board[j][i] == player for j in range(3)):
            return True
    
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] == player or \
       board[0][2] == board[1][1] == board[2][0] == player:
        return True
    
    return False

def is_board_full(board):
    """Checks if the board is full (i.e., no empty spaces)."""
    return all(cell != ' ' for row in board for cell in row)

def get_move():
    """Prompts the player to enter their move and returns it as a tuple (row, col)."""
    while True:
        try:
            move = input("Enter your move (row and column) as 'row col': ")
            row, col = map(int, move.split())
            if row in [1, 2, 3] and col in [1, 2, 3]:
                return row - 1, col - 1
            else:
                print("Invalid input. Please enter row and column as numbers from 1 to 3.")
        except ValueError:
            print("Invalid input. Please enter two numbers separated by a space.")

def play_tic_tac_toe():
    """Main function to play Tic-Tac-Toe."""
    board = [[' ' for _ in range(3)] for _ in range(3)]
    players = ['X', 'O']
    turn = 0
    
    print("Welcome to Tic-Tac-Toe!")
    
    while True:
        print_board(board)
        player = players[turn % 2]
        print(f"Player {player}'s turn.")
        
        while True:
            row, col = get_move()
            if board[row][col] == ' ':
                board[row][col] = player
                break
            else:
                print("The cell is already taken. Try again.")
        
        if check_winner(board, player):
            print_board(board)
            print(f"Player {player} wins!")
            break
        
        if is_board_full(board):
            print_board(board)
            print("The game is a draw!")
            break
        
        turn += 1

if __name__ == "__main__":
    play_tic_tac_toe()
