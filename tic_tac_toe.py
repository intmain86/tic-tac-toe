from random import choice

print('Tic Tac Toe [Using the Numpad Layout]')

while True:
    def display_board(board):
        print(board[7],'|',board[8],'|',board[9])
        print(board[4],'|',board[5],'|',board[6])
        print(board[1],'|',board[2],'|',board[3])

    board_layout = ['-',' ',' ',' ',' ',' ',' ',' ',' ',' ']

    def player_input():
        while True:
            player_1 = input('Player 1, pick a marker X or O: ')

            if player_1 not in ('X','O'):
                print('Invalid marker. Must be uppercase X or O.')
            else:
                break

        if player_1 == 'X':
            player_2 = 'O'
        else:
            player_2 = 'X'

        print(f'Player 1 Marker: {player_1}')
        print(f'Player 2 Marker: {player_2}')
        
        return player_1, player_2
    
    player_1, player_2 = player_input()

    def place_marker(board,marker,position):
        board[position] = marker

    def check_for_win(board,marker):
        if board[7] == board[8] == board[9] == marker:
            return True
        elif board[4] == board[5] == board[6] == marker:
            return True
        elif board[1] == board[2] == board[3] == marker:
            return True
        elif board[7] == board[4] == board[1] == marker:
            return True
        elif board[8] == board[5] == board[2] == marker:
            return True
        elif board[9] == board[6] == board[3] == marker:
            return True
        elif board[7] == board[5] == board[3] == marker:
            return True
        elif board[9] == board[5] == board[1] == marker:
            return True
        return False
    
    def first_to_play():
        return choice((player_1,player_2))
    
    current_player = first_to_play()
    print(f'{current_player} starts.')

    def check_for_space(board,position):
        return board[position] == ' '
    
    def check_full_board(board):
        return ' ' not in board
    
    def player_choice(board):
        index_choice = int(input('Enter a position in the range 1-9: '))

        if not check_for_space(board,index_choice):
            return 'Occupied position.'
        else:
            return index_choice

    def play_again():
        replay = input('Replay? (Y/N): ')

        if replay.lower() == 'y':
            return True
        return False
    
    playing = True
    while playing:

        display_board(board_layout)

        index_choice = player_choice(board_layout)
        if index_choice == 'Occupied position.':
            print('This position is occupied.')
            continue

        place_marker(board_layout, current_player, index_choice)

        if check_for_win(board_layout, current_player):
            display_board(board_layout)
            print(f'{current_player} has won the game.')

            playing = False
            continue

        if check_full_board(board_layout):
            display_board(board_layout)
            print('It is a tie!')

            playing = False
            continue

        current_player = player_1 if current_player == player_2 else player_2

    if not play_again():
        break