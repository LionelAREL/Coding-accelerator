def getBoard():
    L= []
    with open('sudoku.txt',"r") as f:
        [L.append(list(line.replace("\n", "").strip())) for line in f.readlines()]

    for i in range(len(L)):
        for j in range(len(L[0])):
            if L[i][j] != "." : L[i][j] = int(L[i][j])
    return L[:]


board = getBoard()
def printBoard():
    for i in board:
        print(i)


def getEmpty():
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == ".":
                return [i,j]
    return None
                

def is_valid(value,x,y):
    for i in range(len(board[x])):
        if i != y and board[x][i] == value:
            return False

    for i in range(len(board)):
        if i != x and board[i][y] == value:
            return False

    start_block_x = x//3 * 3
    start_block_y = y//3 * 3

    for i in range(3):
        for j in range(3):
            if(board[start_block_x+i][start_block_y+j] == value):
                return False
    return True


def resolve():
    new_target = getEmpty()
    if new_target == None:
        return True
    
    for number_try in range(1,10):
        if is_valid(number_try,*new_target):
            board[new_target[0]][new_target[1]] = number_try

            if resolve() :
                return True
            board[new_target[0]][new_target[1]] = "."
    return False

printBoard()
resolve()
print("------")
printBoard()


