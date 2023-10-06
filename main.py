import random, time, array, math, os
from termcolor import cprint
board = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]]
solboard = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]]
def numbersRow():
    for i in range(len(solboard)):
        for j in range(len(solboard[i])):
            if solboard[i][j] != 9:
                count = 0
                if i > 0 and j > 0 and solboard[i - 1][j - 1] == 9:
                    count += 1
                if i > 0 and solboard[i - 1][j] == 9:
                    count += 1
                if i > 0 and j < len(solboard[i]) - 1 and solboard[i - 1][j + 1] == 9:
                    count += 1
                if j > 0 and solboard[i][j - 1] == 9:
                    count += 1
                if j < len(solboard[i]) - 1 and solboard[i][j + 1] == 9:
                    count += 1
                if i < len(solboard) - 1 and j > 0 and solboard[i + 1][j - 1] == 9:
                    count += 1
                if i < len(solboard) - 1 and solboard[i + 1][j] == 9:
                    count += 1
                if i < len(solboard) - 1 and j < len(solboard[i]) - 1 and solboard[i + 1][j + 1] == 9:
                    count += 1
                solboard[i][j] = count
def initBoard():
    for n in range(9):
        bomb = random.randint(0, 8)
        solboard[n][bomb] = 9

    numbersRow()
def reset():

    print()
    cprint('Welcome to MineSweeper!', 'magenta')
    cprint('=============================', 'magenta')
    print()
    cprint("Type 'I' To Receive Instructions", 'black')
    cprint("Type 'P' To Play Game", 'black')
    print()
    decision = input("Enter Choice: ")

    if decision != 'I' and decision != 'P':
        os.clear()
        print("Please Enter Either 'P' or 'I'", 'red')
        reset()

    if decision == 'I':
        print()
        cprint("Minesweeper is a classic puzzle game. To play, use the numbers given to you on the board to deduce mine placements. Flag possible mines using the 'F' key, which places a flag on the spot. If you believe there is no mine on the spot, enter 'U'. Find all 9 mines to win. Using flags incorrectly loses the game, and so does uncovering a mine without a flag. Have fun, and remember that any move can be your last! :)", 'blue')
        print()
        decision2 = input("Enter 'P' To Play Game: ")

    if decision == 'P' or decision2 == 'P':
        print()
        initBoard()
        gamePlay()
def gamePlay():
    game = True
    flags = 9
    for i in range(len(solboard)):
        for j in range(len(solboard[i])):
            if solboard[i][j] != 9 and solboard[i][j] != 0:
                n = random.randint(0, 5)
                if n > 2:
                    board[i][j] = solboard[i][j]     
    while game:

        for rows in board:
            print(rows)
        print()   
        print("You have " + str(flags) + " flags left!") 
        print()     

        row = int(input("Enter Row of Guess: ")) - 1
        col = int(input("Enter Column of Guess: ")) - 1
        type = input("Type of Marking: ")
        if flags == 0:
            for i in solboard:
                for j in i:
                    if j == 9:
                        os.system('clear')
                        print("You didn't find all the mines, you lost", 'red')
                        game = False
                        reset()
                    else:
                        os.system('clear')
                        print("You Won!!!!", 'green')
                        aaaa = input("Enter 'R' to Play Again: ")
                        if aaaa == 'R':
                            reset()
                        else:
                            os.system('clear')
        if row > 8:
            row = int(input("Enter Row of Guess: ")) - 1
        elif col > 8:
            col = int(input("Enter Column of Guess: ")) - 1
        elif row < 0:
            row = int(input("Enter Row of Guess: ")) - 1
        elif col < 0:
            col = int(input("Enter Column of Guess: ")) - 1
        elif len(type) > 1:
            type = input("Type of Marking: ")
        if type == 'U' and solboard[row][col] != 9:
            board[row][col] = 'U'
        elif flags > 0 and type == 'F':
            board[row][col] = '⚐'
            solboard[row][col] = '⚐'
            flags -= 1
        elif type == 'U' and solboard[row][col] == 9:
            os.system('clear')
            print("You died to a mine :(", 'red')
            game = False
            reset()
        else:
            print("Invalid Input", 'red')
            gamePlay()
            game = False
            reset()       
        print()    
reset()
