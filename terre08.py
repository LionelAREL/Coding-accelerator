import sys

try:
    arg=sys.argv[1]
    if len(sys.argv) != 2:
        raise Exception
    print(len(arg))
except Exception as e:
    print("erreur.")