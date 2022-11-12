def remplaceSpace(reference,to_check):
    for i in range(len(reference)):
        temp = ""
        for j in range(len(reference[0])):
            if to_check[i][j] == " ":
                temp += reference[i][j]
        to_check[i] = to_check[i].replace(" " * len(temp),temp)
    return to_check

def getBoard():
    L = []
    with open('board.txt',"r") as f:
        [L.append(line.replace("\n", "")) for line in f.readlines()]
    return L

def getFind():
    L =[]
    with open('to_find.txt',"r") as f:
        [L.append(line.replace("\n", "")) for line in f.readlines()]
    return L


F = getFind()
B = getBoard()
line_Find = len(F) 
line_Board = len(B) 
column_Board = len(B[0]) 
column_Find = max([len(F[i]) for i in range(len(F))])
# print(B,F)
if line_Find > line_Board or column_Find > column_Board :
    print("not possible")

for i in range(0,line_Board - line_Find + 1) :
    for j in range(column_Board-1,line_Find-2,-1) :
        tempBoard = B[i:i+line_Find]
        tempBoard = [tempBoard[i][j-column_Find+1:j+1] for i in range(len(tempBoard))] 
        tempFind = remplaceSpace(tempBoard,F[:])
        # print((tempBoard))
        # print((tempFind))
        if tempFind == tempBoard :
            print("Trouvé !\nCoordonnées : {},{}\n".format(i,j))

print("Introuvable")