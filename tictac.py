''' 
W01 Prove: Developer
Author: Enrique Terrones
'''
def main():
    play_again = "yes"
    while play_again == "yes":
        player = next_player("")
        board = table()
        while not (win_x(board)or win_o(board) or draw(board)):
            print_table(board)
            move(player, board)
            player = next_player(player)
        print_table(board)
        if win_x(board):
            print("Player x Won!")
        elif win_o(board):
            print("Player o Won!")
        elif draw(board):
            print("It's a Draw")
        print()

        play_again = input("Do you want to play again? (Yes/NO): ")
    print("Thanks for playing!")


def table():
    board = []
    for square in range(9):
        board.append(square + 1)
    return board

def print_table(board):
    print()
    print(f"{board[0]}|{board[1]}|{board[2]}")
    print('-+-+-')
    print(f"{board[3]}|{board[4]}|{board[5]}")
    print('-+-+-')
    print(f"{board[6]}|{board[7]}|{board[8]}")
    print()

def move(player, board):
    square = int(input(f"{player}'s turn select a square (1-9): "))
    board[square - 1] = player

def next_player(current):
    if current == "" or current == "o":
        return "x"
    elif current == "x":
        return "o"
def win_x(board):
    return (board[0] == board[1] == board[2] =="x" or
            board[3] == board[4] == board[5] =="x"or
            board[6] == board[7] == board[8] =="x"or
            board[0] == board[3] == board[6] =="x"or
            board[1] == board[4] == board[7] =="x"or
            board[2] == board[5] == board[8] =="x"or
            board[0] == board[4] == board[8] =="x"or
            board[2] == board[4] == board[6]=="x")
def win_o(board):
    return (board[0] == board[1] == board[2] =="o" or
            board[3] == board[4] == board[5] =="o"or
            board[6] == board[7] == board[8] =="o"or
            board[0] == board[3] == board[6] =="o"or
            board[1] == board[4] == board[7] =="o"or
            board[2] == board[5] == board[8] =="o"or
            board[0] == board[4] == board[8] =="o"or
            board[2] == board[4] == board[6]=="o")
def draw(board):
    for square in range(9):
        if board[square] != "x" and board[square] != "o":
            return False
    return True 

if __name__ == "__main__":
    main()