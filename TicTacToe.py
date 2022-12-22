from numpy import random
b = input("Would you like to go first?(y/n)")
global board
board = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
player = ' '
computer = ' '
global truth
truth = True

placeholder = {'x': '', 'o': ''}

def printboard():
    for i in range(0, 3):
        for j in range(0, 3):
            print(board[i][j] + " ", end = '')
        print()

if ((b == "y") or (b == "Y")):
    c = input("Which symbol would you like to play with?(x/o)")
    if ((c == "x") or (c == "X")):
        player = 'x'
        computer = 'o'
        placeholder['x'] = 'player'
        placeholder['o'] = 'computer'
    elif ((c == 'o') or (c == 'O')):
        player = 'o'
        computer = 'x'
        placeholder['o'] = 'player'
        placeholder['x'] = 'computer'
        
elif ((b == "n") or (b == "N")):
    c = input("Which symbol would you like to play with?(x/o)")
    if ((c == "x") or (c == "X")):
        player = 'x'
        computer = 'o'
        placeholder['x'] = 'player'
        placeholder['o'] = 'computer'
    elif ((c == 'o') or (c == 'O')):
        player = 'o'
        computer = 'x'
        placeholder['o'] = 'player'
        placeholder['x'] = 'computer'
else:
    print("Please enter a legal symbol(y/n) and execute the program again.")
    truth = False
    
def isempty():
    for i in range(0, 3):
        for j in range(0, 3):
            if board[i][j] != '_ ':
                return False
    return True
def cellcheck(i, j):
    if(type(i, j) in [1, 2, 3, 4, 5, 6, 7, 8, 9]):
        return False
    return True

def type(i, j):
    return(board[i][j])

def columncheck(i, j):
    if i == 0:
        v1 = type(i + 1, j)
        v2 = type(i + 2, j)
    elif i == 1:
        v1 = type(i - 1, j)
        v2 = type(i + 1, j)
    else:
        v1 = type(i - 1, j)
        v2 = type(i - 2, j)
    if (v1 == v2) and (type(i, j) == v1):
        print("Game over, " + placeholder[v1] + " wins!")
        truth = False
        return True
    return False

def rowcheck(i, j):
    if j == 0:
        v1 = type(i, j + 1)
        v2 = type(i, j + 2)
    elif j == 1:
        v1 = type(i, j - 1)
        v2 = type(i, j + 1)
    else:
        v1 = type(i, j - 1)
        v2 = type(i, j - 2)
    if (v1 == v2) and (type(i, j) == v1):
        print("Game over, " + placeholder[v1] + " wins!")
        truth = False
        return True
    return False

def crosscheck(i, j):
    if (i == j):
        if ((type(0, 0) == type(1, 1)) and (type(1, 1) == type(2, 2))):
           print("Game over, " + placeholder[type(i, j)] + " wins!")
           truth = False
           return True
        else:
            return False
    elif (i + j == 4):
        if ((type(0, 2) == type(1, 1))):
            if (type(1, 1) == type(2, 0)):
                print("Game over, " + placeholder[type(i, j)] + " wins!")
                truth = False
                return True
        else:
            return False
    
def GameLoop(truth):
    numberlist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    while(truth):
        printboard()
        print()
        if((b == "y") or (b == "Y")):
            #player goes first
            a = int(input("Enter a number among the ones shown in the grid")) - 1
            if (a + 1) in numberlist:
                i = int(a/3)
                j = a%3
                
                #player part
                board[i][j] = player
                numberlist.remove(a + 1)
                
                printboard()
                if(crosscheck(i, j)):
                    break
                elif (columncheck(i, j)):
                    break
                elif (rowcheck(i, j)):
                    break
                
                #computer part
                print("Thinking move...")
                x = int(random.choice(numberlist))
                x = x - 1
                i = int(x/3)
                j = x%3
                board[i][j] = computer
                numberlist.remove(x + 1)
                printboard()
                if(crosscheck(i, j)):
                    break
                elif (columncheck(i, j)):
                    break
                elif (rowcheck(i, j)):
                    break
                
            else:
                print("Please select a an empty cell")
            
            
        else:

            #player goes second
            #
            print("Thinking move...")
            x = int(random.choice(numberlist))
            x = x - 1
            i = int(x/3)
            j = x%3
            board[i][j] = computer
            numberlist.remove(x + 1)
            printboard()
            if(crosscheck(i, j)):
                break
            elif (columncheck(i, j)):
                break
            elif (rowcheck(i, j)):
                break
            #
            a = int(input("Enter a number among the ones shown in the grid")) - 1
            if (a + 1) in numberlist:
                i = int(a/3)
                j = a%3
                board[i][j] = player
                numberlist.remove(a + 1)
                
                printboard()
                if(crosscheck(i, j)):
                    break
                elif (columncheck(i, j)):
                    break
                elif (rowcheck(i, j)):
                    break
            else:
                print("Please select a an empty cell")
        
GameLoop(truth)
        
