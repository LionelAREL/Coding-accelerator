import sys

try:
    argv=sys.argv[1].split(":")
    date=argv.copy()
    if len(str(date[1])) != 4 or not len(str(date[0])) in [1,2]:
        raise Exception
    date[0] = int(date[0])
    date[1] = int(argv[1][:-2])
    date.append(argv[1][-2:])
    if len(argv[0]) != 2 or len(argv[1]) !=4 or not 0<=date[0]<13 or not 0<=date[1]<59 :
        raise Exception
    if date[0] == 12 and date[2] == "PM":
        date[0] = 0
    elif date[2] == "PM":
        date[0] += 12
    print(f"{date[0]}:{date[1]}")
            
except Exception as e:
    print("erreur.",e)