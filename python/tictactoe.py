# Tic Tac Toe - Christian Daga

import subprocess as sp
import random

while True:
    args = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
    turn = 'X'
    player = ''
    gameOver = False
    difficulty = 1
    winningCombos = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
    validInputs = ['1','2','3','4','5','6','7','8','9','X','O']
    
    # Prints Tic Tac Toe Board
    def tictactoe(p1,p2,p3,p4,p5,p6,p7,p8,p9): 
        print('Tic Tac Toe')
        print('_______')
        print('|'+p7+'|'+p8+'|'+p9+'|')
        print('_______')
        print('|'+p4+'|'+p5+'|'+p6+'|')
        print('_______')
        print('|'+p1+'|'+p2+'|'+p3+'|')
        print('_______')
    
    # Switches turn
    def switchTurn():
        global turn
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'
    
    # Updates Board
    def display(V):
        args[V] = turn
        sp.call('clear', shell=True)
        sp.call('cls', shell=True)
        tictactoe(*args)
        switchTurn()
    
    # Check for win
    def win():
        global gameOver
        for i in range(len(winningCombos)):
            taken = ['','','']
            tempCombo = winningCombos[i]
            for s in range(len(tempCombo)):
                taken[s] = args[tempCombo[s]-1]
            if taken[0] == taken[1] and taken[0] == taken[2] and not taken[0] == ' ':
                switchTurn()
                print(turn+' Wins!!!!')
                gameOver = True

        if not ' ' in args and not gameOver:
            print('You all suck, no one wins :,(')
            gameOver = True

    # Gets Player Move
    def playerInput():
        prompt = input('Player '+turn+': What position?(1-9): ')
        while not prompt in validInputs:
            print('Invalid Input')
        V = int(prompt)-1
        if args[V] == ' ':
            display(V)
        else:
            print('tis taken')
    
    # Initialize        
    sp.call('clear', shell=True)
    sp.call('cls', shell=True)
    tictactoe(*args)
    print('Play with Num Pad Bruh')
    tempPlayers = input('Number of players(1/2): ')
    while tempPlayers != '1' and tempPlayers != '2':
        print('Invalid Input')
        tempPlayers = input('Number of players(1/2): ')
    players = int(tempPlayers)
    if players == 1:
        tempDifficulty = input('What difficulty(1-5): ')
        while not tempDifficulty in validInputs[0:5]:
            print('Invalid Input')
            tempDifficulty = input('What difficulty(1-5): ')
        difficulty = int(tempDifficulty) * 10 + 50
        player = input('Which letter X or O: ').upper()
        while not player in validInputs[9:]:
            print('Invalid Input')
            player = input('Which letter X or O: ').upper()
    
    # 2 Player
    while not gameOver and players == 2:
        # Checks for 3 in a row or full board
        win()
        
        # Stops Game
        if gameOver:
            break
        
        # Player Input
        playerInput()
    
    # Vs Bot        
    while not gameOver and players == 1:
        # Checks for 3 in a row or full board
        win()
        
        # Stops Game
        if gameOver:
            break
        
        # Player Input
        if turn == player:
            playerInput()
                
        # Bot Input
        else:
            botWin = False
            V = random.randint(0,8)
            while args[V] != ' ':
                V = random.randint(0,8)
            missChance = random.randint(0,100)
            if missChance < difficulty:
                for i in range(len(winningCombos)):
                    taken = ['','','','']
                    tempCombo = winningCombos[i]
                    for s in range(len(tempCombo)):
                        taken[s] = args[tempCombo[s]-1]
                    if ((taken[0] == taken[1] or taken[0] == taken[2]) and taken[0] != ' ') or (taken[1] == taken[2] and taken[1] != ' '):
                        for r in range(3):
                            if taken[r] == ' ':
                                if turn in taken:
                                    botWin = True
                                V = tempCombo[r]-1
                    if botWin:
                        break
            display(V)
    
    # Play Again Prompt
    while gameOver:
        exitPrompt = input('Play Again? y/n ')
        if exitPrompt == 'n':
            break
        elif exitPrompt == 'y':
            gameOver = False
        else:
            print('Invalid Input')

    # Exits Game
    if gameOver:
        break
