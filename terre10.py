import sys

try:
    a=int(sys.argv[1])
    if len(sys.argv) != 2 or a<0:
        raise Exception
    print(a**(1/2))
except Exception as e:
    print("erreur.")