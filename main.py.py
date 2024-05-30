# Tic Tac Toe game for 7x7 board

# Initialize the board with all empty cells
board = [[' ' for j in range(7)] for i in range(7)]

# Define the function to print the board
def print_board():
    for row in board:
        print(' | '.join(row))

# Define the function to check if there's a winner
def check_winner(player):
    # Check rows for a win
    for i in range(7):
        for j in range(4):
            if all([board[i][j+k] == player for k in range(4)]):
                return True
    # Check columns for a win
    for i in range(4):
        for j in range(7):
            if all([board[i+k][j] == player for k in range(4)]):
                return True
    # Check east-south diagonal for a win
    for i in range(4):
        for j in range(4):
            if all([board[i+k][j+k] == player for k in range(4)]):
                return True
    # Check west-south diagonal for a win
    for i in range(4):
        for j in range(3, 7):
            if all([board[i+k][j-k] == player for k in range(4)]):
                return True
    return False

def evaluate_board():
    # Evaluate the board by counting the number of 3-in-a-row for each player and get a score
    x_3_in_a_row = o_3_in_a_row = 0
    for i in range(7): # row wise
        for j in range(4):
            if 'X' in [board[i][j+k] for k in range(4)] and ' ' in [board[i][j+k] for k in range(4)]:
                x_3_in_a_row += 1
            elif 'O' in [board[i][j+k] for k in range(4)] and ' ' in [board[i][j+k] for k in range(4)]:
                o_3_in_a_row += 1
    for i in range(4): # col wise
        for j in range(7):
            if 'X' in [board[i+k][j] for k in range(4)] and ' ' in [board[i+k][j] for k in range(4)]:
                x_3_in_a_row += 1
            elif 'O' in [board[i+k][j] for k in range(4)] and ' ' in [board[i+k][j] for k in range(4)]:
                o_3_in_a_row += 1
    for i in range(4): # east-south diagonal wise
        for j in range(4):
            if 'X' in [board[i+k][j+k] for k in range(4)] and ' ' in [board[i+k][j+k] for k in range(4)]:
                x_3_in_a_row += 1
            elif 'O' in [board[i+k][j+k] for k in range(4)] and ' ' in [board[i+k][j+k] for k in range(4)]:
                o_3_in_a_row += 1
    for i in range(4): # west-south diagonal wise
        for j in range(3, 7):
            if 'X' in [board[i+k][j-k] for k in range(4)] and ' ' in [board[i+k][j-k] for k in range(4)]:
                x_3_in_a_row += 1
            elif 'O' in [board[i+k][j-k] for k in range(4)] and ' ' in [board[i+k][j-k] for k in range(4)]:
                o_3_in_a_row += 1
    
    if x_3_in_a_row > o_3_in_a_row:
        return 1
    elif o_3_in_a_row > x_3_in_a_row:
        return -1
    else: return 0

# Define the function to play the game
def play_game():
    # Initialize player and turn count
    player = 'X'
    turn_count = 0
    # Loop until a winner is found or the board is full
    while turn_count < 49:
        # Print the board
        print_board()
        if player == 'X':
            # Use minimax with alpha-beta pruning to find the best move for player X
            _, row, col = minimax_alpha_beta(player, -float('inf'), float('inf'), 4)
            print("Player X's move: ({}, {})".format(row, col))
        else:
            # Ask player O for their move
            move = input("Player O, enter your move (row,column): ")
            row, col = map(int, move.split(','))
        # Check if the move is valid and update the board
        if board[row][col] == ' ':
            board[row][col] = player
            # Check if the player has won
            if check_winner(player):
                print_board()
                print("Player " + player + " wins!")
                return
            # Switch to the other player
            player = 'O' if player == 'X' else 'X'
            turn_count += 1
        else:
            print("Invalid move. Try again.")
    # If the loop finishes without a winner, it's a tie
    print_board()
    print("It's a tie!")

# Define the minimax function with alpha-beta pruning
def minimax_alpha_beta(player, alpha, beta, depth):
    """
    Implements the minimax algorithm with alpha-beta pruning to determine the best move for the computer player.

    Parameters:
        - player (string): 'X' if the current player is the computer player (maximizing player),
            'O' if the current player is the human player (minimizing player)
        - depth (int): the maximum depth of the game tree to explore
        - alpha (float): the alpha value for alpha-beta pruning
        - beta (float): the beta value for alpha-beta pruning

    Returns:
        - score, row, col
            - If the current node is a leaf node (i.e., a terminal state of the game is reached):
                - 1, None, None if player 'X' has won
                - -1, None, None if player 'O' has won
            - If the current node is not a leaf node:
                - evaluate_board(), None, None
            - Otherwise,
                - best_score, best_row, best_col to play for player 'X'
    """

    ### Add your code here ###
    #Leaf node is reached (terminal state of game)
    if depth==0 :
        if check_winner('X'):
            return 1,None,None
        #if human wins then:
        elif check_winner('O'):
            return -1,None,None
        #if human doesnt win and computer doesn't win, its a tie
        else:
            return 0,None,None
        
        
    #Go to else condition if we are NOT at a leaf node 
    else:
        #Check winning condition first at non-leaf nodes
        #if computer wins then:
        if check_winner('X'):
            return 1,None,None
        #if human wins then:
        elif check_winner('O'):
            return -1,None,None


        #if no one is winning, game continues
        #Maximizing player
        if player=='X':
            initial_value=-float('inf')
            for i in range(7):
                for j in range(7):
                    if board[i][j]==' ':
                        board[i][j]='X'
                        #we recursively call function. We are basically simulating the opponent's move and the result we get is the 
                        #best result the opponent can get and we store it. Depth is gonna decrease as we simulate other player's moves
                        value,temp_row,temp_col=minimax_alpha_beta('O',alpha,beta,depth-1)

                        board[i][j]=' '
                        #if the human (simulated) score is better, then we swap values
                        if value > initial_value:
                            initial_value=value
                            final_row=i
                            final_col=j
                            alpha=max(alpha,initial_value)

                        if alpha >= beta:
                            # i had to use a break here because if i simply just returned the initial_value,initial_row,initial_col
                            # i was getting an error
                            break

        #Minimizing player        
        elif player=='O':
            initial_value=float('inf')
            for i in range(7):
                for j in range(7):
                    if board[i][j]==' ':
                        board[i][j]='O'
                        value,temp_row,temp_col=minimax_alpha_beta('X',alpha,beta,depth-1)

                        board[i][j]=' '
                        if value < initial_value:
                            initial_value=value
                            final_row=i
                            final_col=j
                            beta=min(beta,initial_value)

                        if alpha >= beta:
                            break
                        
        return initial_value,final_row,final_col

# Start the game
play_game()
