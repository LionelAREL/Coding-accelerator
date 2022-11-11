import sys

try:
    argv=sys.argv[1:]
    if len(argv) <= 2:
        raise Exception
    argv.sort()
    real = sys.argv[1:]
    if real == argv : print("Triée !")
    else: print("Pas triée !")
except Exception as e:
    print("erreur.",e)