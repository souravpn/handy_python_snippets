board = [" " for i in range(9)]
print(board)

def print_board():
    row_1 = "|{}|{}|{}|".format(board[0],board[1],board[2])
    row_2 = "|{}|{}|{}|".format(board[3],board[4],board[5])
    row_3 = "|{}|{}|{}|".format(board[6],board[7],board[8])

    print()
    print(row_1)
    print(row_2)
    print(row_3)
    print()

def player_move(icon):
    if icon == "X":
        player_num = 1
    else:
        player_num = 2
        
    choice = int(input("Player {}'s move... Enter you pos: ".format(player_num)).strip())
    if board[choice-1] == " ":
        board[choice-1] = icon
    else:
        print("already filled! please try again!")

def check_success(icon):
    if (board[0]==icon and board[1]==icon and board[2]==icon) or \
       (board[3]==icon and board[4]==icon and board[5]==icon) or \
       (board[6]==icon and board[7]==icon and board[8]==icon) or \
       (board[0]==icon and board[4]==icon and board[8]==icon) or \
       (board[2]==icon and board[4]==icon and board[6]==icon) or \
       (board[0]==icon and board[3]==icon and board[6]==icon) or \
       (board[1]==icon and board[4]==icon and board[7]==icon) or \
       (board[2]==icon and board[5]==icon and board[8]==icon):
        return True
    else:
        return False

while True:
    print_board()
    player_move("X")
    if check_success("X") == True:
        print_board()
        print("Player 1 won!")
        break

    print_board()
    player_move("O")
    if check_success("O") == True:
        print_board()
        print("Player 2 won!")
        break



