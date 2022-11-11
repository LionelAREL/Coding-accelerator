import sys

try:
    a=int(sys.argv[1])
    b=int(sys.argv[2])
    if len(sys.argv) != 3 or b<0:
        raise Exception
    print(a**b)
except Exception as e:
    print("erreur.")