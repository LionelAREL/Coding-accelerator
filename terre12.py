import sys

try:
    date=sys.argv[1].split(":")
    if len(str(date[1])) != 2 or not len(str(date[0])) in [1,2]:
        raise Exception
    date[0] = int(date[0])
    date[1] = int(date[1])
    if len(sys.argv) != 2 or len(date) !=2 or not 0<=date[0]<25 or not 0<=date[1]<59 :
        raise Exception
    if date[0] == 24:
        date[0] = 0
    elif date[0] > 12:
        date[0] -= 12
    if date[0] <= 12 : print(f"{date[0]}:{date[1]}AM")
    else : print(f"{date[0]}:{date[1]}PM")
            
except Exception as e:
    print("erreur.")