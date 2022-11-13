import sys

def getPlatInString(file):
    L= []
    with open(file,"r") as f:
        [L.append(list(line.replace("\n", "").strip())) for line in f.readlines()]
    return L[:]


def getPlatInBool(plat):
    L= plat[:]
    for i in range(len(L)):
        for j in range(len(L[0])):
            if L[i][j] == "." : L[i][j] = True
            else : L[i][j] = False
    return L[:]


def printPlat(plat):
    for i in plat:
        print(i)

def contain(plat,i,j,size_x,size_y):
    reference = plat[i:i+size_x + 1]
    reference = [reference[i][j:j + size_y + 1] for i in range(len(reference)) ]
    for i in range(len(reference)):
        for j in range(len(reference[0])):
            if reference[i][j] == False:
                return False
    return True

def findParameters(plat):
    plat = getPlatInBool(plat)
    position = [-1,-1]
    best_size = [-1,-1]
    for i in range(len(plat)-1):
        for j in range(len(plat[0])-1):
            for size_x in range(1,len(plat)-i+1):
                for size_y in range(1,len(plat[0])-j+1):
                    if contain(plat,i,j,size_x,size_y) and best_size[0]*best_size[1] < size_x * size_y and size_x == size_y:
                        position = [i,j]
                        best_size = [size_x,size_y]
    return (best_size[0],*position)

def printFromParameter(plat,size,position_x,position_y):
    temp = plat[:]
    for i in range(len(temp)):
        for j in range(len(temp[0])):
            if position_x <= i <= position_x + size and position_y <= j <= position_y + size:
                print("°",end="")
            else : 
                print(temp[i][j],end="")
        print("\n")

try :
    if len(sys.argv) != 2:
        raise Exception
    file=sys.argv[1]
    plat = getPlatInString(file)
    parameters = findParameters(plat)
    printFromParameter(getPlatInString(file),*parameters)
except Exception as e:
    print("erreur.")