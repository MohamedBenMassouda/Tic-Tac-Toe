board = {'1': ' ', '2': ' ', '3': ' ',
         '4': ' ', '5': ' ', '6': ' ',
         '7': ' ', '8': ' ', '9': ' '}


def printBoard(board):
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print(board['7'] + '|' + board['8'] + '|' + board['9'])


def play():
    turn = "X"
    count = 0

    for i in range(10):
        printBoard(board)
        print("It's your turn", turn, ". Your move? ")
        move = input()

        if board[move] == ' ':
            board[move] = turn
            count += 1

        else:
            print("Invalid.")
            continue

        if count >= 5:
            if board['1'] == board['2'] == board['3'] != ' ':
                printBoard(board)
                print("\nGame Over\n")
                print(turn, "Won")
                break

            elif board['4'] == board['5'] == board['6'] != ' ':
                printBoard(board)
                print("\nGame Over\n")
                print(turn, "Won")
                break

            elif board['7'] == board['8'] == board['9'] != ' ':
                printBoard(board)
                print("\nGame Over\n")
                print(turn, "Won")
                break

            elif board['1'] == board['4'] == board['7'] != ' ':
                printBoard(board)
                print("\nGame Over\n")
                print(turn, "Won")
                break

            elif board['2'] == board['5'] == board['8'] != ' ':
                printBoard(board)
                print("\nGame Over\n")
                print(turn, "Won")
                break

            elif board['3'] == board['6'] == board['9'] != ' ':
                printBoard(board)
                print("\nGame Over\n")
                print(turn, "Won")
                break

            elif board['1'] == board['5'] == board['9'] != ' ':
                printBoard(board)
                print("\nGame Over\n")
                print(turn, "Won")
                break

            elif board['3'] == board['5'] == board['9'] != ' ':
                printBoard(board)
                print("\nGame Over\n")
                print(turn, "Won")
                break

        if count == 9:
            print(board)
            print("It' a tie.")

        if turn == "X":
            turn = "O"

        else:
            turn = "X"

play()