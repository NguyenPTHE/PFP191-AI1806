def draw_board(board):
    """Draws the Tic-Tac-Toe board"""
    print('   |   |')
    print(' ' + board[0] + ' | ' + board[1] + ' | ' + board[2])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[3] + ' | ' + board[4] + ' | ' + board[5])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[6] + ' | ' + board[7] + ' | ' + board[8])
    print('   |   |')

def get_player_move(board, player):
    """Gets the player's move and updates the board"""
    valid_move = False
    while not valid_move:
        move = input(f"{player}'s turn. Enter a position (1-9): ")
        if move.isdigit() and int(move) in range(1, 10):
            index = int(move) - 1
            if board[index] == ' ':
                board[index] = player
                valid_move = True
            else:
                print('That position is already taken. Try again.')
        else:
            print('Invalid input. Enter a number between 1 and 9.')
    draw_board(board)

def check_winner(board):
    """Checks if there is a winner"""
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] != ' ':
            return board[i]
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] != ' ':
            return board[i]
    if board[0] == board[4] == board[8] != ' ':
        return board[0]
    if board[2] == board[4] == board[6] != ' ':
        return board[2]
    return None

def is_board_full(board):
    """Checks if the board is full"""
    return ' ' not in board

def play_game():
    """Plays a game of Tic-Tac-Toe"""
    board = [' '] * 9
    players = ['X', 'O']
    current_player = 0
    draw_board(board)
    while True:
        get_player_move(board, players[current_player])
        winner = check_winner(board)
        if winner is not None:
            print(f"{winner} wins!")
            break
        if is_board_full(board):
            print("It's a tie!")
            break
        current_player = (current_player + 1) % 2

play_game()
