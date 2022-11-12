def getPatString():
    L= []
    with open('plateau.txt',"r") as f:
        [L.append(list(line.replace("\n", "").strip())) for line in f.readlines()]
    return L


def getPlat():
    L= getPatString()
    for i in range(len(L)):
        for j in range(len(L[0])):
            if L[i][j] == "." : L[i][j] = True
            else : L[i][j] = False
    return L[:]

plat = getPlat()

def printPlat():
    for i in plat:
        print(i)

def contain(i,j,size_x,size_y):
    reference = plat[i:i+size_x + 1]
    reference = [reference[i][j:j + size_y + 1] for i in range(len(reference)) ]
    # print(reference)
    for i in range(len(reference)):
        for j in range(len(reference[0])):
            if reference[i][j] == False:
                # print(reference)
                return False
    return True

position = [-1,-1]
best_size = [-1,-1]
for i in range(len(plat)-1):
    for j in range(len(plat[0])-1):
        for size_x in range(1,len(plat)-i+1):
            for size_y in range(1,len(plat[0])-j+1):
                if contain(i,j,size_x,size_y) and best_size[0]*best_size[1] < size_x * size_y and size_x == size_y:
                    position = [i,j]
                    best_size = [size_x,size_y]
                    # print(i,j)
# printPlat()
# print(position)
# print(best_size)

temp = getPatString()
# print(temp)

for i in range(len(temp)):
    for j in range(len(temp[0])):
        if position[0] <= i <= position[0] + best_size[0] and position[1] <= j <= position[1] + best_size[0]:
            print("°",end="")
        else : 
            print(temp[i][j],end="")
    print("\n")