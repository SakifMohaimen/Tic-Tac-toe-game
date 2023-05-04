def display(board):
    print(board[1] + "|" + board[2] + "|" + board[3])
    print("------")
    print(board[4] + "|" + board[5] + "|" + board[6])
    print("------")
    print(board[7] + "|" + board[8] + "|" + board[9])
        

def player():
    player1 = ''
    player2 = ''
    marker = input("Please Enter Player 1's marker (X or O): ")
    while player2 == '':
        player1 = marker
        player1 = player1.upper()
        if player1 == 'X':
            player2 = 'O'
        elif player1 == 'O':
            player2 = 'X'
        else :
            print("Wrong input")
            marker = input("Please Enter Player 1's marker again (X or O): ")

    return (player1, player2)



def marker_position(board, marker, position):
    board[position] = marker
    return board


def win_check(board, marker):
    return ((board[1] == board[2] == board[3] == marker) or
(board[4] == board[5] == board[6] == marker) or
(board[7] == board[8] == board[9] == marker) or
(board[1] == board[4] == board[7] == marker) or
(board[2] == board[5] == board[8] == marker) or
(board[3] == board[6] == board[9] == marker) or
(board[1] == board[5] == board[9] == marker) or
(board[3] == board[5] == board[7] == marker))


def check_full(board):
    count = 0
    for i in range (0, 10):
        if board[i] == 'X' or board[i] == 'O':
            count = count + 1
    if count == 9:
        return True
    else:
        return False



def main():
    print("Welcome to tic tac toe!")
    board = [" "] * 10
    d = display(board)
    (p1_marker, p2_marker)  = player()
    pos = 0
    another_game = 'Y'
    win = ''
    while another_game == 'Y':
        win = False
        while win != True and  not check_full(board):
            
            if p1_marker == 'X':
                print("Player1's turn.")
                pos = int(input("What's the position of your marker (1-9)? "))
                place_marker = marker_position(board, p1_marker, pos)
                display(board)
                win = win_check(board, p1_marker)
                if win == True:
                    print("Player1 is the winner!")
                if win != True and  not check_full(board):
                    print("Player2's turn.")
                    pos = int(input("What's the position of your marker (1-9)? "))
                    place_marker = marker_position(board, p2_marker, pos)
                    display(board)
                    win = win_check(board, p2_marker)
                    if win == True:
                        print("Player2 is the winner!")
            else:
                print("Player2's turn.")
                pos = int(input("What's the position of your marker (1-9)? "))
                place_marker = marker_position(board, p2_marker, pos)
                display(board)
                win = win_check(board, p2_marker)
                if win == True:
                    print("Player2 is the winner!")
                if win != True and  not check_full(board):
                    print("Player1's turn.")
                    pos = int(input("What's the position of your marker (1-9)? "))
                    place_marker = marker_position(board, p1_marker, pos)
                    display(board)
                    win = win_check(board, p1_marker)
                    if win == True:
                        print("Player1 is the winner!")
            if check_full(board) and win != True:
                    print("The game is draw")
        another_game = input("Do you want to play another game (Y or N)? ")
        if another_game == 'Y':
            board = [" "] * 10
            print("New Game!")
            display(board)
        


main()
